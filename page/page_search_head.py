import page
from base.base_action import BaseAction

class PageSearchHead(BaseAction):
    #点击头部搜索按钮
    def page_click_headsearch(self):
        self.base_click(page.search_head_link)
    # 输入搜素字
    def page_input(self, search_content):
        self.base_input(page.search_head_input, search_content)
    #获取搜索结果
    def page_get_searchcontent(self):
        return self.base_find_elements(page.search_list)
    #头部搜索
    def page_head_search(self,content):
        self.page_click_headsearch()
        self.page_input(content)

