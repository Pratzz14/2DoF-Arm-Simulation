'''
2 DoF robotic arm 2D simulation
Imagining a SCARA ARM moving in 2D

Author: Pratik Mahankal - pratik.mahankal14@gmail.com

-- Opens up a OpenCV window 
-- Left mouse click to assign the goal end point
-- Adjustable ARM lengths
-- Adjustable window length

'''

import cv2
import numpy as np
from inverse_k import inverse_k2dof as ik
import math

arm1_len = 300
arm2_len = 200

window_width = 640
window_height = 480

img = np.zeros((window_height,window_width,3), dtype=np.uint8)

def graphics(click_x,click_y,a1,a2,x,y):

    # Handling the Quadrant 2, negative values
    if x < 0:
        a1 += 180

    x = click_x
    y = click_y
    
    global img
    img = np.zeros((window_height,window_width,3), dtype=np.uint8)
    img = cv2.circle(img, (int(click_x) ,int(click_y)), 10, (0, 0, 255), -1)
    img = cv2.line(img, (window_width//2,0), (window_width//2,window_height), (0, 0, 255), 1)
    img = cv2.rectangle(img, ((window_width//2)-50,window_height-50), ((window_width//2)+50,window_height+50), (0, 0, 255), -1)

    # ARM1 graphics
    x1 = (window_width//2) + (arm1_len * math.cos(math.radians(a1)))
    y1 = window_height - (arm1_len * math.sin(math.radians(a1)))
    img = cv2.line(img, ((window_width//2),window_height), (int(x1),int(y1)), (0, 255, 0), 9)

    # ARM2 graphics
    if x > x1:
        x2 = x1 + (arm2_len * math.cos(math.radians(a1+a2)))
        y2 = y1 - (arm2_len * math.sin(math.radians(a1+a2)))
    else:
        x2 = x1 - (arm2_len * math.cos(math.radians(180-(a1+a2))))
        y2 = y1 - (arm2_len * math.sin(math.radians(180-(a1+a2))))

    img = cv2.line(img, (int(x1),int(y1)), (int(x2),int(y2)), (255, 0, 0), 3)

    cv2.imshow("simulation",img)

def click_event(event, x, y, flags, params):

    # Mouse event: ON LEFT CLICK
    if event == cv2.EVENT_LBUTTONDOWN:

        click_x = x
        click_y = y
        
        # handling x-cord
        if (x == window_width//2):x = 0
        elif x < window_width//2:x = -(window_width//2-x)
        else: x = x - window_width//2
        
        # handling y-cord
        y = window_height - y
        print(x, y, " -- ",end=" ")
        print(x,y)

        possible,a1,a2 = ik(x,y,arm1_len,arm2_len)
        if not possible:
            print("Not possible")
        else:
            print(a1,a2)
            graphics(click_x,click_y,a1,a2,x,y)


# Generating a black canvas with background
img = np.zeros((window_height,window_width,3), dtype=np.uint8)
img = cv2.line(img, (window_width//2,0), (window_width//2,window_height), (0, 0, 255), 1)
img = cv2.rectangle(img, ((window_width//2)-50,window_height-50), ((window_width//2)+50,window_height+50), (0, 0, 255), -1)

#Display image and initialize mouse click event
cv2.imshow("simulation",img)
cv2.setMouseCallback('simulation', click_event)

k = cv2.waitKey(0)
if k == ord('q') or k == 27:
    cv2.destroyAllWindows()