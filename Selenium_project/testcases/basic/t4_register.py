from idlelib import browser


import pyautogui
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testcases import t1_locate_checkbox as t1
from time import sleep
import time

# Pil 在pillow里
from PIL import Image
from util import util


def check_registration():
    driver = webdriver.Chrome()
    driver = webdriver.Chrome()
    driver.get('http://localhost:8080/jpress-v3.2.0/user/register')
    driver.maximize_window()

    name = util.gen_random_str()
    email = name+'@qq.com'
    password = 'something'
    password2 = 'something'
    expected = '注册成功，点击确定进行登录。'
    verfi = util.get_code(driver, 'captchaimg')

    driver.find_element(By.NAME, 'username').send_keys(name)

    driver.find_element(By.NAME, 'email').send_keys(email)

    driver.find_element(By.NAME, 'pwd').send_keys(password)

    driver.find_element(By.NAME, 'confirmPwd').send_keys(password2)

    driver.find_element(By.NAME, 'captcha').send_keys(verfi)

    driver.find_element(By.XPATH, '/html/body/div/div/div/form/div[6]/div/button').click()
    sleep(3)
    WebDriverWait(driver,5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print(alert.text)
    print(expected)
    print(alert.text==expected)
    assert alert.text == expected
    alert.accept()
    driver.quit()
