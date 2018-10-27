s = raw_input().strip()
k = "abcdefghijklmnopqrstuvwxyz"

for _ in range (input()) :
	t = 0
	p = []
	for i in range (27) :
		p.append(0)

	l, r = map(int, raw_input().split())
	l = l-1
	
	for i in range(l,r) :
		g = 0
		for j in k :
			if s[i] == j :
				p[g] += 1
				break
			g += 1
	p.sort()
	i = 26
	c = 0
	y = 0
	t = 0
	while p[i] != 0 :
		if p[i] >= 2 :
			c += p[i]
			y += 1
		else :
			t += 1
		i -= 1
	m = 1000000007
	kj = 1
	for i in range (1,y+1) :
		kj = (kj%m*i%m)%m
	if t >= 1 :
		print (kj%m*t%m)%m
	else :
		print kj



