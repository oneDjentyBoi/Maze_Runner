import cv2
import numpy as np
import threading
import time
import sys
import BFS as b
import A_star as a_star
from Point import Pt
r=0.65 # resize factor
s=0
e=0
p=0
wid=2
flag=0
def resize_image(img):
		h, w = img.shape[:2]
		return cv2.resize(img,(int(h),int(r*w)))

def mouse_event(event,x,y,flags,params):
		global s,e,img,p,flag
		if event==cv2.EVENT_LBUTTONUP:
			if p==0:
				cv2.rectangle(img,(x-wid,y-wid),(x+wid,y+wid),(0, 255, 0),-1)
				s = Pt(x,y)
				p+=1
			elif p==1:
				cv2.rectangle(img,(x-wid,y-wid),(x+wid,y+wid),(204, 0, 255),-1)
				e = Pt(x,y)
				p+=1
		if event==cv2.EVENT_RBUTTONUP:
			flag=1

def disp():
		global img
		cv2.imshow("Maze_runner",img)
		cv2.setMouseCallback('Maze_runner',mouse_event)
		u=0
		while True and flag==0:
			cv2.imshow("Maze_runner",img)
			cv2.waitKey(1)

img=cv2.imread("MAZE_.png", cv2.IMREAD_GRAYSCALE)
img=resize_image(img)
_,img=cv2.threshold(img,120,255,cv2.THRESH_BINARY)
img=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
h, w = img.shape[:2]

t= threading.Thread(target=disp, args=())
t.start()
while p<2:
	pass
t2=time.time()
#b.bfs(s,e,h,w,img)
a_star.a_s_(s,e,h,w,img)
print(time.time()-t2)
t.join()

sys.exit(1)
cv2.waitKey(0)
