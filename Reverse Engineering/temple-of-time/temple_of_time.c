// gcc temple_of_time.c -o temple

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>
#include <unistd.h>

#define FLAG "CSC{fake_flag}"

void init(){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
    alarm(3);
}

// Seed getter
int r66666666666666666666666666666666666666666666666666666666666666666666(int a, int b, int c, int d, int e, int f, int g, int h, int i, int j, int k, int l, int m, int n, int o, int p){
    return j ^ p ^ a ^ m ^ f ^ b ^ e ^ i ^ d ^ h ^ c ^ g ^ k ^ l ^ n ^ o;
}

// Win
void r6666666666666666666666666666666666666666666666666666666666666666666666666(){
    printf("GG, here is ur flag : %s\n", FLAG);
    exit(1337);
}

// banner
void r6666666666666666666666666666666666666666666666666666666666666666666666666666666(){
    printf("           /\\          \n");
    printf("         _/  \\_        \n");
    printf("        /      \\       \n");
    printf("       /        \\      \n");
    printf("      /    /\\    \\     \n");
    printf("     /____/__\\____\\    \n");
    printf("    /     /    \\     \\ \n");
    printf("   /_____/      \\_____\\\n");
    printf("  /\\    /________\\    /\\\n");
    printf(" /  \\  /          \\  /  \\\n");
    printf("/____\\/____________\\/____\\\n");
}

// Loading bar
void r66666666666666666666666666666666666666666666666666666666666666666666666666(char *a, unsigned long long delay) {
    char loader[4] = {'-', '\\', '|', '/'};
    int i;

    for(i = 0; i < delay; i++) {
        printf("\r[%c] %s", loader[i % 4], a);
        sleep(.2);
    }
}

// Fail
void r66666666666666666666666666666666666666666666666666666666666666666666666666666666(){
    puts("Congrats!");
    r66666666666666666666666666666666666666666666666666666666666666666666666666("Just wait, still trying to getting your flag...", ULLONG_MAX);
    r6666666666666666666666666666666666666666666666666666666666666666666666666();
}

// Start
int r666666666666666666666666666666666666666666666666666666666666666666() {
    short year;

    // banner
    r6666666666666666666666666666666666666666666666666666666666666666666666666666666();

    puts("\n===== Temple of Time =====");
    puts("#> Tell me what year do you want to go?");
    printf("$> ");
    scanf("%4hd", &year);
    srand(year);

    int a = rand(), b = rand(), c = rand(), d = rand(), e = rand(), f = rand(), g = rand(), h = rand(), i = rand(), j = rand(), k = rand(), l = rand(), m = rand(), n = rand(), o = rand(), p = rand();

    puts("");

    // Loading bar
    r66666666666666666666666666666666666666666666666666666666666666666666666666("Generating the password...", year%100);
    puts("");

    // Seed generator
    int newSeed = r66666666666666666666666666666666666666666666666666666666666666666666(f, a, m, c, j, b, e, d, g, i, h, k, l, n, o, p);

    srand(newSeed%10000);

    printf("Enter the password : ");
    scanf("%4hd", &year);
    puts("");

    if (year != rand()%10000){
        // Fail
        r66666666666666666666666666666666666666666666666666666666666666666666666666666666();
    }

    // Win
    r6666666666666666666666666666666666666666666666666666666666666666666666666();
    return 0;
}


int main(){
    // alarm here
    init();
    r666666666666666666666666666666666666666666666666666666666666666666();
    return 0;
}
