import cv2
import matplotlib.pyplot as plt
import numpy as np
input="./images/highway.jpg"

def get_edge(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(13,13),0)
    canny=cv2.Canny(blur,20,60)
    return canny
def get_roi(img):
    mask=np.zeros_like(edge) #全黑遮罩
    points=np.array([[[351,342],[399,292],[473,283],[671,376]]]) #建立多邊形座標
    cv2.fillPoly(mask,points,255) #(全黑遮罩,多邊形座標,繪製的像素值(255為全白))
    roi=cv2.bitwise_and(img,mask)#做and運算
    cv2.imshow('mask', mask)
    return roi
img=cv2.imread(input) #讀取圖片
edge=get_edge(img) #邊緣偵測
roi=get_roi(edge)
# cv2.imshow('edge',edge)

cv2.imshow('roi',roi)
cv2.waitKey(0)