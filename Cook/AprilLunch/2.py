l = [True for i in range (100000+1)]
def gcd (x, y) :
	while (y) :
		x, y = y, x%y
	return x
def seive () : 
	p = []
	n = 100000;
	i = 2
	while i*i <= n :
		if l[i] == True :
			for j in range (i*2, n, i) :
				l[j] = False;
		i += 1
 
	for i in range (n) :
		if l[i]:
			p.append(i)
	return p
 
 
if __name__ == '__main__' :
	p = seive ()
	for _ in range (input()) :
		n, k = map(int, raw_input().split())
		a = map(int, raw_input().split())
		p = p[::-1]
		c = 0
		f = 0
		for i in a :
			if i == a[0] :
				f += 1
		if  f== len(a) :
			f = 1
		else :
			f = 0
		for i in range (n) :
			for j in p :
				r = 0
				if j != 0 and a[i]%j == 0 :
					r = a[i]/j
				if r != 0 and r <= k:
					a[i] = j
					c += 1
			if c > 2 :
				break
		s = a[0]
		for i in a :
			s = gcd(s, i)
	
		if c <= 1 or f == 1 or s > 1:
			print "NO"
		else :
			print "YES"
