import numpy as np
import cv2
from packages import image as im
from packages import drawing as dw

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
        if x > 70 and x < 140: 
            cv2.setMouseCallback("image", activate)      
    
    elif event == cv2.EVENT_MOUSEMOVE: 
        if drawing == True:
            # print(ix,iy)
            if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900 :
                cv2.rectangle(img, pt1 =(ix, iy), pt2 =(x, y),  color =(0, 0, 0), thickness = -1) 
            # if x > 70 and x < 140: 
                # cv2.setMouseCallback("image", activate)
    
    elif event == cv2.EVENT_LBUTTONUP: 
        drawing = False
        if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900:
            cv2.rectangle(img, pt1 =(ix, iy), pt2 =(x, y), color =(0, 0, 0), thickness =-1) 
        # if x > 70 and x < 140: 
            # cv2.setMouseCallback("image", activate)

def rubber(event, x, y, flags, param): 
      
    global ix, iy, drawing, img 
      
    if event == cv2.EVENT_LBUTTONDOWN: 
        drawing = True
        ix = x 
        iy = y             
        if x > 70 and x < 140: 
            cv2.setMouseCallback("image", activate)    
            
    elif event == cv2.EVENT_MOUSEMOVE: 
        if drawing == True:
            # print(ix,iy)
            if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900 :
                cv2.rectangle(img, pt1 =(ix, iy), pt2 =(x, y),  color =(255, 255, 255), thickness = -1) 
      
    elif event == cv2.EVENT_LBUTTONUP: 
        drawing = False
        if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900:
            cv2.rectangle(img, pt1 =(ix, iy), pt2 =(x, y), color =(255, 255, 255), thickness =-1) 

def pencil(event, x, y, flags, param): 
      
    global ix, iy, drawing, img 
      
    if event == cv2.EVENT_LBUTTONDOWN: 
        drawing = True
        ix = x 
        iy = y             
        if x > 70 and x < 140: 
            cv2.setMouseCallback("image", activate) 
            
    elif event == cv2.EVENT_MOUSEMOVE: 
        if drawing == True:
            # print(ix,iy)
            if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900 :
                img[y:y+2,x:x+2,:] = (0,0,0)
      
    elif event == cv2.EVENT_LBUTTONUP: 
        drawing = False
        if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900:
            img[y:y+2,x:x+2,:] = (0,0,0)

def activate(event, x, y, flags, param):        

    if event == cv2.EVENT_LBUTTONDOWN and y > 635 and y < 705 and x > 70 and x < 140: 
        cv2.setMouseCallback("image", draw_rectangle)
        
    if event == cv2.EVENT_LBUTTONDOWN and y > 535 and y < 605 and x > 70 and x < 140:
        cv2.setMouseCallback("image", rubber)
    
    if event == cv2.EVENT_LBUTTONDOWN and y > 435 and y < 505 and x > 70 and x < 140:
        cv2.setMouseCallback("image", pencil)  

img[50:700,250:900,:] = (255, 255, 255)
# print(np.shape(img), np.shape(im.fill))
for val in im.list_icon:
    cv2.circle(img, (90,val[1]+30), 42, (255,255,255), -1)
    img[val[1]:val[1]+im.size[0], im.size[0]:2*im.size[0], :] = val[0]

cv2.namedWindow(winname = "image") 
cv2.setMouseCallback("image", activate)

# if rectangle == True:
    # cv2.setMouseCallback("image", draw_rectangle) 
    
while True: 
    cv2.imshow("image", img) 
    if cv2.waitKey(10) == 27: 
        break
    elif cv2.waitKey(10) == ord('c'):
        img[50:700,250:900,:] = (255, 255, 255)

    
cv2.destroyAllWindows() 
  


