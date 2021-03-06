import numpy as np
import cv2
import math
from packages import image as im
from packages import drawing as dw

ix = -1
iy = -1
drawing = False
img = cv2.imread(r'F:\freelancer\projekt2\images\wood.png')

def draw_rectangle(event, x, y, flags, param): 
      
    global ix, iy, drawing, img 
      
    cv2.circle(img, (90,im.square_cord+30), 42, (215,215,215), -1)
    img[im.square_cord:im.square_cord+im.size[0], im.size[0]:2*im.size[0], :] = im.square_shaded    
      
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
      
    cv2.circle(img, (90,im.rubber_cord+30), 42, (215,215,215), -1)
    img[im.rubber_cord:im.rubber_cord+im.size[0], im.size[0]:2*im.size[0], :] = im.rubber_shaded  
      
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
    
    cv2.circle(img, (90,im.pencil_cord+30), 42, (215,215,215), -1)
    img[im.pencil_cord:im.pencil_cord+im.size[0], im.size[0]:2*im.size[0], :] = im.pencil_shaded
      
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

def circle(event, x, y, flags, param): 
      
    global ix, iy, drawing, img 
    
    cv2.circle(img, (90,im.circle_cord+30), 42, (215,215,215), -1)
    img[im.circle_cord:im.circle_cord+im.size[0], im.size[0]:2*im.size[0], :] = im.circle_shaded
    
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
                cv2.circle(img, (int((ix+x)/2), int((iy+y)/2)),int(math.sqrt( ((ix-x)**2)+((iy-y)**2) )),(0,0,0),-1)
      
    elif event == cv2.EVENT_LBUTTONUP: 
        drawing = False
        if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900:
            cv2.circle(img, (int((ix+x)/2), int((iy+y)/2)),int(math.sqrt( ((ix-x)**2)+((iy-y)**2) )),(0,0,0),-1)

def line(event, x, y, flags, param): 
      
    global ix, iy, drawing, img 
    
    cv2.circle(img, (90,im.line_cord+30), 42, (215,215,215), -1)
    img[im.line_cord:im.line_cord+im.size[0], im.size[0]:2*im.size[0], :] = im.line_shaded
    
    if event == cv2.EVENT_LBUTTONDOWN: 
        drawing = True
        ix = x 
        iy = y             
        if x > 70 and x < 140: 
            cv2.setMouseCallback("image", activate) 
            
    # elif event == cv2.EVENT_MOUSEMOVE: 
        # if drawing == True:
            # # print(ix,iy)
            # if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900 :
                # cv2.line(img,(ix,iy),(x,y),(0,0,0),2)
      
    elif event == cv2.EVENT_LBUTTONUP: 
        drawing = False
        if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900:
            cv2.line(img,(ix,iy),(x,y),(0,0,0),2)

def plume(event, x, y, flags, param): 
      
    global ix, iy, drawing, img 
    
    cv2.circle(img, (90,im.plume_cord+30), 42, (215,215,215), -1)
    img[im.plume_cord:im.plume_cord+im.size[0], im.size[0]:2*im.size[0], :] = im.plume_shaded    
      
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
                cv2.line(img,(ix,iy),(x,y),(0,0,0),2)
      
    elif event == cv2.EVENT_LBUTTONUP: 
        drawing = False
        if iy > 50 and iy < 700 and ix > 250 and ix < 900 and y > 50 and y < 700 and x > 250 and x < 900:
            cv2.line(img,(ix,iy),(x,y),(0,0,0),2)

def activate(event, x, y, flags, param):   
    
    for val in im.list_icon:
        cv2.circle(img, (90,val[1]+30), 42, (255,255,255), -1)
        img[val[1]:val[1]+im.size[0], im.size[0]:2*im.size[0], :] = val[0]
    
    if event == cv2.EVENT_LBUTTONDOWN and y > im.square_cord and y < im.square_cord+70 and x > 70 and x < 140: 
        cv2.setMouseCallback("image", draw_rectangle)
        
    if event == cv2.EVENT_LBUTTONDOWN and y > im.rubber_cord and y < im.rubber_cord+70 and x > 70 and x < 140:
        cv2.setMouseCallback("image", rubber)
    
    if event == cv2.EVENT_LBUTTONDOWN and y > im.pencil_cord and y < im.pencil_cord+70 and x > 70 and x < 140:
        cv2.setMouseCallback("image", pencil)  
    
    if event == cv2.EVENT_LBUTTONDOWN and y > im.circle_cord and y < im.circle_cord+70 and x > 70 and x < 140:
        cv2.setMouseCallback("image", circle)  
        
    if event == cv2.EVENT_LBUTTONDOWN and y > im.line_cord and y < im.line_cord+70 and x > 70 and x < 140:
        cv2.setMouseCallback("image", line)  

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
  


