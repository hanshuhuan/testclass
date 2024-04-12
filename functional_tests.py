from email import header
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.by import By

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
        # 现在有一个在线待办事项的应用
        # 进入应用的首页
        self.browser.get('http://localhost:8000')

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
        time.sleep(1) #(4)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn('1: Buy flowers', [row.text for row in rows])
        # 页面有一个文本输入框，可以输入另一个待办事项
        # 输入“give to girlfriend”
        self.fail('Finish the test!')
        # 页面再次更新，显示了两个待办事项

        # 现在想知道这个网站是否会记住这两个待办事项
        # 看到网站为用户生成了一个唯一的URL

        # 访问这个URL，发现待办事项列表还在
        # 满意的去睡觉了

if __name__ == '__main__':
    unittest.main()