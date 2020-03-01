#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int main() {
	long N = 0, r = 0;
	int sq = 0, tri = 0;
	double rt = 0.00;
	scanf("%lld", &N);
	rt = sqrt(N);
	r = sqrt(N);
	if (r - rt == 0) {
		sq = 1;
	}
	r = sqrt(2 * N);
	if (2 * N == r * (r + 1) || 2 * N == r * (r - 1)){
		tri = 1;
	}
	if (sq == 1 && tri == 1) printf ("Both\n");
	else if (sq == 1 && tri != 1) printf("Square\n"); 
	else if (tri == 1 && sq != 1) printf("Triangular\n");
	else if (tri != 1 && sq != 1) printf("Neither\n");
	return 0;
}
