#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	long cnt = 0;
	int fib[41] = {0};
	fib[0] = 0;
	fib[1] = 1;
	int target = 0, i = 0;
	scanf("%d", &target);
	for (i = 0; i < target; i++) {
		fib[i+2] = fib[i] + fib[i+1];
	}
	cnt = fib[target];
	cout << cnt;
	printf("\n");
	return 0;
}
