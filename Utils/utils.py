from jsonpath import jsonpath


class Utils:
    @classmethod
    def jsonpath(cls, json_object, expr):
        """
        jsonpath的方法
        :param json_object:
        :type json_object:
        :param expr:
        :type expr:
        :return:
        :rtype:
        """
        return jsonpath(json_object, expr)

    # def