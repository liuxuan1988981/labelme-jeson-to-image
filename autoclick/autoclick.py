from pickle import FALSE
import time
import pyautogui
import cv2
import numpy as np
from PIL import ImageGrab
import keyboard as k


pyautogui.PAUSE = 0.5
class click():
    def __init__(self) -> None:
        self.dict_dtc_date = {}
        self.flag_can = 3
        pass
    
    def auto_Click(self,var_avg):
        pyautogui.click(var_avg[0], var_avg[1], button='left')
        pyautogui.mouseDown(button='left')
        pyautogui.mouseUp(button='left')


    def get_xy(self,img_model_path,img):
        img_terminal = cv2.imread(img_model_path)
        # 读取模板的高度宽度和通道数
        height, width, channel = img_terminal.shape
        # 使用matchTemplate进行模板匹配（标准平方差匹配）
        result = cv2.matchTemplate(img, img_terminal, cv2.TM_SQDIFF_NORMED)
        # 解析出匹配区域的左上角图标
        check=cv2.minMaxLoc(result)
        if check[0]<0.1:
            upper_left = check[2]
            # 计算出匹配区域右下角图标（左上角坐标加上模板的长宽即可得到）
            lower_right = (upper_left[0] + width, upper_left[1] + height)
            # 计算坐标的平均值并将其返回
            avg = (int((upper_left[0] + lower_right[0]) / 2), int((upper_left[1] + lower_right[1]) / 2))
        else:
            avg =0
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


    def main_gui(self):
        while  True:
            im = ImageGrab.grab()
            img = cv2.cvtColor(np.array(im), cv2.COLOR_BGR2RGB)
            self.routine("./war/to_battle.png", "to_battle",img)
            time.sleep(5)
            select=self.check_status("./war/select.png","select",img)
            if select == True:
                k.press('enter')
                time.sleep(0.5)
                k.release('enter')
                time.sleep(4)  
            ingame=self.check_status("./war/ingame.png","ingame",img)
            if ingame == True:
                k.press('b')
                time.sleep(0.5)
                k.release('b')
                pyautogui.mouseDown(button='left')
                pyautogui.mouseUp(button='left')
                # break
            time.sleep(2)
               

if __name__ == "__main__":
    
    ck=click()
    ck.main_gui()
   

