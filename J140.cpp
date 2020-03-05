#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int i = 0; int x = 0; int n = 0; int a = 1;
	scanf("%d", &x);
	for (n=1; n<=x; n++){
		a = n*n;
		for (i=1; i<=x; i++){
			printf("%d ", a);
			a+=n;
		}
		printf("\n");
	}
	return 0;
}
