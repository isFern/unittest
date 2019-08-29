import unittest
import xmlrunner
import HTMLTestRunner
import time
'''实现功能：不同方式添加test_case,且运行生成不同样式的测试报告；'''


class Test(unittest.TestCase):

    flag = 1
    '''setUp() 在每个测试方法执行前执行一次,tearDown() 在每个测试方法执行后执行一次，
    如本例子的test_Add1和test_Add2 ；
    setUp用来为准备测试环境和数据，tearDown用来清理环境和数据，以备之后的测试'''
    '''类方法 setUpClass() 在所有测试方法开始执行前执行一次,
     tearDownClass() 在所有测试方法执行后执行一次'''

    def setUp(self):
        print("每个测试case开始执行前执行")

    def tearDown(self):
        print("每个测试case结束执行后执行")

    @classmethod
    def setUpClass(cls):
        print("所有测试case开始执行前执行")

    @classmethod
    def tearDownClass(cls):
        print("所有测试case结束执行后执行.")

    def add(self,a,b):
        return a+b

    # 每个测试方法均以 test 开头，否则是不被unittest识别的。
    def test_Add1(self):
        print('test_Add1')
        self.assertEqual(3,self.add(1,2))

    def test_Add2(self):
        print('test_Add2')
        self.assertEqual(3,self.add(1,4))

    '''skip装饰器一共有三个
    unittest.skip(reason)

    unittest.skipIf(condition, reason)

    unittest.skipUnless(condition, reason)

    skip无条件跳过，skipIf当condition为True时跳过，skipUnless当condition为False时跳过'''
    @unittest.skip("跳过tes_Add3")
    def test_Add3(self):
        self.assertEqual(6,self.add(2,4))
        print('test_Add3')

    @unittest.skipIf(flag == 1, "当condition为True时跳过")
    def test_Add4(self):
        print('test_Add4')
        self.assertEqual(6,self.add(2,4))

    @unittest.skipUnless(flag == 1, "当condition为False时跳过")
    def test_Add5(self):
        print('test_Add5')
        self.assertEqual(6, self.add(2, 4))


if __name__ == '__main__':

    test_suite = unittest.TestSuite()
    # 添加case方法一：执行case顺序根据与添加的顺序一致
    '''test_cases = [Test("test_Add5"),Test("test_Add2"),Test("test_Add3"),Test("test_Add4"),Test("test_Add1")]
    test_suite.addTests(test_cases)'''

    # 添加case方法二：单独一个一个添加
    '''test_suite.addTest(Test("test_Add5"))
    # test_suite.addTest(Test("test_Add4"))'''

    # 添加case方法三：loadTestsFromTestCase()，传入TestCase
    # test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test))

    # 添加case方法四
    test_suite.addTest(unittest.makeSuite(Test))

    # 生成Text格式测试报告
    '''with open('TextTestRunnerReport.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(test_suite)'''

    # 生成xml格式的测试报告
    '''# test_suite.addTest(unittest.makeSuite(Test))
    runner = xmlrunner.XMLTestRunner(output='report')  # 指定报告放的目录
    runner.run(test_suite)'''

    # 生成HTML格式的测试报告
    now = time.strftime(u'%Y%m%d%H%M')
    # test_suite.addTest(Test('test_Add1'))
    # test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test))
    report = ".\\report\\" + now + "HTMLreport.html"
    with open(report,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(f, verbosity=2, title='这是HTML格式测试报告', description='测试报告')
        runner.run(test_suite)

    # verbosity参数可以控制执行结果的输出，0 是简单报告、1 是一般报告、2 是详细报告
    # unittest.main(verbosity=2)
