// gcc -fpie -fstack-protector -O0 -static chall_demo.c -o chall_demo
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>

#define secret_society_key "DEMO_KEY"
#define CANARY_SIZE 8
#define BUFSIZE 64
#define FLAGSIZE 128

unsigned long seed=0;
char global_canary[CANARY_SIZE];
char buf_msg[BUFSIZE];
char canary[CANARY_SIZE];

int first_check() {
    char buf[32];
    printf("[ASK] the secret key : ");
    read(0, buf, 20);
    if (strncmp(buf, secret_society_key, strlen(secret_society_key)) == 0) {
        return 1;
    } else {
        return 0;
    }
}

void read_canary() {
    int fd = open("/dev/urandom",O_RDONLY);
    read(fd, global_canary, CANARY_SIZE);
    close(fd);

    for (size_t i = 0; i < CANARY_SIZE; i++) {
        global_canary[i] = ((int)(global_canary[i]&0xff) % 90) + 35;
    }
}

void menu_help() {
    puts("\n===| DEMO VERSION |===");
    puts("MSG");
    puts("GET");
    puts("QUIT");
}

void menu_msg(){
    // initialization
    char *new_buf = malloc(1024);
    char *endptr;
    memset(buf_msg, 0, BUFSIZE);
    memcpy(canary,global_canary,CANARY_SIZE);
    
    // seed check ?
    printf("[ASK] seed check (ex: 0xdeadbeef) : ");
    read(0, new_buf, 64);

    // Convert the hexadecimal string to a long integer
    if (strtoul(new_buf, &endptr, 16) != seed) {
        // printf("%lu|%lu\n", strtoul(new_buf, &endptr, 16), seed); // debug
        printf("[ERR]\n");
        return;
    }

    // input
    printf("[SYN] message : ");
    read(0,new_buf,1024);
    memcpy(buf_msg,new_buf,strlen(new_buf)-1);
    free(new_buf);

    // check vuln ?
    if (memcmp(canary,global_canary,CANARY_SIZE)) {
        puts("[RST]");
    } else {
        puts("[ACK]");
    }
}

void menu_get() {
    char *buf = malloc(1024);
    char *endptr;
    printf("[ASK] secret value (ex: 0xf00db4b3) ? ");
    read(0, buf, 32);

    // Convert the hexadecimal string to a long integer
    if (strtoul(buf, &endptr, 16) != *(unsigned long*)global_canary) {
        printf("[RST]");
        exit(1);
    } else {
        int fd = open("secret_message.txt",O_RDONLY);memset(buf, 0, FLAGSIZE + 1);read(fd, buf, FLAGSIZE);close(fd);
        printf("[FIN]\n%s\n", buf);
        exit(0);
    }
}

void init() {
    // generate random
    srand(time(NULL));

    // set buffer
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    // zeroing
    memset(global_canary, 0, CANARY_SIZE);
    memset(canary, 0, CANARY_SIZE);
    memset(buf_msg, 0, BUFSIZE);

    // alarm exit for 5min
    alarm(300);
}


int main() {
    init();
    read_canary();
    char buf[64];
    
    puts(" __     __         _                      _____                 _   _ ");
    puts(" \\ \\   / /        | |                    / ____|               | | | |");
    puts("  \\ \\_/ /__  _   _| | _____  ___  ___   | |  __ _   _  ___  ___| |_| |");
    puts("   \\   / _ \\| | | | |/ / _ \\/ __|/ _ \\  | | |_ | | | |/ _ \\/ __| __| |");
    puts("    | | (_) | |_| |   < (_) \\__ \\ (_) | | |__| | |_| |  __/\\__ \\ |_|_|");
    puts("    |_|\\___/ \\__,_|_|\\_\\___/|___/\\___/   \\_____|\\__,_|\\___||___/\\__(_)");
    puts("                                                                      ");
    printf("  this is demo version, the default key is \"%s\"\n", secret_society_key);
    printf("");

    if (first_check()) {
        while (1) {
            menu_help();
            printf("> ");read(0, buf, 32);

            // menu
            if (strncmp("MSG", buf, 3) == 0) {
                seed = (rand()*(unsigned long)(*(unsigned long*)secret_society_key));
                menu_msg();
            } else if (strncmp("GET", buf, 3) == 0) {
                menu_get();
            } else if (strncmp("QUIT", buf, 4) == 0) {
                puts("[EOL]");
                break;
            }
        }
    } else {
        puts("\n[RST]");
    }
    return 0;
}