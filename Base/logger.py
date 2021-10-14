import logging  # 引入logging模块
import os.path
import time


class Log(object):

    def __init__(self, logger_name):

        # 第一步，创建一个logger
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)  # Log等级总开关

        # 第二步，创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d-%H_%M', time.localtime(time.time()))
        log_path = os.path.dirname(os.getcwd()) + '/Logs/'
        log_name = log_path + rq + '.log'
        logfile = log_name
        fh = logging.FileHandler(logfile, mode='w', encoding='utf-8')
        fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
        # 第三步，定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        # 第四步，将logger添加到handler里面
        self.logger.addHandler(fh)

    def get_log(self):
        return self.logger


# # 日志
# logger.debug('this is a logger debug message')
# logger.info('this is a logger info message')
# logger.warning('this is a logger warning message')
# logger.error('this is a logger error message')
# logger.critical('this is a logger critical message')
