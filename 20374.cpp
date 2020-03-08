#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int main() {
	long long p = 0; long long b = 0; long long m = 0; long long r = 0;
	scanf("%lld\n%lld\n%lld\n", &b, &p, &m);
	r = pow((b % m), p);
	r  = r % m;
	printf("%lld", r);
	return 0;
}
