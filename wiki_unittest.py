import unittest
from selenium import webdriver
import time
class MyWikiTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path='C:\drivers\chromedriver.exe')

    def test_googletest(self):
        driver = self.driver
        driver.get("https://www.wikipedia.org/")
        driver.find_element_by_name('search').send_keys("wataniya")
        driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i').click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()