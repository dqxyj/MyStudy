# python3
# encoding:utf-8

import os
import time
import pyautogui
from utils import Utils

curr_path = os.path.dirname(os.path.realpath(__file__))
enter_game = os.path.join(curr_path,'RiChang.png')
icon = os.path.join(curr_path,'RiChang_next.png')
battle = os.path.join(curr_path,'Battle.png')
task = os.path.join(curr_path,'RiChang_next2.png')
time.sleep(2)
def autoplay():
   count = 0
   while True:
      print("Begin to autoplay!")
      print("Now count :", count)
      pyautogui.click(1500,530)
      while True:
          pos = pyautogui.locateCenterOnScreen(task, confidence=0.8)
          if pos is None:
              print("No")
              continue
          else:
              print("Get")
              pyautogui.moveTo(pos[0],pos[1])
              pyautogui.click()
              break
      time.sleep(5)
      count += 1
      if count > 50 :
          print("End.....")
          break

#time.sleep(5)
isRunning = True
btn_pos_x, btn_pos_y = pyautogui.locateCenterOnScreen(enter_game, confidence=0.8)
clk_pos_x = btn_pos_x + Utils.gaussRandInt(0, 40, 80, allowMinus=True)
clk_pos_y = btn_pos_y + Utils.gaussRandInt(0, 40, 80, allowMinus=True)
pyautogui.moveTo(x=clk_pos_x, y=clk_pos_y, duration=Utils.gaussRand(0.8, 0.3), tween=pyautogui.easeInOutQuad)
time.sleep(Utils.gaussRand(0.8, 0.5))
pyautogui.click()
try:
    pos = pyautogui.locateCenterOnScreen(enter_game, confidence=0.6)
    print("Gei RiChang is", pos)
    pyautogui.moveTo(pos[0],pos[1])
    pyautogui.click(pos[0],pos[1])
    time.sleep(4)
    pos = pyautogui.locateCenterOnScreen(icon, confidence=0.6)
    pyautogui.moveTo(pos[0],pos[1],duration=0.25)
    pyautogui.click(pos[0],pos[1])
except:
    pos = pyautogui.locateCenterOnScreen(enter_game, confidence=0.6)
    print("Gei RiChang is", pos)
    pyautogui.moveTo(836,829)
    pyautogui.click(836,829)
    time.sleep(4)
    pos = pyautogui.locateCenterOnScreen(icon, confidence=0.6)
    pyautogui.moveTo(pos[0],pos[1],duration=0.25)
    pyautogui.click(pos[0],pos[1])
time.sleep(4)
pos = pyautogui.locateCenterOnScreen(battle, confidence=0.6)
if pos is None:
    autoplay()
else :
    pyautogui.moveTo(pos[0],pos[1])
    pyautogui.click()
    time.sleep(4)
    autoplay()
