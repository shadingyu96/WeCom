from Utils.config import cf
from api.wework import WeWork


class ContactApi(WeWork):
    def __init__(self):
        _corp_secret = cf.get_value("we_work", "contact_secret")
        self.token = self.get_token(_corp_secret)
        self.path = "data/contact_api.yml"

    # 创建成员
    def create_user(self, userid, name, department, mobile, alias=None):
        # template替换yaml中的数据
        p_data = {'token': self.token, 'ip': self.ip, 'userid': userid, 'name': name,
                  'department': department, 'mobile': mobile, 'alias': alias}
        return self.send_api_data(self.path, p_data, "create_user")

    # 读取成员
    def get_user(self, userid, name=None):
        p_data = {'token': self.token, 'ip': self.ip, 'userid': userid, 'name': name}
        return self.send_api_data(self.path, p_data, "get_user")

    # 更新成员
    def update_user(self, userid, name=None):
        p_data = {'token': self.token, 'ip': self.ip, 'userid': userid, 'name': name}
        return self.send_api_data(self.path, p_data, "update_user")

    # 删除成员
    def delete_user(self, userid):
        p_data = {'token': self.token, 'ip': self.ip, 'userid': userid}
        return self.send_api_data(self.path, p_data, "delete_user")

    # 批量删除成员
    def batchdelete_user(self, useridlist: list):
        p_data = {'token': self.token, 'ip': self.ip, 'useridlist': useridlist}
        return self.send_api_data(self.path, p_data, "batchdelete_user")

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

if __name__=="__main__":
    a=ContactApi()
    print(a.create_user("tong", "tong", 1, "13172661165"))