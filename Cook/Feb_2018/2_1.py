import math
for _ in range (input()) :
	n, a, b, c = map(int, raw_input().split()) 
	c = 0
	for i in range (1, int(math.sqrt(a))) :
		for j in range (1, int(math.sqrt(b))) :
			for k in range (1, int(math.sqrt(c))) :
				if i*j*k == n :
					c += 1
	print c
