#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int v = 0, n = 0, i = 0, cnt = 0, oct = 0;
	scanf("%d", &v);
	oct += v;
	scanf("%d", &n);
	int a[n] = {0};
	for (i = 0; i < n; i++) {
		scanf("%d", &a[i]);
		oct -= a[i];
		if (oct <= 0) {
			cnt++;
			oct += 250;
		}
	}
	printf("$%d", 250*cnt);
	return 0;
}
