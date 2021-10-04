import unittest
import testStr

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTest(TestStringMethods("test_split"))
suite.addTest(TestStringMethods("test_isupper"))
suite.addTest(MyTestCase("test_maybe_skipped"))
suite.addTest(MyTestCase("test_format"))

HtmlTestRunner.HTMLTestRunner(combine_reports=True, open_in_browser=True, descriptions=False,
                              report_title="Report").run(suite)