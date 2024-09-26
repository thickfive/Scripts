#include <stdio.h>
#include "undefine.h"

int main() {
    printf("Hello world!\n");
    test_undefined_symbol();
    return 0;
}

// 第三方静态库存在 undefined symbols 加上设置 iOS 项目设置 -all_load 导致项目编译失败的原因:
// 第 1 步可以编译, 说明 .o 文件允许存在 undefined symbols
// 如果不实现 void undefined_symbol_imp(void), 第 2 步就编译不过, 说明可执行文件不允许 undefined symbols
void undefined_symbol_imp(void) {
    printf("1. gcc -c undefine.c -o undefine.o \n");
    printf("2. gcc main.c undefine.o \n");
    printf("3. ./a.out \n");
}