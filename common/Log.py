import logging  # 导入日志组件.
import datetime
import os


class Logging():
        def __init__(self,case):
            self.case=case  
            now = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S') # 文件名的格式.
            file_path = os.path.dirname(__file__)
            log_path = file_path.replace('common','log')
            logging.basicConfig(level=logging.DEBUG,    # 如果不想看debug，就把DEBUG改成INFO
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                                datefmt='%a, %d %b %Y %H:%M:%S',
                                filename=log_path + '/' + now + r"result.log",
                                filemode='w')
            logger = logging.getLogger()
            logger.info(case)


