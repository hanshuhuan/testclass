from email import header
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

Max_Wait=10

class NewVisitorTest(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        try:
            table = self.browser.find_element(By.ID, 'id_list_table')
            rows = table.find_elements(By.TAG_NAME, 'tr')
            self.assertIn(row_text, [row.text for row in rows])
            return 
        except(AssertionError,WebDriverException) as e:
            if time.time() - start_time > Max_Wait:
                raise e
            time.sleep(0.5)
    def test_can_start_a_list_and_retrieve_it_later(self):
        # 现在有一个在线待办事项的应用
        # 进入应用的首页
        self.browser.get(self.live_server_url)

        # 网页里包含'To-Do'这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # 应用有一个输入待办事项的文本输入框
        inputbox = self.browser.find_element(By.ID, 'id_new_item') #(1)
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # 输入一个待办事项“buy flowers”
        inputbox.send_keys('Buy flowers') #(2)
        # 按回车键后，页面更新了
        # 待办事项列表里显示了“1: buy flowers”
        inputbox.send_keys(Keys.ENTER) #(3)
        self.wait_for_row_in_list_table('1: Buy flowers')
        # 页面有一个文本输入框，可以输入另一个待办事项
        # 输入“give a gift to lyb"
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Give a gift to lyb')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        # 页面再次更新，显示了两个待办事项
        self.wait_for_row_in_list_table('1: Buy flowers')
        self.wait_for_row_in_list_table('2: Give a gift to lyb')
        # 意满离
    def test_multiple_users_can_start_lists_at_different_urls(self):
        # 张三现在有一个新的待办事项应用
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy flowers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy flowers')
        # 他注意到网站为他生成了一个唯一的URL
        zhangsan_list_url = self.browser.current_url
        self.assertRegex(zhangsan_list_url, '/web/.+')
        # 现在有一个叫李四的新用户访问了网站
        # 我们使用一个新的浏览器会话
        self.browser.quit()
        self.browser = webdriver.Firefox()
        # 李四访问首页，看不到张三的待办事项
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy flowers', page_text)
        self.assertNotIn('Give a gift to lyb', page_text)
        # 李四输入一个新的待办事项，新建一个清单
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        # 李四获得了他的唯一URL
        lisi_list_url = self.browser.current_url
        self.assertRegex(lisi_list_url, '/web/.+')
        self.assertNotEqual(lisi_list_url, zhangsan_list_url)
        # 这个页面还是没有张三的清单
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy flowers', page_text)
        self.assertIn('Buy milk', page_text)
        # 意满离