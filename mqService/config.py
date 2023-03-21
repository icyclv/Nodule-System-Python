
## Model configuration
model_config = {
                "seg_model" :"nodulenet",
                "detect_model" : None,
                "classification_model" : "nasnet",
                "lung_model" : "lungmask"
                }


#service configuration
rabbitmq_config = {"host": "192.168.159.188",
                     "port": 5672,
                     "username": "admin",
                     "password": "123"}

minio_config = {
    "endpoint": "192.168.159.188:9000",
    "accessKey": "root",
    "secretKey": "chang2001",
    "bucketName": "medical-images"
}

ORIGIN_SUFFIX = "_origin.npz"
RESULT_SUFFIX = "_result.npz"