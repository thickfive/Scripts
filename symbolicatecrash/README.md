## 使用方式
``` shell
$ ./symbolicatecrash Test.crash Test.app.dSYM > result.crash
```

## 错误处理
- Error: "DEVELOPER_DIR" is not defined at ./symbolicatecrash line 69. 
``` shell
$ export DEVELOPER_DIR="/Applications/Xcode.app/Contents/Developer"
```