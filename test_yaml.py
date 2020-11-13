"""
@File : test_yaml.py
@Author: Sardine
@Date : 2020/11/13
@Desc : 把字典转化为yaml格式
"""
import yaml


def test_send():
    """传入字典，输出yaml格式"""
    data = {
        "get_user": {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {"access_token": "self.token",
                       "userid": "userid"}
        }
    }
    yaml2 = yaml.safe_dump(data)
    print('')
    print(yaml2)


if __name__ == '__main__':
    test_send()
