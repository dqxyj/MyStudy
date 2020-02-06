# python3
# encoding:utf-8

# python3
# encoding:utf-8

import os
import time
import pyautogui
from utils import Utils
curr_path = os.path.dirname(os.path.realpath(__file__))
print(curr_path)
start_btn_imgpath = os.path.join(curr_path, 'test.png')
print(start_btn_imgpath)
btn_pos_x, btn_pos_y = pyautogui.locateCenterOnScreen(start_btn_imgpath, confidence=0.8)
clk_pos_x = btn_pos_x + Utils.gaussRandInt(0, 40, 80, allowMinus=True)
clk_pos_y = btn_pos_y + Utils.gaussRandInt(0, 40, 80, allowMinus=True)
pyautogui.moveTo(x=clk_pos_x, y=clk_pos_y, duration=Utils.gaussRand(0.8, 0.3), tween=pyautogui.easeInOutQuad)
time.sleep(Utils.gaussRand(0.8, 0.5))
pyautogui.click()
print("click")