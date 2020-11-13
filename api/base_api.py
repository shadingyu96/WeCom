import os
from string import Template

import requests
import yaml

from Utils.config import cf
from Utils.get_log import log
from Utils.utils import Utils


class BasePage:
    """
    api的抽象类
    """
    json_data = None
    # 通过配置文件获取测试的环境的ip地址
    ip = cf.get_value("env", "formal_ip")
    Base_Path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    def send_api(self, data: dict):
        return requests.request(**data).json()

    def jsonpath(self, expr):
        return Utils.jsonpath(self.json_data, expr)

    @classmethod
    def load_yaml(cls, path, sub=None):
        """
        封装读取yaml的代码，通过路径直接读取yaml文件并转化为python的数据类型
        :param path: yml文件的相对路径
        :type path: str
        :param sub: 可读取下一级目录
        :type sub: yaml文件的数据类型
        :return: 返回读取的数据
        :rtype: data
        """
        path1 = os.path.join(cls.Base_Path, path)
        with open(path1, encoding="utf-8") as f:
            # 不写sub就获取yml中所有的内容，写就获取yml的二级目录
            if sub is None:
                return yaml.safe_load(f)
            else:
                return yaml.safe_load(f)[sub]

    @classmethod
    def dump_yaml(cls, path):
        path1 = os.path.join(cls.Base_Path, path)
        with open(path1, "r+", encoding="utf-8") as f:
            yaml.safe_dump(f)

    @classmethod
    def template(cls, path, data, sub=None):
        path1 = os.path.join(cls.Base_Path, path)
        with open(path1, encoding="utf-8") as f:
            if sub is None:
                '''
                不需要对数据进行二次提取，Template(f.read()).substitute(data)先替换变量
                yaml.safe_load把yml格式的字符串变成dict类型返回
                '''
                return yaml.safe_load(Template(f.read()).substitute(data))
            else:
                '''
                由于Template需要替换全部的变量，有漏的就会报错，先写Template(f.read()).substitute(data)
                就会报错，data只对sub下一层的数据改，并没有改其他层的数据，肯定会报错
                需要先yaml.safe_load(f)[sub]提取到下一层的数据，但由于是dict
                要通过yaml.dump转化成yml格式的字符串，经过Template来改变变量，最后在yaml.safe_load转化成dict
                '''
                return yaml.safe_load(Template(yaml.safe_dump(yaml.safe_load(f)[sub])).substitute(data))

    def send_api_data(self, path, p_data, sub=None):
        data: dict = self.template(path, p_data, sub)
        log.info(f"请求的参数是{data}")
        return self.send_api(data)


if __name__ == '__main__':
    a = BasePage()
    print(a.load_yaml("data/contact_api.yml", "get_user"))
