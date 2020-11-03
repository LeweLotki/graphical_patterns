import numpy as np
import cv2

fill = cv2.imread(r'F:\freelancer\projekt2\images\icons\ronded\cfill.png')
circle = cv2.imread(r'F:\freelancer\projekt2\images\icons\ronded\ccircle.png')
line = cv2.imread(r'F:\freelancer\projekt2\images\icons\ronded\cline.png')
paint = cv2.imread(r'F:\freelancer\projekt2\images\icons\ronded\cpaint.png')
pencil = cv2.imread(r'F:\freelancer\projekt2\images\icons\ronded\cpencil.png')
rubber = cv2.imread(r'F:\freelancer\projekt2\images\icons\ronded\crubber.png')
square = cv2.imread(r'F:\freelancer\projekt2\images\icons\ronded\csquare.png')

fill_cord = 35
circle_cord = fill_cord + 100
line_cord = circle_cord + 100
paint_cord = line_cord + 100
pencil_cord = paint_cord + 100
rubber_cord = pencil_cord + 100
square_cord = rubber_cord + 100
size = (60,60)
list_icon = [[fill,fill_cord], [circle, circle_cord] ,[line, line_cord] , [paint, paint_cord], [pencil, pencil_cord], [rubber, rubber_cord], [square, square_cord]]
# list_icon_shaded = [[fill_shaded,fill_cord], [circle_shaded, circle_cord] ,[line_shaded, line_cord] , [paint_shaded, paint_cord], [pencil_shaded, pencil_cord], [rubber_shaded, rubber_cord], [square_shaded, square_cord]]

for val in list_icon:
   val[0] = cv2.resize(val[0],size) 

fill_shaded = cv2.resize(cv2.imread(r'F:\freelancer\projekt2\images\icons\shaded\sfill.png'),size)
circle_shaded = cv2.resize(cv2.imread(r'F:\freelancer\projekt2\images\icons\shaded\scircle.png'),size) 
line_shaded = cv2.resize(cv2.imread(r'F:\freelancer\projekt2\images\icons\shaded\sline.png'),size) 
paint_shaded = cv2.resize(cv2.imread(r'F:\freelancer\projekt2\images\icons\shaded\spaint.png'),size) 
pencil_shaded = cv2.resize(cv2.imread(r'F:\freelancer\projekt2\images\icons\shaded\spencil.png'),size)
rubber_shaded = cv2.resize(cv2.imread(r'F:\freelancer\projekt2\images\icons\shaded\srubber.png'),size) 
square_shaded = cv2.resize(cv2.imread(r'F:\freelancer\projekt2\images\icons\shaded\ssquare.png'),size) 



