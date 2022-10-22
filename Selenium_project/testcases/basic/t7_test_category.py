from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from util import util
class TestUserLogin(object):
    def __init__(self,login):
        self.login = login


    def test_add_category_error(self):
        username = ''
        # 前置条件，必须得有python
        parent = 'python'
        slug = 'test'
        expected = '分类名称不能为空'
        # 点击进入纹章分类
        self.login.driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        self.login.driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/ul/li[3]/a').click()
        sleep(1)


        self.login.driver.find_element(By.NAME, 'category.title').send_keys(username)
        # 选择父分类
        parent_category_elem = self.login.driver.find_element(By.NAME,'category.pid')
        Select(parent_category_elem).select_by_visible_text(parent)
        # 输入slug
        self.login.driver.find_element(By.NAME, 'category.slug').send_keys(slug)

        # 点击添加
        self.login.driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div/div[1]/div/form/div[2]/div/div/button').click()
        loc = (By.CLASS_NAME,'toast-message')
        WebDriverWait(self.login.driver,5).until(EC.visibility_of_element_located(loc))
        msg = self.login.driver.find_element(*loc).text
        assert msg == expected
