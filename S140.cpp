#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int i = 0; int x = 0; int n = 0; int a = 1;
	scanf("%d", &x);
	a = x*x*(x+1)/2;
	for (n=x; n>0; n--){
		for (i=1; i<=x; i++){
			printf("%d ", a);
			a-=n;
		}
		printf("\n");
	}
	return 0;
}
