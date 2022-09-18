import os
import cv2
def nothing(emp):
    pass
def jindu(name,video):
    cv2.namedWindow(name,0)
    cv2.resizeWindow(name, 800, 600)
    cap = cv2.VideoCapture(video)
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    loop_flag = 0
    pos = 0
    cv2.createTrackbar('time', name, 0, frames, nothing)

    while 1:
        if loop_flag == pos:
            loop_flag = loop_flag + 1
            cv2.setTrackbarPos('time', name, loop_flag)
            print('loop_flag1', loop_flag)
        else:
            pos = cv2.getTrackbarPos('time', name)
            loop_flag = pos
            cap.set(cv2.CAP_PROP_POS_FRAMES, pos)
            print('loop_flag2', loop_flag)
        ret, img = cap.read()

        cv2.imshow(name, img)
        if cv2.waitKey(1) & 0xFF == ord('q'): #按q退出
            cv2.waitKey(0)

if __name__ == '__main__':
    video = r"D:Team-CVvideo_wang	est/1.MOV"
    name = video.split('.')[-1]
    jindu(name, video)