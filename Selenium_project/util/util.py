import pickle
import random
import string
import time
from PIL import Image
import os
import json
import requests
from testcases import t3_AI_verification as ai

from selenium.webdriver.common.by import By

TOKEN = 'free'  # token 获取：http://www.bhshare.cn/imgcode/gettoken
URL = 'http://www.bhshare.cn/imgcode/'  # 接口地址


def get_code(driver, pic):
    t = time.time()
    path = os.path.dirname(os.path.dirname(__file__)) + '\\screenshots'
    picture_name1 = path + '\\' + str(t) + '.png'
    driver.save_screenshot(picture_name1)
    left = pic.location['x']
    top = pic.location['y']
    right = pic.size['width'] + left
    height = pic.size['height'] + top
    im = Image.open(picture_name1)
    img = im.crop((left, top, right, height))

    t = time.time()
    picture_name2 = path + '\\' + str(t) + '.png'
    img.save(picture_name2)
    return ai.imgcode_local(picture_name2)



def gen_random_str():
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return rand_str


def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        cookies = driver.get_cookies()
        print(cookies)
        pickle.dump((cookies, filehandler))


def load_cookies(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)
