import mock
import unittest


class Test(unittest.TestCase):
    def add(self, a, b):
        return a+b


class TestMock(unittest.TestCase):

    def setUp(self):
        self.test = Test()

    def tearDown(self):
        pass

    def test_add(self):
        self.test.add = mock.Mock(return_value=3)
        self.assertEqual(self.test.add(4,2),3)


if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test))
    with open('TestReportMock.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(test_suite)
    # unittest.main(verbosity=2)




