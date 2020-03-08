#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	long long p = 0; long long b = 0; long long m = 0; long long r = 0;
	scanf("%lld\n%lld\n%lld\n", &b, &p, &m);
	r = ((b % m)^p) % m;
	printf("%lld", r);
	return 0;
}
