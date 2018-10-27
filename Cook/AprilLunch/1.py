if __name__ == '__main__' :
	for _ in range (input()) :
		n = input()
		if n%10 == 0 :
			print "0"
		else :
			for i in range (1, 11) :
				n *= 2
				if n%10 == 0 :
					break;
			if n%10 == 0 :
				print i
			else :
				print "-1"
