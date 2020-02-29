#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int x = 0, y = 0, z = 0, cnt = 0;
	char m = 0, n = 0;
	scanf("%d %c %d %c %d", &x, &m ,&y, &n, &z);
	if (m!='*' && n=='*') {
		cnt += y * z;
		if (m == '+') cnt += x;
		if (m == '-') cnt = x - cnt;
	}
	else {
		if (m == '+' && n == '+') cnt = cnt + x + y + z;
		if (m == '+' && n == '-') cnt = cnt + x + y - z;
		if (m == '-' && n == '+') cnt = cnt + x - y + z;
		if (m == '-' && n == '-') cnt = cnt + x - y - z;
		if (m == '*' && n == '+') cnt += x * y + z;
		if (m == '*' && n == '-') cnt += x * y - z;
		if (m == '*' && n == '*') cnt += x * y * z;
	}
	printf("%d\n", cnt);
	return 0;
}
