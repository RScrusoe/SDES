
t = int(input())
ans = []
while t>0:
	'''
		x = int(input())
		while 1:
			x+=1
			if str(x) == str(x)[::-1]:
				print(x)
				break
	'''

	'''
	ct = 0
	n = int(input())
	l = list(str(n))
	
	for x in l:
		if (int(x)==0) or (int(x)==6) or (int(x)==9):
			ct+=1
		elif int(x)==8:
			ct+=2
	ans.append(ct)
	'''
	stops = int(input())
	lines = int(input())
	data = [[] for i in range(lines)]
	for i in range(lines):
		data[i].append(int(input()))
		data[i].append(int(input()))
		data[i].append(int(input()))

	


	t-=1
for i in ans:
	print(i)
