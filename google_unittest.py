import unittest
from selenium import webdriver
import time
class MyTestCase(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path='C:\drivers\chromedriver.exe')

    def test_googletest(self):
        driver = self.driver
        driver.get("https://www.youtube.com/")
        driver.find_element_by_name('search_query').send_keys("wataniya")
        driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon').click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
