#!/bin/bash
#
# [【Linux 】向Shell脚本传递参数、getopts、getopt](https://blog.csdn.net/m0_45406092/article/details/133276390)
# [shell 命令行参数（getopt和getopts）](https://www.cnblogs.com/cangqinglang/p/11943661.html)
# [Shell其实很简单（30）使用getopt处理参数](https://www.bilibili.com/video/BV19D421K7Yv/?spm_id_from=333.337.search-card.all.click&vd_source=659d8096ba4cc734f6ab09201a3b4d92)

# echo "=========="
# echo "当前脚本名称: $0"
# echo "参数个数: $#"
# echo "第1个参数: $1"
# echo "第2个参数: $2"
# echo "参数(*)...: $*"
# echo "参数(@)...: $@"
# echo "最后一个参数: $_"
# echo "=========="

# getopts 格式化参数, 很容易获取参数选项与参数值, 只支持单个字符, 不支持长选项
# while getopts  "abc:d" ARG; do
#     echo "ARG=[$ARG], OPTIND=[$OPTIND] OPTARG=[$OPTARG]"
# done

# Mac 版本的 getopt 与 gun-getopt 实现不一样, 整理参数, 具体逻辑需要自己实现
# set -- 清空参数, nu-getopt 参数尾部自动添加 -- 并将多余参数移动到 -- 之后
set -- $(gnu-getopt -o a:n: -l age:,name: -- "$@") 
echo "gnu-getopt 整理过后的参数: $@"
while true; do
    case "$1" in
        -a|--age)
            echo "-a, --age: $2"
            shift 2;; # 去掉前 n 个参数
        -n|--name)
            echo "-n, --name: $2"
            shift 2;;
        --)
            break;;
        *)
            echo "非法选项"
            exit 1;;
    esac
done