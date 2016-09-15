def integrate(f,a,b,n):
	h = float((b-a)/n)
	total = 0
	for i in range(n):
		total += f(a + (i+0.5)*h)*h
	return total


def test_integrate():
	assert abs(integrate(lambda x: x, 0.0,1.0,10) - 0.5) < 1e-10
	assert abs(integrate(lambda x: x*x,0.0,1.0,10) - 1.0/3.0) < 1e-3