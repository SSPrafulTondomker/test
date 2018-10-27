for _ in range (input()) :
	n, a, b, c = map(int, raw_input().split())
	print len([(i, j, k) for i in range(1,n+1) for j in range(1,n+1) for k in range (1,n+1) if i <= a and j <= b and k <= c and i*j*k == n])
