from Point import Pt

def heapify(arr,i):
	smallest=i
	l=2*i+1
	r=2*i+2
	if smallest<len(arr):
		a,b=arr[smallest]
	if l<len(arr):
		f,g=arr[l]
	if r<len(arr):
		h,j=arr[r]
	if l<len(arr) and b>g:
		smallest = l
		a,b=arr[smallest]
	if r<len(arr) and b>j:
		smallest = r
		a,b=arr[smallest]
	if smallest!=i:
		t = arr[smallest]
		arr[smallest] = arr[i]
		arr[i] = t
		heapify(arr,smallest)

class priority_queue:
	def __init__(self):
		self.cap=-1
		self.pq=[]
	def size(self):
		return len(self.pq)
	def push(self,s,d):
		self.pq.append((s,d))
		self.cap+=1
		i=self.cap
		a,b=self.pq[int((i-1)/2)]
		while i!=0 and b>d:
			t=self.pq[i]
			self.pq[i]=self.pq[int((i-1)/2)]
			self.pq[int((i-1)/2)]=t
			a,b=self.pq[i]
			i=int((i-1)/2)
	def _pop(self):
		if(len(self.pq)>0):
			t=self.pq[0]
			self.pq[0]=self.pq[self.cap]
			heapify(self.pq,0)
			self.cap-=1
			self.pq.pop()
			return t