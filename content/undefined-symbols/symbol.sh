#!/bin/bash
#
# 扫描指定 framework 二进制文件中包含的符号
# $ bash symbol.sh <file> <arch> <symbol>

FRAMEWORK_PATH=$(dirname "$1")
FRAMEWORK=$(basename "$1")
ARCH=$2
SYMBOL=$3
ARCH_TEMP="$FRAMEWORK-$ARCH-temp"

echo "文件夹路径：$FRAMEWORK_PATH"
echo "文件名：$FRAMEWORK"

if [[ $SYMBOL == "" ]]; then
    cat <<EOF
========
❌ 参数错误: $ bash symbol.sh <file> <arch> <symbol>
⭐️ 如果出错了, 可以尝试下列命令, 输出符号到文件后再查找
$ nm -gC $FRAMEWORK_PATH/$FRAMEWORK > symbols.txt
$ cat symbols.txt | grep $SYMBOL
========
EOF
    exit
fi

cd "$FRAMEWORK_PATH"

echo "1. lipo -info $FRAMEWORK:"
# 如果包含多个架构, 需要先分离
if [[ $(lipo -info $FRAMEWORK) =~ "Non-fat file" ]]; then
    echo "2. mkdir $ARCH_TEMP:"
    mkdir $ARCH_TEMP
    echo "3. cp $FRAMEWORK $ARCH_TEMP/$FRAMEWORK"
    cp $FRAMEWORK $ARCH_TEMP/$FRAMEWORK
else
    echo "2. mkdir $ARCH_TEMP:"
    mkdir $ARCH_TEMP
    echo "3. lipo $FRAMEWORK -thin $ARCH -output $ARCH_TEMP/$FRAMEWORK:"
    lipo $FRAMEWORK -thin $ARCH -output $ARCH_TEMP/$FRAMEWORK
fi

cd $ARCH_TEMP
echo "4. nm -gC $FRAMEWORK | grep $SYMBOL:"
# nm -gC $FRAMEWORK | grep $SYMBOL

# 分离目标文件
ar xv $FRAMEWORK
SYMBOLS="========\n这些文件中包含 symbol: $SYMBOL\n"
for file in $(ls); do
    RES="$(nm -gC $file | grep $SYMBOL)"
    if [[ $RES =~ $SYMBOL ]]; then
        SYMBOLS="$SYMBOLS ⭐️ $file:\n$RES\n"
    fi
done
SYMBOLS="$SYMBOLS========"
echo -e "$SYMBOLS"

# 清理目标文件
if [[ $4 == "" ]]; then
echo "清理临时文件夹 $ARCH_TEMP?  y/n:"
read -n 1 char
echo -e "\n开始清理... (如果需要保留, 请手动复制)"
fi
rm -d -r ../$ARCH_TEMP