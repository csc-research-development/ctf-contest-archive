#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void init(){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
    alarm(10);
}

void win(){
    char filename[] = "flag.txt";
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        printf("Tidak dapat membuka file %s\n", filename);
        return 1;
    }
    char ch;
    while ((ch = fgetc(file)) != EOF) {
        putchar(ch);
    }
    fclose(file);
}

void vuln(){
    char name[1001];
    gets(name);
}

int main(){
    init();
    vuln();
    return 0;
}