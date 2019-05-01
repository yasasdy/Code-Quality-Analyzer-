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

// int main() {
//     int a, b, c;

//     a = 2;
//     b = 3;
//     c = 0;

//     if (a < b) {
//         a *= 5;
//         a += b;
//         a /= 10;
//     } else {
//         a--;
//     }
    
//     for (int i = 0; i < 10; i++)
//     {
//         c++;
//     }
//     add();
//     return 0;
// }

// void add() {
//     int a, b;
//     a = 3;
//     b = 4;
// }