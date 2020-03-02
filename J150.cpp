#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int x = 0; int i = 1; int n = 1; int t = 1;
	scanf("%d", &x);
	
	for (n = 1; n <= x; n++){
		for (i = 1; i <= x; i++){
			printf ("%d ", t);
			if (i != x) {
				t+=4;
			}
		}
		printf("\n");
	}
	
	return 0;
}
