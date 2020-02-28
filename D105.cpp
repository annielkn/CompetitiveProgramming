#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int a1 = 0, a2 = 0, a3 = 0;
	int b1 = 0, b2 = 0, b3 = 0;
	scanf("%d %d %d", &a1, &a2, &a3);
	scanf("%d %d %d", &b1, &b2, &b3);
	if (a1 > b1) {
		printf("After\n");
	}
	else if (b1 > a1){
		printf("Before\n");
	}
	else if (b1 == a1) {
		if (a2 > b2) printf("After\n");
		else if (b2 > a2) printf("Before\n");
		else if (a2 == b2) {
			if (a3 > b3) printf("After\n");
			else if (b3 > a3) printf("Before\n");
			else if (a3 == b3) printf("Same\n");
		}
	}
	return 0;
}
