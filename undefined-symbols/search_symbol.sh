#!/bin/bash
#
# 全局扫描包含指定符号的静态库/动态库
# $ bash search_symbol.sh <path> <symbol>

SEARCH_PATH=$1
SYMBOL=$2

if [[ $SYMBOL == "" ]]; then
    cat <<EOF
========
❌ 参数错误: $ bash search_symbol.sh <path> <symbol>
========
EOF
    exit
fi

SYMBOLS="========\n这些文件中包含 symbol: $SYMBOL\n"

function search_a() {
    for FRAMEWORK_PATH in $(find $SEARCH_PATH -name "*.a"); do
        RES="$(nm -gC $FRAMEWORK_PATH | grep $SYMBOL)"
        if [[ $RES =~ $SYMBOL ]]; then
            SYMBOLS="$SYMBOLS ⭐️ $FRAMEWORK_PATH\n"
        fi
    done
}

function search_framework() {
    for FRAMEWORK_PATH in $(find $SEARCH_PATH -name "*.framework"); do
        FRAMEWORK=$(echo $FRAMEWORK_PATH | xargs  -I {} basename {} | cut -d'.' -f1)
        RES="$(nm -gC $FRAMEWORK_PATH/$FRAMEWORK | grep $SYMBOL)"
        if [[ $RES =~ $SYMBOL ]]; then
            SYMBOLS="$SYMBOLS ⭐️ $FRAMEWORK_PATH\n"
        fi
    done
}

search_a
search_framework

SYMBOLS="$SYMBOLS========"
echo -e "$SYMBOLS"