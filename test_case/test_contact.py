import pytest

from Utils.get_log import log
from api.Contact_api import ContactApi


class TestContact:
    def setup_class(self):
        self.api = ContactApi()

    @pytest.mark.parametrize("userid, name, department, mobile", [("zhangsan10", "夏星星4", [1], "13760025988"), ("lisi9", "夏星星5", [1], "13750034618")])
    def test_create_user(self, userid, name, department, mobile):
        r = self.api.create_user(userid, name, department, mobile)
        log.info("-------------开始增加成员测试---------")
        print(r)
        log.info("-------------测试结束---------")
        assert r["errcode"] == 0 and r["errmsg"] == "created"

    @pytest.mark.parametrize("userid, name", [("zhangsan10", "夏星星4")])
    def test_get_user(self, userid, name):
        r = self.api.get_user(userid, name)
        print(r)
        assert r["errcode"] == 0

    @pytest.mark.parametrize("userid, name", [("zhangsan10","夏星星4")])
    def test_update_user(self, userid, name):
        r = self.api.update_user(userid, name)
        print(r)
        assert r["errcode"] == 0 and r["errmsg"] == "updated"
