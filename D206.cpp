#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int start = 0;
	scanf("%d", &start);
	printf("%d\n", start);
	while (start != 1){
		if (start % 2 == 1) {
			start = start * 3 + 1;
			printf("%d\n", start);
		}
		if (start % 2 == 0) {
			start = start / 2;
			printf("%d\n", start);
		}
	}
	return 0;
}
