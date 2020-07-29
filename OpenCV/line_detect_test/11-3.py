import cv2
import autocar_module as m
import numpy as np
input="./images/highway.jpg"
img = cv2.imread(input)
edge = m.get_edge(img)              # 邊緣偵測
mask = np.zeros_like(edge)          # 全黑遮罩
points = np.array([[[351,342],
                    [399,292],
                    [473,283],
                    [671,376]]])

cv2.fillPoly(mask, points, 255)     # 繪製三角形
cv2.imshow('Mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()