import cv2
import numpy as np

def video2images(Video_Dir):
    cap = cv2.VideoCapture(Video_Dir)
    c = 1  # 帧数起点
    index = 1  # 图片命名起点，如1.jpg
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    
    while True:
        # 逐帧捕获
        ret, frame = cap.read()
        # 如果正确读取帧，ret为True
        if not ret:
            print("Can't receive frame.")
            break
        # 设置每5帧取一次图片，若想逐帧抽取图片，可设置c % 1 == 0
        if c % 5 == 0:
            frame=frame[100:500,100:500,:]
            # 图片存放路径，即图片文件夹路径
            # cv2.imwrite('data/' + str(index) + '.jpg', frame) 
            cv2.imshow("123",frame)
            index += 1
        c += 1
        cv2.waitKey(1)
        # 按键停止
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
 
def playvideo(Video_Dir):
    cap = cv2.VideoCapture(Video_Dir)

    while(cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow('image', frame)
        k = cv2.waitKey(20)
        #q键退出
        if (k & 0xff == ord('q')):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    Video_Dir = "1.mkv"
    video2images(Video_Dir)
    # playvideo(Video_Dir)
