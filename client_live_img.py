"""
rolo : client
Level : Fun
Dec : 
Created at : 2016.11.29
Modified on : 2017.03.01
Author : Iflier
"""

import socket
import cv2
import numpy as np


address = ("localhost", 7000)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(address)

capture = cv2.VideoCapture(0)

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

while capture.isOpened():
    ret,frame = capture.read()
    result,imgencode = cv2.imencode(".jpg", frame, encode_param)
    data = np.array(imgencode)
    stringData = data.tostring()
    sock.send(bytes(str(len(stringData)).rjust(16), encoding='utf-8'))    
    sock.send(stringData)    
    decimg = cv2.imdecode(data, 1)
    """cv2.imshow("Client", decimg)
    if cv2.waitKey(1)&0xff == 27:
        break"""
sock.close()
capture.close()
#cv2.destroyAllWindows()
