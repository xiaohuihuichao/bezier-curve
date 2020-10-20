import cv2
import numpy as np

from 贝塞尔曲线 import bezier


points = np.asarray([[100, 315], [200, 380], [300, 495], [400, 660], [500, 875]])
canvas = np.zeros((1100, 550, 3), dtype=np.uint8) + 100

curve = bezier(points, 3)

for point in points:
    canvas = cv2.circle(canvas, (point[0], point[1]), 3, (255, 255, 255), 3)
    
for t in range(0, 2000):
    t /= 2000
    x, y = curve(t).reshape(-1)
    cv2.circle(canvas, (round(x), round(y)), 1, (255, 0, 255))

cv2.imwrite("a.jpg", canvas)
