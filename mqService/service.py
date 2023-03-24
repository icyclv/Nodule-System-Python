import io
import json
import os.path
import random
from datetime import timedelta

import numpy as np
import pika

import pika
import time

import requests
from minio import Minio

from config import rabbitmq_config, model_config, minio_config, ORIGIN_SUFFIX, RESULT_SUFFIX

from mqService.utils.logUtil import logger
from net.ModelConstant import load_model
from utils.detect import detect


def process(name):
    url = minio_client.presigned_get_object(minio_config["bucketName"], name, expires=timedelta(minutes=10))
    req = requests.get(url)

    file = np.load(io.BytesIO(req.content), allow_pickle=True)
    img, spacing = file['img'], file['spacing']
    return img, spacing

def upload(buf,name):
    value = buf.getvalue()
    minio_client.put_object(minio_config["bucketName"], name, io.BytesIO(value), len(value))

def inference(scan_id,name):
    origin_name = name+ORIGIN_SUFFIX
    upload_name = name+RESULT_SUFFIX
    img, spacing=process(origin_name) #获取数据
    result,buf=detect(img,spacing,seg_model, detect_model, classification_model, lung_model, scan_id) #检测
    upload(buf,upload_name) #上传
    return result



def callback(ch, method, properties, body):
    body = json.loads(body)
    logger.info(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " [x] Received %r" % body)

    scan_id = body["scanId"]
    name = body["fileName"]

    try:

        result = inference(scan_id,name)

        res = {
            "success": True,
            "scanId": scan_id,
            "noduleList": result
        }

        channel.basic_publish(exchange='NoduleExchange', routing_key='NoduleResult', body= json.dumps(res))
        ch.basic_ack(delivery_tag=method.delivery_tag)
        logger.info(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " [x] Done %r" % body)
    except Exception as e:
        res = {
            "success": False,
            "scanId": scan_id,
        }
        channel.basic_publish(exchange='NoduleExchange', routing_key='NoduleResult', body=json.dumps(res))

        logger.error(e)
        # 报告错误，并且重新放回队列，


        channel.basic_nack(delivery_tag=method.delivery_tag, requeue=True) #s 可能是显存不足，这种情况可以放回队列让其他服务器处理


if __name__ == "__main__":
    # 连接rabbitmq
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(rabbitmq_config["host"], port=int(rabbitmq_config["port"]),
                              credentials=pika.PlainCredentials(rabbitmq_config["username"], rabbitmq_config["password"])))
    channel = connection.channel()
    channel.exchange_declare("NoduleExchange", "direct", durable=True)
    channel.queue_declare(queue='NoduleInferenceQueue', durable=True)
    channel.queue_bind(queue='NoduleInferenceQueue', exchange='NoduleExchange', routing_key='NoduleInference')
    channel.queue_declare(queue='NoduleResultQueue', durable=True)
    channel.queue_bind(queue='NoduleResultQueue', exchange='NoduleExchange', routing_key='NoduleResult')

    #加载模型
    seg_model, detect_model, classification_model, lung_model=load_model(model_config["seg_model"], model_config["detect_model"], model_config["classification_model"], model_config["lung_model"])


    #minio
    minio_client = Minio(
        endpoint=minio_config["endpoint"],
        access_key=minio_config["accessKey"],
        secret_key=minio_config["secretKey"],
        secure=False
    )
    # 设置日志，文件名为当前时间
    #




    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='NoduleInferenceQueue', auto_ack=False, on_message_callback=callback)

    logger.info(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
