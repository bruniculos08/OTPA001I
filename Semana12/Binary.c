#include "stdio.h"
#define BYTE2BINARY_FMT "%c%c%c%c%c%c%c%c"
#define BYTE2BINARY(byte) \
    (byte & 0x80 ? '1' : '0'), \
    (byte & 0x40 ? '1' : '0'), \
    (byte & 0x20 ? '1' : '0'), \
    (byte & 0x10 ? '1' : '0'), \
    (byte & 0x08 ? '1' : '0'), \
    (byte & 0x04 ? '1' : '0'), \
    (byte & 0x02 ? '1' : '0'), \
    (byte & 0x01 ? '1' : '0')

int main(void) {
    int number = 1;
    printf("0b"BYTE2BINARY_FMT"\n", BYTE2BINARY(number));
    printf("0b"BYTE2BINARY_FMT" "BYTE2BINARY_FMT"\n", BYTE2BINARY(number>>8), BYTE2BINARY(number));   
}