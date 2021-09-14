import logging #python字典
from tools import project_path
class MyLog:
    def my_log(self,msg,level):
        my_logger=logging.getLogger('接口测试')
        my_logger.setLevel('DEBUG')
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        ch=logging.StreamHandler()
        ch.setLevel('ERROR')
        ch.setFormatter(formatter)
        fh=logging.FileHandler(project_path.log_path,encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)
        if level=='DEBUG':
            my_logger.debug(msg)
        elif level=='INFO':
            my_logger.info(msg)
        elif level=='WARNING':
            my_logger.warning(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        elif level=='CRITICAL':
            my_logger.critical(msg)
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self,msg):
        self.my_log(msg,'DEBUG')

    def info(self,msg):
        self.my_log(msg,'INFO')

    def error(self,msg):
        self.my_log(msg,'ERROR')

    def warning(self,msg):
        self.my_log(msg,'WARNING')

    def critical(self,msg):
        self.my_log(msg,'CRITICAL')
