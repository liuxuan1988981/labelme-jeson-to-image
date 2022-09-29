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

    def get_xy(self,img_model_path):
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
        
        
        # while True:  # 开始录制
        im = ImageGrab.grab()
        img = cv2.cvtColor(np.array(im), cv2.COLOR_BGR2RGB)
        
        # cv2.imshow('WindowName', im_cv)
        # if cv2.waitKey(1) == ord('q'):
        #     break
        # time.sleep(2)
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

    def check_status(self,img_model_path):
        img = pyautogui.screenshot()
        img_terminal = cv2.imread(img_model_path)
        # 读取模板的高度宽度和通道数
        height, width, channel = img_terminal.shape
        # 使用matchTemplate进行模板匹配（标准平方差匹配）
        result = cv2.matchTemplate(img, img_terminal, cv2.TM_SQDIFF_NORMED)
        status=None
        if result!=None:
            status=True
        return status

    def auto_Click(self,var_avg):
        """
        输入一个元组，自动点击
        :param var_avg: 坐标元组
        :return: None
        """
        pyautogui.click(var_avg[0], var_avg[1], button='left')
        time.sleep(1)


    def routine(self,img_model_path, name):
        avg = self.get_xy(img_model_path)
        print(f"clicking---{name}")
        self.auto_Click(avg)


    def click_part1(self):
        self.routine("./war/play.png", "play")
      


    def click_part2(self,times):
        
        for i in range(times):
            time.sleep(1)
            # 点击1-7 注意要先让模拟器记忆1-7
            self.routine("./pic/1-7.png", "1-7")
            # 点击代理指挥
            self.routine("./pic/PRTS.png", '代理指挥')
            # 点击开始行动
            self.routine("./pic/start-1.png", '开始行动')
            # 点击作战页的开始行动
            self.routine("./pic/start-2.png", "作战页的开始行动")
            # 等待行动结束
            time.sleep(90)
            # 点击结算页面退出
            self.routine("./pic/operation_over.png", '结算页面的行动结束')
            # 因为黑屏比较长，设置较长时间的睡眠
            time.sleep(3)



if __name__ == "__main__":
    ck=click()
    ck.click_part1()
   

