import cv2
import numpy as np
from onvif import ONVIFCamera
import asyncio
import os


def setup_camera(ip, port, user, passwd):
    camera = ONVIFCamera(ip, port, user, passwd)
    media = camera.create_media_service()
    profiles = media.GetProfiles()
    return profiles[0].token  # 返回首个配置文件的Token

def move_ptz(ip, port, user, passwd, x, y):
    camera = ONVIFCamera(ip, port, user, passwd)
    ptz = camera.create_ptz_service()
    profile_token = setup_camera(ip, port, user, passwd)
    
    # 持续移动指令
    ptz.ContinuousMove({
        'ProfileToken': profile_token,
        'Velocity': {'PanTilt': {'x': x, 'y': y}}  # x:水平方向, y:垂直方向
    })
    asyncio.sleep(0.5)  # 移动持续时间
    ptz.Stop({'ProfileToken': profile_token})  # 停止移动
move_ptz("192.168.1.34",80, "admin", "418LYZ20now", x=1, y=0.5)

def connect_camera(ip, username='admin', password='', port=554, stream='stream1'):
    # 构造RTSP地址
    rtsp_url = f"rtsp://{username}:{password}@{ip}:{port}/{stream}"
    cap = cv2.VideoCapture(rtsp_url)
    return cap

cap = connect_camera('192.168.1.34','admin','418LYZ20now',554,'stream2')
open,frame = cap.read()
s = 1
while open :
    open,frame = cap.read()
    frame = cv2.resize(frame,(0,0),fx=s,fy=s)
    cv2.imshow("STREAM",frame)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
    elif key == ord('a'):
        s += 0.1
    elif key == ord('d'):
        s -= 0.1
cap.release()
cv2.destroyAllWindows()

