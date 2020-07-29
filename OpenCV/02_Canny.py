import cv2
input="./images/國道.jpg"

def get_edge(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(13,13),0)
    canny=cv2.Canny(blur,30,70) #(輸入影像,最低門檻值,最高門檻值)
    #象素值梯度變化低於門檻值輸出0，象素值梯度變化高於門檻值輸出225代表邊緣，若介於之間則以此像素周邊鄰居是否為邊緣來判定。
    #像素值定義:某一小區塊平均亮度
    #圖片分成點陣圖(jpg、png、跟向量圖
    return canny
def get_edge2(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(13,13),0)
    canny=cv2.Canny(blur,70,70) #(輸入影像,最低門檻值,最高門檻值)
    #象素值梯度變化低於門檻值輸出0，象素值梯度變化高於門檻值輸出225代表邊緣
    #像素值定義:某一小區塊平均亮度
    #圖片分成點陣圖(jpg、png、跟向量圖
    return canny
img=cv2.imread(input) #讀取圖片
edge=get_edge(img)
edge2=get_edge2(img)
cv2.imshow('EDGE',edge)
cv2.imshow('EDGE2',edge2)
cv2.waitKey(0)