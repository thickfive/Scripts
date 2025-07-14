import time
import datetime

def print_time():
    index = 0
    while True:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        index += 1
        print(index, current_time, flush=True)
        time.sleep(1)

if __name__ == "__main__":
    print_time()

# 1. 后台运行, 同时输出到控制台和文件
# $ nohup python3 nohup.py 2>&1 | tee nohup.log &
# 2. 跟踪文件变化
# $ tail -f nohup.log
# 3. 查找进程, 可能会出现多条结果(包括查找命名本身)
# $ ps aux | grep "nohup.py"
# 4. 结束进程
# $ kill <PID>
#
# MacOS 下关闭控制台 nohup 程序依然会退出, 使用 disown 或者 screen 等方式来实现
#
# disown 不支持重连
# 1. $ nohup python3 nohup.py 2>&1 | tee nohup.log & disown
# 2. $ kill <PID>
#
# screen 支持重连
# 1. $ screen                                   // 开启 screen 子进程
# 2. $ python3 nohup.py 2>&1 | tee nohup.log    // 执行命令后可以关闭控制台在后台运行
# 2. $ screen -r 或者 screen -r -d <PID>        // 恢复 screen 子进程
# 3. $ Ctrl+C                                  // 结束命令
# 4. $ exit                                    // 退出 screen