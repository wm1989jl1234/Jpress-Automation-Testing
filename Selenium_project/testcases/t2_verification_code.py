from idlelib import browser

import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time

# Pil 在pillow里
from PIL import Image
# 找坐标，选位置。通过屏幕坐标确定位置
import pyautogui


def cropImg():
    # 实现方法是保存截图，然后抠出来验证码，再用tesseract解析字符
    driver = webdriver.Chrome()
    driver.get('http://localhost:8080/jpress-v3.2.0/user/register')
    driver.maximize_window()
    pic = driver.find_element(By.ID, 'captchaimg')
    t = time.time()
    # 保存图片
    picture_name1 = str(t) + '.png'
    driver.save_screenshot(picture_name1)

    # 找到左顶点之后用图片的宽度和高找到右底点
    left = pic.location['x']
    top = pic.location['y']
    right = pic.size['width'] + left
    height = pic.size['height'] + top

    im = Image.open(picture_name1)
    # 剪裁，crop((左顶X,左顶Y，宽度，高度))
    img = im.crop((left, top, right, height))

    t = time.time()
    # 保存图片
    picture_name2 = str(t) + '.png'

    img.save(picture_name2)

    driver.quit()

def checkImg():
    image1 = Image.open('C:\\Users\\yimin\\Desktop\\1_pyyisAG7o8p4w4son8IHNQ.png.jpeg')
    str = pytesseract.image_to_string(image1)
    print(str)
