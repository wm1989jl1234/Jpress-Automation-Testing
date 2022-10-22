from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from util import util


class TestUserLogin(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress-v3.2.0/admin/login')
        self.driver.maximize_window()

    def test_admin_login_code_error(self):
        username = 'admin'
        password = '123456'
        captcha = '666'
        expected = '验证码不正确，请重新输入'
        self.driver.find_element(By.NAME, 'user').send_keys(username)
        self.driver.find_element(By.NAME, 'pwd').send_keys(password)
        self.driver.find_element(By.NAME, 'captcha').send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        assert alert.text == expected
        alert.accept()

    def test_admin_login_code_ok(self):
        username = 'admin'
        password = '123456'
        captcha = util.get_code(self.driver,self.driver.find_element(By.XPATH, '//*[@id="form"]/div[3]/img'))
        expected = 'JPress后台'
        self.driver.find_element(By.NAME, 'user').send_keys(username)
        self.driver.find_element(By.NAME, 'pwd').send_keys(password)
        self.driver.find_element(By.NAME, 'captcha').send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()
        sleep(2)

        WebDriverWait(self.driver, 5).until(EC.title_is(expected))

        assert self.driver.title== expected

