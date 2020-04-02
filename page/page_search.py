from time import sleep
import page
from base.base_action import BaseAction

class PageSearch(BaseAction):
    # 输入搜素字
    def page_input(self,search_content):
        self.base_input(page.search_input,search_content)
    # 获取下拉选项搜索的结果
    def page_get_searchcontent(self):
        return self.base_find_elements(page.search_list)
    #首页搜索
    def page_search(self,search_content):
        #输入内容
        self.page_input(search_content)
        sleep(5)

