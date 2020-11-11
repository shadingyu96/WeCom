from api_page.page_api import BasePage
from api_page.wework_utills import WeWorkUtills


class AddressApi(BasePage):
    def __init__(self):
        corpsecret = "lsgkRCZorU9MLTU7h-f7s0S7fOA4-fXIJutzJChxxIk"
        self.token = WeWorkUtills().get_token(corpsecret)

    # 创建成员
    def creat(self, userid, name):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {
                "access_token": self.token,
                "userid": userid,
                "name": name
        }
        }
        return BasePage.send_api(data)
