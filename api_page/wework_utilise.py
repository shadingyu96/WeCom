from api_page.page_api import BasePage


class WeWorkUtilise(BasePage):
    def get_token(self, corpsecret, corpid="wwf55a566b6d1c6bd3"):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {"corpid": corpid, "corpsecret": corpsecret}
        }
        results = self.send_api(data)
        return results["access_token"]
