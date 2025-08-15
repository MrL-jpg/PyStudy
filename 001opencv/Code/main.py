import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

#生成随机灰度和BGR图像
# random_data = bytearray(os.urandom(120000))
# grayRandomImg = np.array(random_data).reshape(300,400)
# cv2.imwrite("Code/Source/grayRandomImg.png", grayRandomImg)
# colorRandomImg = np.array(random_data).reshape(100,400,3)
# cv2.imwrite("colorRandomImg.png",colorRandomImg)


# img = cv2.imread('Code\Source\dog.jpg')
# grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# imgByteArray = bytearray(img)
# grayImgByteAray = bytearray(grayImg)

# fixImg = np.array(imgByteArray) #将byte序列转换成一维数组
# fixGrayImg = np.array(grayImgByteAray)

# fixImg = fixImg.reshape(429,499,3)
# #fixGrayImg = fixGrayImg.reshape(429.499)

# cv2.imshow("FIXED_IMG",fixImg)
# #cv2.imshow("GRAY_FIXED_IMG", fixGrayImg)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #修改像素点的值

# img = cv2.imread('Code\Source\dog.jpg')
# print(img.item((100,100,0)))
# img[100,100,0] = 0;
# print(img.item((100,100,0)))

# #视频读取

# vc = cv2.VideoCapture("Code/Source/test.mp4")

# fps = vc.get(cv2.CAP_PROP_FPS)
# size = (int(vc.get(cv2.CAP_PROP_FRAME_WIDTH)),int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# fourcc = cv2.VideoWriter.fourcc(*'XVID')

# print(f"fps:{fps}\nsize:{size}")
# print(fourcc)

# success,frame = vc.read()
# print(f"read:{success}")
# videowrite = cv2.VideoWriter("testOutput.avi", fourcc, fps, size)

# while success is True and frame is not None:
#      videowrite.write(frame)
#      success,frame = vc.read()

# 摄像头读取并保存

# vc = cv2.VideoCapture(0)

# fps = int(vc.get(cv2.CAP_PROP_FPS))
# size = (int(vc.get(cv2.CAP_PROP_FRAME_WIDTH)),int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# forcc = cv2.VideoWriter.fourcc(*"mp4v")
# videowriter = cv2.VideoWriter("cap.mp4",forcc,fps,size)

# time = 10*fps-1

# while time > 0:
#     open,frame = vc.read()
#     if open is not True:
#         print(f"frame_data:{frame}\nread_error...")
#     videowriter.write(frame)
#     time -=1
# vc.release()
# cv2.destroyAllWindows()

# 鼠标事件

cliked = False

def mouse_event(event,x,y,flag, _):
    global cliked
    if event == cv2.EVENT_LBUTTONDOWN:
        cliked = True
        print(f"({x},{y})\nclick:{cliked}")
        
    
cv2.namedWindow("MyWindow")
cv2.setMouseCallback("MyWindow",mouse_event)

cv2.waitKey(0) 
