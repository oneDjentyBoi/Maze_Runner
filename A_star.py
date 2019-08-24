import colorsys
from priority_queue import priority_queue
from Point import Pt
import BFS as b
import math
def heuristic_cost(s,e):
	return abs(s.x - e.x) + abs(s.y - e.y)
def a_s_(s,e,h,w,img):
	pq=priority_queue()
	const=2000
	found=0
	visited = [[0 for i in range(w)]for j in range(h)]
	parent = [[Pt() for i in range(w)]for j in range(h)]
	d = heuristic_cost(s,e)
	pq.push(s,d)
	x_c=[0,0,1,-1]
	y_c=[1,-1,0,0]
	visited[s.y][s.x]=1
	while pq.size()>0:
		temp, g = pq._pop()
		if(temp == e):
			found=1
			break
		for i in range(4):
			t_x = temp.x + x_c[i]
			t_y = temp.y + y_c[i]
			if b.isSafe(t_x,t_y,h,w,img,visited) == True:
				visited[t_y][t_x]=visited[temp.y][temp.x]+1
				parent[t_y][t_x]=temp
				d = heuristic_cost(Pt(t_x,t_y),e)
				pq.push(Pt(t_x,t_y),d)
				img[t_y][t_x]=list(reversed([i * 255 for i in colorsys.hsv_to_rgb(visited[t_y][t_x] / const, 1, 1)]))

	path=[]
	if found==1:
		i=e
		while i!=s:
			path.append(Pt(i.x,i.y))
			i=parent[i.y][i.x]
		path.append(s)
		path.reverse()
		for p in path:
			for i in range(-1,1):
				img[p.y+i][p.x+i]=[0,0,0]
		print("Path found")
	else:
		print("Path not found")