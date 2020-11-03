import numpy as np
import cv2

ix = -1
iy = -1
drawing = False
img = cv2.imread(r'F:\freelancer\projekt2\images\wood.png')

def draw_rectangle(event, x, y, flags, param): 
      
    global ix, iy, drawing, img 
      
    if event == cv2.EVENT_LBUTTONDOWN: 
        drawing = True
        ix = x 
        iy = y             
              
    elif event == cv2.EVENT_MOUSEMOVE: 
        if drawing == True: 
            cv2.rectangle(img, pt1 =(ix, iy), 
                          pt2 =(x, y), 
                          color =(0, 255, 255), 
                          thickness = -1) 
      
    elif event == cv2.EVENT_LBUTTONUP: 
        drawing = False
        cv2.rectangle(img, pt1 =(ix, iy), 
                      pt2 =(x, y), 
                      color =(0, 255, 255), 
                      thickness =-1) 