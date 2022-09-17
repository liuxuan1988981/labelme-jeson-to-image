
import cv2
 
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
            # 图片存放路径，即图片文件夹路径
            cv2.imwrite('data/' + str(index) + '.jpg', frame) 
            index += 1
        c += 1
        cv2.waitKey(1)
        # 按键停止
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
 

if __name__ == "__main__":
    Video_Dir = "1.mkv"
    video2images(Video_Dir)
