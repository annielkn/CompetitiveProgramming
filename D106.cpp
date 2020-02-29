#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int N = 0;
	scanf("%d", &N);
	if (N % 100 != 11 && N % 100 != 12 && N % 100 != 13){
		switch(N % 10) {
			case 1: {printf("%dst", N); break;}
			case 2: {printf("%dnd", N); break;}
			case 3: {printf("%drd", N); break;}
			case 4: {printf("%dth", N); break;}
			case 5: {printf("%dth", N); break;}
			case 6: {printf("%dth", N); break;}
			case 7: {printf("%dth", N); break;}
			case 8: {printf("%dth", N); break;}
			case 9: {printf("%dth", N); break;}
			case 0: {printf("%dth", N); break;}
		}
	}
	else {
		printf("%dth", N);
	}
	printf("\n");
	return 0;
}
