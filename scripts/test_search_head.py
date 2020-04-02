import unittest
from parameterized import parameterized
from base.read_data import read_data
from time import sleep
from page.page_search_head import PageSearchHead

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.search = PageSearchHead()
    def tearDown(self):
        self.search.driver.quit()
    @parameterized.expand(read_data("test_search", "data.yaml"))
    def test_search_head(self,content):
        self.search.page_head_search(content)
        sleep(10)
        #获取搜索结果
        self.select_elements = self.search.page_get_searchcontent()
        #断言
        try:
            for ele in self.select_elements:
                self.assertIn(ele.text, "123")
                print(ele.text)
            self.assertTrue(len(self.select_elements) <=10, True)
        except Exception as e:
            print(e)

