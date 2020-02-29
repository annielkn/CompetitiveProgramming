#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	char s1[256], s2[256], s3[256], s4[256], s5[256];
	gets(s1);
	gets(s2);
	gets(s3);
	gets(s4);
	gets(s5);
	printf("My name is %s.\n", s1);
	printf("My husband is %s.\n", s2);
	printf("We live in a %s.\n", s5);
	printf("I had some play time with %s while taking the %s.\n", s3, s4);
	return 0;
}
