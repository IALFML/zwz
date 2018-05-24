import logging

class log:
    def __init__(self):
        pass

    def printlog(self,level,message):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        #用于写入日志文件
        logfile = r'C:\Users\admin\PycharmProjects\python\xybao\log\logger.txt'
        fh = logging.FileHandler(logfile, mode='a')
        fh.setLevel(logging.INFO)

        # 用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 将logger添加到handler里面
        logger.addHandler(fh)
        logger.addHandler(ch)

        # 日志
        if level=="debug":
            logger.debug(message)
        elif level =="info":
            logger.info(message)
        elif level=="warning":
            logger.warning(message)
        elif level=="error":
            logger.error(message)
        else:
            logger.critical(message)

    def debug(self,message):
        self.printlog("debug",message)

    def info(self, message):
        self.printlog("info", message)

    def warning(self, message):
        self.printlog("warning",message)

    def error(self, message):
        self.printlog("error", message)

    def critical(self, message):
        self.printlog("critical", message)


# # 打印日志
# def printlog(level,message):
#     # 第一步，创建一个logger
#     logger = logging.getLogger()
#     logger.setLevel(logging.INFO)  # Log等级总开关
#
#     # 第二步，创建一个handler，用于写入日志文件
#     logfile = 'D:/pycharm/python/Test_project/Log/logger.txt'
#     fh = logging.FileHandler(logfile, mode='a')
#     fh.setLevel(logging.INFO)  # 输出到file的log等级的开关
#
#     # 第三步，再创建一个handler，用于输出到控制台
#     ch = logging.StreamHandler()
#     ch.setLevel(logging.INFO)  # 输出到console的log等级的开关
#
#     # 第四步，定义handler的输出格式
#     formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
#     fh.setFormatter(formatter)
#     ch.setFormatter(formatter)
#
#     # 第五步，将logger添加到handler里面
#     logger.addHandler(fh)
#     logger.addHandler(ch)
#
#     # 日志
#     if level=="debug":
#         logger.debug(message)
#     elif level =="info":
#         logger.info(message)
#     elif level=="warning":
#         logger.warning(message)
#     elif level=="error":
#         logger.error(message)
#     else:
#         logger.critical(message)


if __name__=="__main__":
    t=log()
    t.info("zwz")