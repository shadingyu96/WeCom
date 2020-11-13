from Utils.config import cf
from api.base_api import BasePage


class WeWork(BasePage):
    corp_id = cf.get_value("we_work", "corp_id")
    token_url = cf.get_value("we_work", "token_url")
    token = dict()

    def get_access_token(self, secret):
        data = {
            "method": "get",
            "url": self.token_url,
            "params": {"corpid": self.corp_id, "corpsecret": secret}
        }
        result = self.send_api(data)
        return result

    def get_token(self, secret):
        # 避免重复请求，提高速度
        if secret not in self.token.keys():
            result = self.get_access_token(secret)
            self.token[secret] = result["access_token"]
            # print(self.token)
        return self.token[secret]


if __name__ == '__main__':
    secret = cf.get_value("we_work", "contact_secret")
    print(secret)
    a = WeWork()
    print(a.corp_id)
    # secret = "lsgkRCZorU9MLTU7h-f7s0NsC_AJYoc9z7jWzwW2JlQ"
    print(a.get_token(secret))