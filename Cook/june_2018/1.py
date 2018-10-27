def check (a, b, c) :
	if a == b :
		print "0"
	elif a > b :
		print "1"
	else :
		print "2"

if __name__ == '__main__' :
	for _ in range (input()) :
		a, b, c = map(int, raw_input().split())
		if c%2 == 0 :
			a, b = abs(a), abs(b)
		check (a, b, c)

		

