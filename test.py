g = (n for n in range(10))
def fibonacci():
	a,b = 0,1
	while 1:
		yield a
		a,b = b,a+b

gg = fibonacci()
for i in range(1):
	print(next(gg))

f = lambda x,y: ((x**i) for i in range(x*y))
print([i for i in f(1,1)])

r = map(lambda x:x**2,(1,2,3,4,5))
print([i for i in r])


f = filter(lambda x : x%2, [i for i in range(10)])
print([i for i in f])


import os

print(os.listdir(path='.'))
print(os.getcwd())
print(os.getcwd())
print([os.path.join(os.getcwd(),i) for i in os.listdir(path='.')])

print([os.path.isdir(i) for i in os.listdir(path='.')])