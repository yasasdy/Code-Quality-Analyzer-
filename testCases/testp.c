# 1 "test.c"
# 1 "<built-in>"
# 1 "<command-line>"
# 31 "<command-line>"
# 1 "/usr/include/stdc-predef.h" 1 3 4
# 32 "<command-line>" 2
# 1 "test.c"
int main(int argc, int *argv[]) {
    int a;
    int b;
    int c;
    int e;
    int a, b, c, e;

    a = 2;
    b = 3;
 c = 0;

    scanf("%d", &e);

    if (a < b || b < c)
    {
        a *= 5;
        a += b;
        a /= 10;
    }
    else
    {
        a--;
    }
 for (int i = 0; i < 10; i++)
 {
  c++;
 }
    printf("Hello");
 add(a, b);
    return 0;
}

void add(int a, int b) {
 a = 3;
 b = 4;
}
