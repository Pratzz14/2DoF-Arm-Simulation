import cv2
import numpy as np

window_width = 640
window_height = 480

def click_event(event, x, y, flags, params):

    # Mouse event: ON LEFT CLICK
    if event == cv2.EVENT_LBUTTONDOWN:
        
        # handling x-cord
        if (x == window_width//2):x = 0
        elif x < window_width//2:x = -(window_width//2-x)
        else: x = x - window_width//2
        
        # handling y-cord
        y = window_height - y
        print(x, y, " -- ",end=" ")
        print(x,y)

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