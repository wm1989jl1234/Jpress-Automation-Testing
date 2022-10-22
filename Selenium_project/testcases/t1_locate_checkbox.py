from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 找坐标，选位置。通过屏幕坐标确定位置
import pyautogui


def test2():
    driver = webdriver.Chrome()
    driver.get('http://www.jpress.cn/user/register')
    driver.maximize_window()
    sleep(2)
    elem = driver.find_element(By.ID, 'agree')
    rect = elem.rect
    # 如果无法自动化选中，就用autogui给出坐标
    pyautogui.click(rect['x']+10,rect['y']+130)

    sleep(5)
    driver.quit()
