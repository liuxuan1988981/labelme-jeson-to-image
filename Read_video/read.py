import cv2
import numpy as np
def nothing(emp):
    pass
def video2images(Video_Dir):
    cap = cv2.VideoCapture(Video_Dir)
    c = 1  # 帧数起点
    index = 1  # 图片命名起点，如1.jpg
    name="love lulu"
    # cv2.namedWindow(name,0)
    # cv2.resizeWindow(name, 1200, 1200)
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    loop_flag = 0
    pos = 0
    # cv2.createTrackbar('time', name, 0, frames, nothing)

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        
        # ret, image = cap.read()
        # 如果正确读取帧，ret为True
        # if not ret:
        #     print("Can't receive frame.")
        #     break
        # 设置每5帧取一次图片，若想逐帧抽取图片，可设置c % 1 == 0
        # if loop_flag == pos:
        #     loop_flag = loop_flag + 1
        #     cv2.setTrackbarPos('time', name, loop_flag)
        #     # print('loop_flag1', loop_flag)
        # else:
        #     pos = cv2.getTrackbarPos('time', name)
        #     loop_flag = pos
        #     cap.set(cv2.CAP_PROP_POS_FRAMES, pos)
        #     # print('loop_flag2', loop_flag)
        c = c + 100
        # if c % 3000==0:
        cap.set(cv2.CAP_PROP_POS_FRAMES, c)
        ret, image = cap.read()
        # lang ,wight
        image=image[200:700,500:1500,:]
        cv2.imwrite('9251/' + str(index) + '.jpg', image) 
        # cv2.imshow(name,image)
        index += 1
        cv2.waitKey(1)
        # if cv2.waitKey(1) == ord('r'):
        #     c = c + 10
        #     frame=cap.set(cv2.CAP_PROP_POS_FRAMES,c)
        #     ret, frame = cap.read()
        # 按键停止
        # if cv2.waitKey(1) == ord('p'):
        #     cv2.imwrite('data/' + str(index) + '.jpg', image)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
 

if __name__ == "__main__":
    Video_Dir = "9251.mp4"
    video2images(Video_Dir)

