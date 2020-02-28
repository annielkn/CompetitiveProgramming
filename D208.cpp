#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int N = 0, max = 0, i = 0, rec = 0;
	scanf("%d", &N);
	int a[N] ={0};
	scanf("%d", &a[0]);
	max = a[0];
	for (i = 1; i < N; i++) {
		scanf("%d", &a[i]);
		if (a[i] > max){ rec = i; max = a[i];}
		//printf("%d\n", max);
	}
	max = a[rec];
	printf("%d\n", max);
	if (max>0) {
		a[rec] = a[rec] * -1;
		max = 0;
		for (i = 0; i < N; i++) {
			if (a[i] > max) max = a[i];
		}
		printf("%d\n", max);
	}
	if (max < 0) {
		a[rec] = a[rec] * -1;
		for (i = 0; i < N; i++) {
			a[i] = a[i] * -1;
		}
		max = a[0];
		for (i = 0; i < N; i++) {
			if (a[i] > 0 && a[i] < max) max = a[i];
		}
		printf("%d\n", max * -1);
	}
	return 0;
}
