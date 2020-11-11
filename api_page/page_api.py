import requests


class BasePage:
    """
    api的抽象类
    """
    def send_api(self, data: dict):
        return requests.request(**data).json()
