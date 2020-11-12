from api_page.page_api import BasePage
from api_page.wework_utilise import WeWorkUtilise


class AddressApi(BasePage):
    def __init__(self):
        _corpsecret = "lsgkRCZorU9MLTU7h-f7s0NsC_AJYoc9z7jWzwW2JlQ"
        self.token = WeWorkUtilise().get_token(_corpsecret)

    # 创建成员
    def create_user(self, userid, name, department, mobile, **kwargs):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {"access_token": self.token},
            "json": {
                "userid": userid,
                "name": name,
                "department": department,
                "mobile": mobile,
                "alias": kwargs["alias"]
            }
        }
        return self.send_api(data)

    # 读取成员
    def get_user(self, userid, name):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {"access_token": self.token,
                       "userid": userid}
        }
        return self.send_api(data)

    # 更新成员
    def update_user(self, userid, name):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params": {"access_token": self.token},
            "json": {
                "userid": userid
            }

        }
        return self.send_api(data)

    # 删除成员
    def delete_user(self, userid):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params": {"access_token": self.token,
                       "userid": userid
                       }
        }
        return self.send_api(data)

    # 批量删除成员
    def batchdelete_user(self, useridlist: list):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete",
            "params": {"access_token": self.token,
                       "userid": useridlist
                       }
        }
        return self.send_api(data)

    # 获取部门成员
    def simplelist_user(self, department_id: str, **kwargs):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
            "params": {"access_token": self.token,
                       "department_id": department_id,
                       "fetch_child": kwargs["fetch_child"]
                       }
        }
        return self.send_api(data)
