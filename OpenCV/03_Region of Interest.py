import cv2
import matplotlib.pyplot as plt
input="./images/highway.jpg"

def get_edge(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(13,13),0)
    canny=cv2.Canny(blur,20,60)
    return canny
img=cv2.imread(input) #讀取圖片
edge=get_edge(img)
plt.imshow(edge)
plt.show()
