import cv2
import autocar_module as m
import numpy as np
input="./images/highway.jpg"
def get_roi(img):
    mask = np.zeros_like(img)           # 全黑遮罩
    points = np.array([[[351,342],[399,292],[473,283],[671,376]]])
    cv2.fillPoly(mask, points, 255)     # 繪製多邊形
    roi = cv2.bitwise_and(img, mask)
    return roi
#---------------------------------------------------#
img = cv2.imread(input)        # 讀取圖片
edge = m.get_edge(img)              # 邊緣偵測
roi = get_roi(edge)                 # 取得 ROI
cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()