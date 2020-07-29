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
    points = np.array([[[351, 342], [399, 292], [473, 283],[671, 376]]]) #建立多邊形座標
    cv2.fillPoly(mask,points,255) #(全黑遮罩,多邊形座標,繪製的像素值(255為全白))
    roi=cv2.bitwise_and(img,mask)#做and運算
    # cv2.imshow('mask', mask)
    return roi
def draw_lines(img,lines):
    for line in lines:
        points=line.reshape(4,)
        x1,x2,y1,y2=points
        cv2.line(img,
                 (x1,y1),
                 (x2,y2),
                 (0,0,255)
                 ,3)
    return img

img=cv2.imread("input") #讀取圖片
edge=get_edge(img) #邊緣偵測
roi=get_roi(edge)
lines=cv2.HoughLinesP(image=roi,
                      rho=3,
                      theta=np.pi/180,
                      threshold=60,
                      minLineLength=40,
                      maxLineGap=50)
#image:輸入影像
#rho:窗框大小，單位為pixel,Theta:弧度來控制窗框大小
#threshold:多少線段穿過資料點才符合
#minLineLength:找到線段最短長度(單位pixel)(ex:設定為40,小於40直線會被忽略)
#maxLineGap:點跟點之間距離(單位pixel)參數越大線段越長
print(lines)
if lines is not None:
    img=draw_lines(img,lines)
else:
    print("偵測不到線")
# cv2.imshow("roi", roi)
cv2.imshow("Line",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

