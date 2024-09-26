#include "undefine.h"
#include <stdio.h>

void test_undefined_symbol(void) {
    printf("========== 1 undefined_symbol_imp >>\n");
    undefined_symbol_imp();
    printf("========== 2 undefined_symbol_imp <<\n");
}