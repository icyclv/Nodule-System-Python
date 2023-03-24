# Nodule-System-Python

#### 介绍

Rabbitmq和Pytorch的推理端

## 注意
其中模型文件需要手动下载：

链接：https://pan.baidu.com/s/1MAo3kcJYf6ZRf78iZd0FNg?pwd=xyfn 
提取码：xyfn 

放置在model文件夹中


## 项目说明
所需中间件：Rabbitmq、Minio


处理信息：Rabbitmq接收到消息后，从Minio中获取文件，进行处理推理，处理完成后将结果上传到Minio中，同时将结果消息发送到Rabbitmq中，有Java服务端接收并更新任务状态

#### 环境配置

待更新...

其中为加速NMS计算：
    
    cd build/box
    python setup.py install

如果出现错误，可以不安装，但速度会慢一些