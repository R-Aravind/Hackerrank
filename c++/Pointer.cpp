#include <stdio.h>

void update(int *a,int *b) {
    int sum;
    sum= (*a)+(*b);
    *b=(*a>=*b)?(*a-*b):(*b-*a);
    *a=sum;

}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
