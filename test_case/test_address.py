import pytest

from api_page.address_api import AddressApi


class TestAddress:
    def setup_class(self):
        self.api = AddressApi()

    @pytest.mark.parametrize("userid, name, department, mobile", [("zhangsan1", "夏星星1", [1], "1376002598282"), ("lisi", "夏星星2", [1], "13750034616")])
    def test_create_user(self, userid, name, department, mobile):
        r = self.api.create_user(userid, name, department, mobile)
        print(r)
        assert r["errcode"] == 0 and r["errmsg"] == "created"