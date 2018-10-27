for _ in range (input()) :
	n = input()
	s = 0
	l = map(int, raw_input().split())
	for i in l :
		s += i
	k = 0
	s = str(s)
	for i in s :
		k += int(i)
	if k%3 == 0 :
		print "Yes"
	else :
		print "No"
