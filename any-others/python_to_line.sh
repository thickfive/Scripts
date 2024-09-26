#!/bin/bash

# 简介: 将脚本文件中的反斜杠、空格(因为Python对缩进敏感)、单引号、换行符替换为转义字符, 输出单行字符串, 便于 echo -e 'single\nline\nstring' > mutiline.file 还原成多行文本
# 用法: python_to_line.sh input [output]
# 说明:
# 	1. sed 's/\\/\\\0134/g' 替换反斜杠 `\` 为 \0134
#   2. sed 's/ /\\\0040/g' 替换空格 ` ` 为 \0040
# 	3. sed "s/\'/\\\0047/g" 替换单引号 `'` 为 \0047
# 	4. sed -e ':a' -e 'N' -e '$!ba' -e 's/\n/\\n/g' 将所有字符读取为一行, 替换换行符为 \n
# 参考: https://stackoverflow.com/questions/1251999/how-can-i-replace-a-newline-n-using-sed

output=$(cat $1 | sed 's/\\/\\\0134/g' | sed 's/ /\\\0040/g' | sed "s/\'/\\\0047/g" | sed -e ':a' -e 'N' -e '$!ba' -e 's/\n/\\n/g')
path=$2
if [ "$path" == '' ]
then
	path="$0.log"
	echo "$(date '+%Y-%m-%d %H:%M:%S') $1" >> $path
	echo $output >> $path
	echo '' >> $path
else
	echo $output > $path
fi
echo $output