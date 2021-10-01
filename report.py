import unittest

import google_unittest
import wiki_unittest

import os
direct = os.getcwd()

class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests(
            unittest.defaultTestLoader.loadTestsFromTestCase(wiki_unittest.MyWikiTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(google_unittest.MyTestCase)
        )


if __name__ == '__main__':
    unittest.main()
