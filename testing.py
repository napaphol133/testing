import numpy as np
import cv2

green = np.uint8([[[30,50,80 ]]]) #BGR
hsv_green = cv2.cvtColor(green,cv2.COLOR_HSV2BGR)
print green
print hsv_green
