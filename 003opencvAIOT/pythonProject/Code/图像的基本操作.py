import cv2
import matplotlib.pyplot as plt
import numpy as np

# 视频读取

# filepath = "./Source/test.mp4"
# vc = cv2.VideoCapture(filepath)
# if vc.isOpened() :
#     open, frame = vc.read()
# else :
#     exit()
# while open :
#     open, frame = vc.read()
#     if frame is None :
#         break
#     if open :
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #转化成灰度图
#         cv2.imshow("test_video",frame)
#         cv2.waitKey(0)
# cv2.waitKey(1000)
# vc.release()
# cv2.destroyAllWindows()

# ROI rejest of interesting

# filepath = "./Source/lena.jpg"
# img = cv2.imread(filepath)
# cut = img[100:150, 100:150]
# b,g,r = cv2.split(img)
# # cv2.imshow('cut', cut)
# # cv2.imshow("b",b)
# # cv2.imshow("g",g)
# # cv2.imshow("r",r)
# img[:,:,0] = 0
# img[:,:,1] = 0
# cv2.imshow("r",img)
# cv2.waitKey(0)
#
# # 图像融合
#
# cat = cv2.imread("./Source/cat.jpg")
# dog = cv2.imread("./Source/dog.jpg")
#
# print(cat.shape)
# print(dog.shape)
# cat = cv2.resize(cat,(500,500))
# dog = cv2.resize(dog,(500,500))
# print(cat.shape)
# print(dog.shape)
#
# res = cv2.addWeighted(cat,0.5,dog,0.5,0)
# cv2.imshow('res',res)
#
# res = cv2.resize(res,(0,0),fx = 1.5,fy = 1.5)
# cv2.imshow("res2",res)
# cv2.waitKey(0)

# 二值化处理

# 1>图片二值化
# img = cv2.imread("./Source/cat.jpg", cv2.IMREAD_GRAYSCALE)
# cv2.imshow("原始灰度图",img)
# retval, ret = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow("二值化处理", ret)
# print(retval)
# cv2.waitKey(0)

# 2>视频二值化处理

vc = cv2.VideoCapture("./Source/test.mp4")

if not vc.isOpened() :
    exit()
while True:
    ret, frame = vc.read()
    if frame is None or ret == False:
        print("read filished")
        exit()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame,(0,0), fx=0.5, fy=0.5)
    retval, res = cv2.threshold(frame, 127, 255, cv2.THRESH_TRUNC)
    cv2.imshow("frame", res)
    cv2.waitKey(10)

