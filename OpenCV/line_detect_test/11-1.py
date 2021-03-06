import cv2
input="./images/highway.jpg"
def get_edge(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # 灰階處理
    blur = cv2.GaussianBlur(gray, (13, 13), 0)      # 高斯模糊
    canny = cv2.Canny(blur, 20, 60)                # 邊緣偵測
    return canny
#----------------------------------------------#
img = cv2.imread(input)    # 讀取圖片
edge = get_edge(img)           
cv2.imshow('Edge', edge)        # 顯示邊緣圖
cv2.waitKey(0)
cv2.destroyAllWindows()