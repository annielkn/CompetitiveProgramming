#include <iostream>
#include <cstdio>
using namespace std;

int main () {
	int n=0, ln=0, i=0, j=0, tmp=0;
	scanf("%d", &n);
	for (ln = 0; ln < n; ln++){
		for (j = 0; j < ln; j++) {
			tmp = ln*ln+1;
			printf("%d ", tmp-(ln*j));
		}
		printf("1\n");
	}
	return 0;
}
