for _ in range (input()) :
	n, k, b = map(int, raw_input().split())
	l = map(int, raw_input().split())
	l.sort()
	r = []
	for i in l :
		r.append(k*i+b)
	i = 0
	c = 1
	while i != n :
		j = i
		f = 0 
		while j != n :
			if r[i] <= l[j] :
				f = 1
				c += 1
			j += 1
		if f == 0 :
			i += 1
		else :
			i = j
	print c

