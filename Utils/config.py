import configparser
import os


class ConfigIni:
    # 项目的绝对路径
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 获取当前的路径，读取config.ini文件
    config_file_path = os.path.join(BASE_PATH, "config.ini")

    def __init__(self, file_path=config_file_path):
        """
        默认读取config.ini文件，也可以修改其他路径
        :param file_path: 读取文件路径
        :type file_path: str
        """
        # 为了让写入文件的路径是唯一值，所以这样定义下来
        self.file_path = file_path
        # 定义配置文件的对象
        self.cf = configparser.ConfigParser()
        # 读取配置文件
        self.cf.read(file_path)

    def get_value(self, section, option):
        """
        获取配置文件的value值
        :param section: 配置文件中的section值
        :type section: str
        :param option: 配置文件中的option值
        :type option: str
        :return: value值
        :rtype: str
        """
        value = self.cf.get(section, option)
        return value

    def set_value(self, section, option, value):
        """
        修改配置文件的value值
        :param section: 配置文件中的section值
        :type section: str
        :param option: 配置文件中的option值
        :type option: str
        :return: value值
        :rtype: str
        """
        # python内存中先修改值
        self.cf.set(section, option, value)
        with open(self.file_path, "w+") as f:
            self.cf.write(f)


cf = ConfigIni()

if __name__ == '__main__':
    print(cf.get_value("we_work", "corp_id"))
