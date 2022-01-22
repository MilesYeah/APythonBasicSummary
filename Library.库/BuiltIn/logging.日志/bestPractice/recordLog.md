```py
import logging
import os
from datetime import datetime
 
 
class RecordLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
 
        # 2.将log信息输出到log文件中
        # 2.1 先定位看将log文件输出到哪里去
        current_dir = os.path.dirname(os.path.abspath(__file__))
        print(current_dir)  # D:\MySpace\Python\WebTesting\util
        log_dir = os.path.join('../logs')
        # 日志名称构建
        log_file_name = datetime.now().strftime("%Y-%m-%d") + '.log'
        log_file_path = log_dir + '/' + log_file_name
        print(log_file_path)
 
        # 2.2 好的，将日志写进log文件中
        self.file_handle = logging.FileHandler(log_file_path, 'a', encoding='utf-8')
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s %(funcName)s %(levelno)s: [%(levelname)s] ---> %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)
 
    def get_log(self):
        return self.logger
 
    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()
 
 
if __name__ == "__main__":
    rl = RecordLog()
    log_info = rl.get_log()
    log_info.debug('输出到文件中去')
    rl.close_handle()
```



## ref
* [python和selenium实现Web自动化(6)：日志处理](https://blog.csdn.net/weixin_48500307/article/details/108451056)
