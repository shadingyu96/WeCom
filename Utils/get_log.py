"""
@File : get_log.py
@Author: Sardine
@Date : 2020/11/13
@Desc : 获取log日志
"""
import logging
import os
import datetime
from Utils.config import cf


class Log:
    # 项目的绝对路径
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 生成的格式化器
    formatter = logging.Formatter("%(asctime)s|%(levelname)-6s|%(filename)s:%(lineno)-3s|%(message)s", "%Y-%m-%d-%H:%M")

    def __init__(self, name="logs"):
        """
        初始化生成器
        :param name: 生成器的名字
        :type name: str
        """
        self.log_name = name
        # 生成记录器
        self.looger = logging.getLogger(name)
        # 默认等级都是最低级别的DEBUG，因为记录器的默认等级优先级高于处理器的
        self.looger.setLevel(logging.DEBUG)

    def set_stream(self):
        """
        初始化流处理器
        :return:
        :rtype:
        """
        # 生成处理器流处理器
        console_handle = logging.StreamHandler()
        # 设置默认等级为DEBUG
        console_handle.setLevel(logging.DEBUG)
        # 处理器添加格式
        console_handle.setFormatter(self.formatter)
        # 记录器添加处理器，就会拥有了屏幕输出和文件输出的日志了
        self.looger.addHandler(console_handle)

    def set_file(self):
        """
        初始化文件处理器
        :return:
        :rtype:
        """
        # 生成日期： 创造Log_2020-12-13.log文件
        a = self.log_name + "_" + str(datetime.date.today()) + ".log"
        # b是最终的文件路径，在根路径的logs文件夹下
        b = os.path.join(self.BASE_PATH, "log", a)
        # 通过配置文件，获取log是w模式还是a的追加模式
        file_mode = cf.get_value("logs", "file_mode")
        # 文件处理器，文件名为demo.logs
        file_handle = logging.FileHandler(filename=b, mode=file_mode)
        # 默认等级为INFO
        file_handle.setLevel(logging.INFO)
        # 处理器添加格式
        file_handle.setFormatter(self.formatter)
        # 记录器添加处理器，就会拥有了屏幕输出和文件输出的日志了
        self.looger.addHandler(file_handle)

    def get_log(self):
        """
        运行创建文件处理器和流处理器的代码，最终返回一个logger对家
        :return: logger对象
        :rtype:
        """
        # 创建文件处理器
        self.set_file()
        # 创建流处理器
        self.set_stream()
        # 返回记录器，拥有文件和流的处理器和格式，可以输出日志了
        return self.looger

log = Log().get_log()

if __name__ == '__main__':
    log.error("abdc")