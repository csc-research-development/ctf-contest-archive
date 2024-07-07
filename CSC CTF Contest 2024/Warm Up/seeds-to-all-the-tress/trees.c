#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int flag[] = {1462820536,
1023494154,
782855190,
143566893,
336631204,
466153543,
2014079576,
1946762140,
1130028559,
884172053,
1430145906,
1409856961,
694143697,
1980838511,
1059496570,
55428430,
1827617549,
1624935103,
125753425,
1893725788,
768460659,
1671307704,
840562299,
376997612,
784812683,
308505445,
534546456,
316869103,
1104193396,
582343605,
49757446};

void init(){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
    alarm(10);
}

int main(){
    init();

    srand(0xbabe);
    char data[1001];
    int store;
    scanf(" %[^\n]", data);

    for (int i=0; data[i]!='\0'; i++){
        store = data[i]^rand();
        if (store != flag[i]){
            printf("Incorrect flag!\n");
            return 1;
        }
    }
    printf("Correct flag!\n");

    return 0;
}