#include <cmath>
#include <cstdio> 
#define PI 3.14159265
using namespace std;

int main() {
	double ret = 0.00, grad = 0.00;
	int a = 0, b = 0, c = 0;
	scanf("%d %d %d", &a, &b, &c);
	grad = c * PI / 180;
	ret = sin(grad);
	ret = ret * a * b;
	printf("%.3lf\n", ret/2);
	return 0;
}
