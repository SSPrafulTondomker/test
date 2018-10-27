#include <bits/stdc++.h>
using namespace std;
long long int maxof (int a, int b, int c)
{
	if (a >= b && a >= c)
		return a;
	else if (b >= a && b >= c)
		return b;
	else 
		return c;
}

int main()
{
	int t;
	scanf ("%d", &t);
	while (t--)
	{
		int n, a, b, c, k;
		scanf ("%d %d %d %d", &n, &a, &b, &c);
		k = maxof (a, b, c);
		if (k == a) 
		{
		}
		else if (k == b)
		{
		}
		else 
		{
		}
	}
	return 0;
}
