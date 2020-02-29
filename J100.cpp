#include <iostream>
#include <cstdio>
using namespace std;
int cnt=0;
int main () {
    int t=0, x=0, y=0;
    scanf("%d", &x);
    for (t=1; t<=x; t++) {
        for (y=1; y<=t; y++){
            cnt++;
            if (t==y) printf("%d\n", cnt); else printf("%d ", cnt);
        }
    }
    for (t=x-1; t>0; t--) {
        for (y=1; y<=t; y++){
            cnt++;
            if (t==y) printf("%d\n", cnt); else printf("%d ", cnt);
        }
    }
    return 0;
}
