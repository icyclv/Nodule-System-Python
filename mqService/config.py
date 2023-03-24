
## Model configuration

import os

import yaml

def get_yaml_config():
    path = os.path.join(os.getcwd(), 'config.yaml')
    f = open(path, encoding='utf-8')
    file = yaml.safe_load(f)
    rabbitmq_config = file['rabbitmq_config']
    model_config = file['model_config']
    minio_config = file['minio_config']
    ORIGIN_SUFFIX = file['ORIGIN_SUFFIX']
    RESULT_SUFFIX = file['RESULT_SUFFIX']
    return model_config, rabbitmq_config, minio_config, ORIGIN_SUFFIX, RESULT_SUFFIX






model_config,rabbitmq_config, minio_config, ORIGIN_SUFFIX, RESULT_SUFFIX = get_yaml_config()