#include <stdio.h>

#ifndef IMPORT_FROM_LIB
#define IMPORT_FROM_LIB 1
#endif

#if IMPORT_FROM_LIB
// C 语言引用 CocoaPod 编译出来的静态库 libexample.a, example.framework 和 动态库 dynamic.framework
//      => gcc main.c -I<头文件目录> -L<静态库目录> -l<静态库名称(不包含前缀 lib + 后缀 .a)>
// 1. 静态库 libexample.a
//      => gcc main.c -I./lib/example -Llib -lexample 
// 2. 静态库 example.framework
//  2.1 需要先做一个软连接, 符合上面的静态库名称格式
//      => ln -s example libexample.a 
//      => gcc main.c -I./lib/example.framework/Headers -Llib/example.framework -lexample
//  2.2 也可以通过直接链接文件具体路径的方式
//      => gcc main.c -I./lib/example.framework/Headers ./lib/example.framework/example
// 3. 动态库 dynamic.framework
//      => gcc main.c -I./lib/dynamic.framework/Headers ./lib/dynamic.framework/dynamic -rpath lib
#include <example.h> 
#else
#include "undefine.h"
// 第三方静态库存在 undefined symbols 加上设置 iOS 项目设置 -all_load 导致项目编译失败的原因:
// 第 1 步可以编译, 说明 .o 文件允许存在 undefined symbols
// 如果不实现 void undefined_symbol_imp(void), 第 2 步就编译不过, 说明可执行文件不允许 undefined symbols
void undefined_symbol_imp(void) {
    printf("1. gcc -c undefine.c -o undefine.o \n");
    printf("2. gcc main.c undefine.o \n");
    printf("3. ./a.out \n");
}
#endif

int main() {
    printf("Hello world!\n");
    test_undefined_symbol();
    return 0;
}