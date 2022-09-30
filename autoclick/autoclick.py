import time
import pyautogui
import cv2
import numpy as np
from PIL import ImageGrab

class click():
    def __init__(self) -> None:
        self.excel_receive_send = "excel/GW_receive_send.xlsx"   
        self.excel_big_date = "excel/big_date.xlsx"
        self.excel_DTC = "excel/DTC.xlsx"
        self.dict_big_date = {}
        self.dict_rs_date = {}    # ON recieve
        self.dict_ac_date = {}    # ACC/OFF recieve
        self.dict_dg_date = {}    # DAIG recieve
        self.dict_dtc_date = {}
        self.flag_can = 3
        
        pass

    def get_xy(self,img_model_path,img):
        """
        用来判定游戏画面的点击坐标
        :param img_model_path:用来检测的图片
        :return:以元组形式返回检测到的区域中心的坐标
        """
        # # 将图片截图并且保存
        # pyautogui.screenshot().save("./war/screenshot.png")
        # img = cv2.imread("./war/screenshot.png")
        
        ##############
        # cap = cv2.VideoCapture(0)
        # while(cap.isOpened()):
        #     ret,frame = cap.read()
        #     cv2.imshow('WindowName', frame)
        # img = frame
        # img_terminal = cv2.imread(img_model_path)
        # # 读取模板的高度宽度和通道数
        # height, width, channel = img_terminal.shape
        # # 使用matchTemplate进行模板匹配（标准平方差匹配）
        # result = cv2.matchTemplate(img, img_terminal, cv2.TM_SQDIFF_NORMED)
        # # 解析出匹配区域的左上角图标
        # upper_left = cv2.minMaxLoc(result)[2]
        # # 计算出匹配区域右下角图标（左上角坐标加上模板的长宽即可得到）
        # lower_right = (upper_left[0] + width, upper_left[1] + height)
        # # 计算坐标的平均值并将其返回
        # avg = (int((upper_left[0] + lower_right[0]) / 2), int((upper_left[1] + lower_right[1]) / 2))
        # return avg
        ##################################################################################################
        # while True:  # 开始录制
        # im = ImageGrab.grab()
        # img = cv2.cvtColor(np.array(im), cv2.COLOR_BGR2RGB)

        img_terminal = cv2.imread(img_model_path)
        # 读取模板的高度宽度和通道数
        height, width, channel = img_terminal.shape
        # 使用matchTemplate进行模板匹配（标准平方差匹配）
        result = cv2.matchTemplate(img, img_terminal, cv2.TM_SQDIFF_NORMED)
        # 解析出匹配区域的左上角图标
        upper_left = cv2.minMaxLoc(result)[2]
        # 计算出匹配区域右下角图标（左上角坐标加上模板的长宽即可得到）
        lower_right = (upper_left[0] + width, upper_left[1] + height)
        # 计算坐标的平均值并将其返回
        avg = (int((upper_left[0] + lower_right[0]) / 2), int((upper_left[1] + lower_right[1]) / 2))
        return avg

    def check_status(self,img_model_path,img):
        img_terminal = cv2.imread(img_model_path)
        # 读取模板的高度宽度和通道数
        height, width, channel = img_terminal.shape
        # 使用matchTemplate进行模板匹配（标准平方差匹配）
        result = cv2.matchTemplate(img, img_terminal, cv2.TM_SQDIFF_NORMED)
        status=None
        if len(result)!=0:
            status=True
        return status

    def auto_Click(self,var_avg):
        pyautogui.click(var_avg[0], var_avg[1], button='left')
        


    def routine(self,img_model_path,name,img):
        avg = self.get_xy(img_model_path,img)
        print(f"clicking---{name}")
        self.auto_Click(avg)


    def click_part1(self):
        
        while  True:
            im = ImageGrab.grab()
            img = cv2.cvtColor(np.array(im), cv2.COLOR_BGR2RGB)
            self.routine("./war/to_battle.png", "to_battle",img)
            time.sleep(2)
      
            


if __name__ == "__main__":
    ck=click()
    ck.click_part1()
   

