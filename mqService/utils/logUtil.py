import logging
import os
import sys
import time
from logging import handlers

level_relations = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'crit': logging.CRITICAL
}

def get_logger(dir,filename_prefix, level='info'):
    log_dir_path = os.path.join(os.getcwd(), dir)
    if os.path.exists(log_dir_path) == False:
        os.makedirs(log_dir_path)
    filename = os.path.join(log_dir_path, filename_prefix)
    logger = logging.getLogger("logger")

    # 设置日志输出的最低等级,低于当前等级则会被忽略
    logger.setLevel(level_relations.get(level))

    # 创建处理器：sh为控制台处理器，fh为文件处理器
    sh = logging.StreamHandler()

    # 创建处理器：sh为控制台处理器，fh为文件处理器,log_file为日志存放的文件夹
    # log_file = os.path.join(log_dir,"{}_log".format(time.strftime("%Y/%m/%d",time.localtime())))
    fh = logging.FileHandler(filename, encoding="UTF-8")

    # 创建格式器,并将sh，fh设置对应的格式
    formator = logging.Formatter(fmt="%(asctime)s %(filename)s %(levelname)s %(message)s",
                                 datefmt="%Y/%m/%d %X")
    sh.setFormatter(formator)
    fh.setFormatter(formator)

    # 将处理器，添加至日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)

    return logger



logger = get_logger('logs',"{}_log.log".format(time.strftime("%Y-%m-%d",time.localtime())) , 'info')
