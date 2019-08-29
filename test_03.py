import requests
import unittest
from mock import patch
'''实现功能：主要了解@patch.object(SomeClass, 'class_method');
@patch.object(SomeClass, 'class_method')
... def test(mock_method):
...     SomeClass.class_method(3)
...     mock_method.assert_called_with(3)'''


class PayApi():

    @staticmethod
    def auth(card,amount):
        pay_url = "http:moni.com"
        data = {"card":card,"amount":amount}
        response = requests.post(pay_url,data = data)
        return response

    def pay(self,user_id,card,amount):
        response = self.auth(card,amount)
        try:
            if response['status_code'] == '200':
                print("用户{}支付金额{}成功".format(user_id,amount))
                return "支付成功"
            elif response['status_code'] == '500':
                print("用户{}支付失败，金额不变".format(user_id))
                return "支付失败"
            else:
                return "未知错误"
        except Exception:
            return "Error, 服务器异常!"


class TestPayApi(unittest.TestCase):

    def setUp(self):
        self.pay = PayApi()

    def tearDown(self):
        pass

    #
    @patch.object(PayApi,'auth')
    def test_success(self,mock_auth):
        mock_auth.return_value =  {'status_code':'200'}
        statusmsg = self.pay.pay('1000','12345','10000')
        self.assertEqual(statusmsg,'支付成功')

    @patch.object(PayApi,'auth')
    def test_fail(self,mock_auth):
        mock_auth.return_value = {'status_code':'500'}
        statusmsg = self.pay.pay('jsdn','6222xxx','10000')
        self.assertEqual(statusmsg,'支付失败')

    @patch.object(PayApi,'auth')
    def test_error(self,mock_auth):
        mock_auth.return_value = {'status_code':'300'}
        statusmsg = self.pay.pay('jsdn', '6222xxx', '20000')
        self.assertEqual(statusmsg,'未知错误')

    @patch.object(PayApi, 'auth')
    def test_exception(self, mock_auth):
        mock_auth.return_value = {'status_codeq':'300'}
        statusmsg = self.pay.pay('jsdn', '6222xxx', '20000')
        self.assertEqual(statusmsg, 'Error, 服务器异常!')


if __name__ == '__main__':
    unittest.main(verbosity=2)







