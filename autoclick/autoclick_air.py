from pickle import FALSE
import time
import pyautogui
import pydirectinput as direct
import cv2
import numpy as np
from PIL import ImageGrab
import keyboard as k
from win32 import win32gui
from win32 import win32api
from win32 import win32process
pyautogui.PAUSE = 0.5

def get_windows(window):
        wlist=['',' - Waiting for game',' - Loading',' - in battle',' - Test Sail']
        for state in wlist:
            windows = window + state
            handle = win32gui.FindWindow(None,windows)
            if handle == 0:
                continue
            else:
                break
        x1, y1, x2, y2 = win32gui.GetWindowRect(handle)
        return  x1, y1, x2, y2 , state

def get_son_windows(parent):
        hWnd_child_list = []
        win32gui.EnumChildWindows(parent, lambda hWnd, param: param.append(hWnd), hWnd_child_list)
        for i in hWnd_child_list:
            if win32gui.GetClassName(i) ==  'DagorWClass':
                break 
        return i


class click():
    # def __init__(self) -> None:

    def auto_Click(self,var_avg):
        # print(var_avg)
        # pyautogui.moveTo(var_avg[0], var_avg[1])
        pyautogui.click(var_avg[0], var_avg[1], button='left')
        # time.sleep(0.5)
        pyautogui.mouseDown(button='left')
        # time.sleep(0.5)
        pyautogui.mouseUp(button='left')

    def get_xy(self,img_model_path,img):
        img_terminal = cv2.imread(img_model_path)
        # 读取模板的高度宽度和通道数
        height, width, channel = img_terminal.shape
        # 使用matchTemplate进行模板匹配（标准平方差匹配）
        result = cv2.matchTemplate(img, img_terminal, cv2.TM_SQDIFF_NORMED)
        # 解析出匹配区域的左上角图标
        check=cv2.minMaxLoc(result)
        print(check)
        if check[0]<0.1:
            upper_left = check[2]
            # 计算出匹配区域右下角图标（左上角坐标加上模板的长宽即可得到）
            lower_right = (upper_left[0] + width, upper_left[1] + height)
            # 计算坐标的平均值并将其返回
            avg = (int((upper_left[0] + lower_right[0]) / 2), int((upper_left[1] + lower_right[1]) / 2))
        else:
            avg = 0
        return avg

    def check_status(self,img_model_path,name,img):
        img_terminal = cv2.imread(img_model_path)
        # 读取模板的高度宽度和通道数
        # height, width, channel = img_terminal.shape
        # 使用matchTemplate进行模板匹配（标准平方差匹配）
        result = cv2.matchTemplate(img, img_terminal, cv2.TM_SQDIFF_NORMED)
        check=cv2.minMaxLoc(result)
        if check[0]<0.1:
            status = True
            print(f"status---{name}")
        else:
            status = False
        return status    

    def routine(self,img_model_path,name,img):
        avg = self.get_xy(img_model_path,img)
        if avg == 0:
          print(f"Not have---{name}")
        else:
            print(f"clicking---{name}")
            self.auto_Click(avg)

    def routine_direx(self,img_model_path,name,img):
        avg = self.get_xy(img_model_path,img)
        if avg == 0:
          print(f"Not have---{name}")
        else:
            print(f"clicking---{name}")
            
            direct.moveTo(avg[0], avg[1]+10)
            time.sleep(0.5)
            pyautogui.mouseDown(button='left')
            time.sleep(0.5)
            pyautogui.mouseUp(button='left')
            # time.sleep(0.5)

# 'War Thunder' 'War Thunder Client'DagorWClass
    def main_gui(self):
        index=0
        while  True:
            if k.is_pressed('esc'):
              break
            x1, y1, x2, y2 ,state= get_windows('War Thunder')
            print(x1, y1, x2, y2)
            print(state)
            im = ImageGrab.grab(bbox =(x1, y1, x2, y2))
            img = cv2.cvtColor(np.array(im), cv2.COLOR_BGR2RGB)  

            if state =='' or ' - Waiting for game' or index==0:
                play=self.check_status("./war/to_battle.png","to_battle",img)
                if play == True:
                    self.routine("./war/to_battle.png", "to_battle",img)
                    time.sleep(5)
                else :
                    # k.press('enter')
                    # time.sleep(0.5)
                    # k.release('enter')
                    time.sleep(5)
            if state ==  '- Loading':
                index = 0
                time.sleep(3)

            # ingame=self.check_status("./war/ingame.png","ingame",img)
            if state == ' - in battle':
                time.sleep(1)
                if index == 0:
                    select=self.check_status("./war/select.png","select",img)
                    if select == True:  
                        k.press('enter')
                        time.sleep(1)
                        k.release('enter') 
                        index = 2
                        time.sleep(13)
                        k.press('s')
                        time.sleep(0.8)
                        k.release('s')                    
                
                return_hanger=self.check_status("./war/return_to_hanger.png","return_to_hanger",img)
                if return_hanger == True:
                    self.routine_direx("./war/return_to_hanger.png", "return_to_hanger",img)
                print(index)
                # ingame=self.check_status("./war/air_in_game.png","ingame",img)

                # if ingame == True:
                #     time.sleep(0.5)
                #     k.press('shift')
                #     time.sleep(3)
                #     k.release('shift')
                #     time.sleep(1)
                #     index = 2

                    # if index == 2:
                    #     print(" second  index == 2")
                    #     time.sleep(0.5)
                    #     direct.press('l')
                    #     time.sleep(0.5)
                    #     k.press('s')
                    #     time.sleep(3)
                    #     k.release('s')   
                    # else:  
                    #     print("=== first in ingame")
                    #     time.sleep(0.5)
                    #     k.press('a')
                    #     k.press('shift')
                    #     time.sleep(0.5)
                    #     k.release('a')
                    #     k.release('shift')
                    #     time.sleep(0.5)
                    #     time.sleep(10)
                    #     index = 2
                    
                    

            if state ==''and index ==2:

                direct.moveTo(x1+100, y1+100)
                time.sleep(1)

                complish=self.check_status("./war/quite_game.png","complish",img)
                if complish == True:     
                    k.press('enter')
                    time.sleep(1)
                    k.release('enter')
                    index == 0

                    
                # pyautogui.mouseDown(button='left')
                # pyautogui.mouseUp(button='left')
                
            # time.sleep(2)
def avg(x1, y1, x2, y2):
        x = int((x1 + x2) / 2)
        y = int((y1 + y2) / 2)
        return x ,y
        
def test():
    index=0
    n=0
    while  True:
        if k.is_pressed('esc'):
            break
        x1, y1, x2, y2 ,state= get_windows('War Thunder') 
        print(state)
        # time.sleep(0.5)
        x,y=avg(x1, y1, x2, y2)
        # pyautogui.mouseDown(button='left')
        # pyautogui.mouseUp(button='left')
        # pyautogui.click(x+20, y, button='right')
        if index == 0:
            # ditect.moveTo(x,y+50)
            index =1
        time.sleep(0.5)
        if index == 1:
            direct.move(5,None)
            n=n+1
            if n%5==0:
               index =0 
               direct.press('c')
        time.sleep(1)
        

    pass         
def test_key_mouse():
    ck=click()
    while  True:
        # x1, y1, x2, y2 ,state= get_windows('War Thunder') 
        # print(state)
        # # time.sleep(0.5)
        # x,y=avg(x1, y1, x2, y2)
        im = ImageGrab.grab()
        img = cv2.cvtColor(np.array(im), cv2.COLOR_BGR2RGB)
        # cv2.imshow('xxx',img)
        # cv2.waitKey(0)
        ck.routine("./war/play.png", "play",img)
        # pyautogui.click(50, 50, button='left')
        time.sleep(2)

        # k.press('b')
        # time.sleep(0.5)
        # k.release('b')

        # pyautogui.mouseDown(button='left')
        # pyautogui.mouseUp(button='left')
        # pyautogui.click(x+20, y, button='right')
        # pyautogui.moveTo(x+100, y+100)
        time.sleep(2)
        if k.is_pressed('esc'):
            break

    pass         


def main_run():
    ck=click()
    ck.main_gui()

if __name__ == "__main__":  
    ck=click()
    ck.main_gui()
    # test()
    # # test_key_mouse()
   

