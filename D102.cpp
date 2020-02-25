#include <iostream>
#include <cmath>
#include <cstdio> 
using namespace std;

int main() {
	double fare=0.00;
	char i;
	int n;
	scanf("%c%lf", &i, &fare);
	n = fare * 10;
	if(n % 2 == 1) fare = fare/2 + 0.05;
	else fare = fare/2;
	printf("$%.1lf\n", fare);
	return 0;
}
