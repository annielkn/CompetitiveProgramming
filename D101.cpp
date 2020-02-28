#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	char a[8];
	int i = 0;
	for(i = 0; i < 8; i++){
		scanf("%c", &a[i]);
	}
	if (a[0]=='2') printf("Fixed\n");
	if (a[0]=='3') printf("Fixed\n");
	if (a[0]=='5') printf("Mobile\n");
	if (a[0]=='6') printf("Mobile\n");
	if (a[0]=='9') printf("Mobile\n");
	return 0;
}
