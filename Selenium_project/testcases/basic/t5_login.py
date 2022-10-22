from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
class TestUserLogin(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress-v3.2.0/user/login')
        self.driver.maximize_window()

    def test_user_login_username_error(self):
        username = ''
        password = '123456'
        expected = '账号不能为空'
        self.driver.find_element(By.NAME,'user').send_keys(username)
        self.driver.find_element(By.NAME, 'pwd').send_keys(password)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()

        WebDriverWait(self.driver,5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        assert alert.text == expected
        alert.accept()
        # self.driver.quit()

    def test_user_login_ok(self):
        username = 'admin'
        password = '123456'
        expected = '用户中心'
        self.driver.find_element(By.NAME, 'user').clear()
        self.driver.find_element(By.NAME, 'user').send_keys(username)
        self.driver.find_element(By.NAME, 'pwd').clear()
        self.driver.find_element(By.NAME, 'pwd').send_keys(password)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()

        WebDriverWait(self.driver, 5).until(EC.title_is(expected))
        sleep(3)
        assert self.driver.title == expected


        self.driver.quit()

