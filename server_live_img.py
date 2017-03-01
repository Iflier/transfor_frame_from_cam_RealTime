"""
rolo : server
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
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(True)
conn, addr = s.accept()


def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf:
            return None
        buf += newbuf
        count -= len(newbuf)
    return buf

while True:
    length = recvall(conn, 16)
    stringData = recvall(conn, int(length))
    data = np.fromstring(stringData, dtype = np.uint8)
    decimg = cv2.imdecode(data, 1)
    cv2.imshow('Sever', decimg)
    if cv2.waitKey(10) == 27:
        break
s.close()
cv2.destroyAllWindows()
