import cv2

input="./images/way.png"
img=cv2.imread(input) #讀取圖片
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #灰階處理
blur=cv2.GaussianBlur(gray,(3,3),0) #高斯模糊的目的在於降低影像雜訊
# (輸入影像,高斯矩陣大小(矩陣越大模糊效果越好),標準差(高斯分布標準差通常設為零))
cv2.imshow('noraml',img)
cv2.imshow('gray',gray)
cv2.imshow('Blur',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()