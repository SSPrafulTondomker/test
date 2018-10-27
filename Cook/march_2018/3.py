import math
def hell(p) :
	print p

for _ in range (input()) :
	a, b, c = map(int, raw_input().split())
	p = 0
	if b == int((a+c)/2.0) :
		hell(p)
	else :
		x, y, z, z2 = 2*b - a, 2*b -c, int(math.ceil((a*1.0 + c )/2.0)), int(math.floor((a*1.0 + c*1.0))/2.0)
		a1, b1, c1, d1 = abs(c - x), abs (a - y), abs (b-z), abs(b-z2)
		q = min(a1, b1)
		p = min(c1, q)
		p = min(d1, p)
	#	print z
		if (a+c)/2 != math.ceil((a*1.0 + c*1.0)/2.0) :
			p += 1
		hell(p)
