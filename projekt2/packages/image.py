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
for val in list_icon:
   val[0] = cv2.resize(val[0],size) 





