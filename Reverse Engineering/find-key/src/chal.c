//  Find the secret key to help Doninic Totero 
#include <stdio.h>
#include <string.h>

// Reference Alphabet
const char *al = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                        "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~";

void a() {
    const char *what = "a$adR?'c4zQ#%?`clvQ%?P?`O`O";

    char name[100];
    printf("What is your name? ");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = 0;

    char x[100];
    int l = strlen(name);

    for (int i = 0; i < l; i++) {
        char *p = strchr(al, name[i]);
        if (p) {
            int n = p - al;
            int w = (i % 2 == 0) ? 30 : 47;
            int o = (n + w + strlen(al)) % strlen(al);
            x[i] = al[o];
        } else {
            x[i] = name[i];
        }
    }
    x[l] = '\0'; 
    printf("Hello %s\n", name);
    unsigned char hmm[] = {0, 0, 0, 78, 67, 1, 16, 107, 39, 10, 106, 19, 58, 44, 11, 103, 15, 24, 99, 21, 106, 100, 126, 120, 117, 112, 76};
    if (strcmp(x, what) == 0) {
        for (int i = 0; i < 27; i++) {
            hmm[i] ^= name[i % strlen(name)];
        }
        printf("Welcome back, %s\n", hmm);
    }
}

void c() {
    int value1, value2;

    printf("Your First Number: ");
    scanf("%d", &value1);
    getchar();

    printf("Your Second Number: ");
    scanf("%d", &value2);

    int lowestValue = value1;

    if (value1 < value2) {
        lowestValue = value1;
    } else if (value2 < value1) {
        lowestValue = value2;
    }

    printf("The Lowest Number is %d\n", lowestValue);
}

int main() {
    a();
    c();

    return 0;
}
