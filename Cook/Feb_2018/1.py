n = input()
s = []
p = ["Beginner", "Junior Developer", "Middle Developer", "Senior Developer", "Hacker", "Jeff Dean"]
for i in range (n) :
	r = map(int, raw_input().split())
	s.append(r)
k = 0
for i in s :
	k = 0
	for j in i :
		k += j
	print p[k]

