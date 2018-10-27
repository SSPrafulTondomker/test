import math
for _ in range (input()) :
	n, a, b, c = map(int, raw_input().split())
	k = int(math.sqrt(n))
	ct = 0
	l = []
	e = []
	for i in range (1, k+1) :
		if n%i == 0 and n/i != i :
			l.append(i)
			l.append(n/i)
		if n%i == 0 and n/i == i :
			l.append(i)
	for i in  l :
		if i <= a:
			r = int(math.sqrt(n/i))
			w = n/i
			e = []
			for p in range (1, r+1) :
				if w%p == 0 and w/p != p :
					e.append(p)
					e.append(w/p)
				if w%p == 0 and w/p == p :
					e.append(p)
			#print w, e
			for j in e:
				if j <= b :
					if w/j <= c :
						ct += 1
	print ct



			
	
