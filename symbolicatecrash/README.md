# 如何通过符号表 dSYM 还原崩溃日志

## 1. 使用 `symbolicatecrash` 脚本

### 复制符号表文件 `*.app.dSYM`
`$ mv '/Users/vvii/Library/Developer/Xcode/DerivedData/Mixed-anhmchznhipngeategvzzzshrbuh/Build/Products/Debug-iphoneos/Mixed.app.dSYM' Mixed.app.dSYM`

### 脚本1
`$ ./symbolicatecrash apple.crash Mixed.app.dSYM > symbolicated.log`
- 错误处理 - Error: "DEVELOPER_DIR" is not defined at ./symbolicatecrash line 69. 
- `$ export DEVELOPER_DIR="/Applications/Xcode.app/Contents/Developer"`

### 脚本2 (系统自带)
`$ /Applications/Xcode.app/Contents/SharedFrameworks/DVTFoundation.framework/Versions/A/Resources/symbolicatecrash apple.crash Mixed.app.dSYM > symbolicated.log`  
作用完全一样, 上面的脚本本来就是从系统里面复制出来的


## 2. 手动计算崩溃地址

### 输出 dSYM 文件信息
`$ dwarfdump --debug-info Mixed.app.dSYM | less > dSYM.info`

### 以下面崩溃日志文件为例, 进行计算
```
...
Thread 0 Crashed:
0   libswiftCore.dylib                0x0000000181585ac4 0x18154d000 + 232132
1   libswiftCore.dylib                0x0000000181585ac4 0x18154d000 + 232132
2   libswiftCore.dylib                0x0000000181585828 0x18154d000 + 231464
3   libswiftCore.dylib                0x0000000181585630 0x18154d000 + 230960
4   libswiftCore.dylib                0x0000000181585188 0x18154d000 + 229768
5   Mixed                             0x0000000104e806ac `0x104df8000` + 558764 
6   Mixed                             0x0000000104e8052c 0x104df8000 + 558380
7   Mixed                             0x0000000104e8038c 0x104df8000 + 557964
8   Mixed                             0x0000000104e2fb88 0x104df8000 + 228232
9   UIKitCore                         0x0000000189ce990c 0x1898bd000 + 4376844
...
Binary Images:
`0x104df8000` - 0x105ea7fff Mixed arm64  <f1e12872a1bb3a6d8b36586ec76bfc50> /private/var/containers/Bundle/Application/240A978B-AF03-4BEC-8916-BA4361AE3358/Mixed.app/Mixed
0x1072e4000 - 0x1072effff libobjc-trampolines.dylib arm64e  <3eb26cf9922139f583d40c8ae83d3424> /private/preboot/Cryptexes/OS/usr/lib/libobjc-trampolines.dylib
...
```

可以看到:  
实际崩溃地址 = 实际基地址 + 偏移（0x0000000104e806ac = 0x104df8000 + 558764，这里 558764 转成 16 进制为 0x886AC）  
理论崩溃地址 = 默认基地址 0x100000000 + 偏移 (0x100000000 + 558764 => 0x100000000 + 0x886AC => 0x1000886AC)   

可以从 `dSYM.info` 文件中手动查找这个理论崩溃地址, DW_AT_low_pc 与 DW_AT_high_pc 区间内包含这个地址的就是对应的函数或者文件  
也可以使用下面的命令:  
`$ dwarfdump --lookup 0x1000886AC --arch arm64 Mixed.app.dSYM` 

显而易见 0x1000886AC 正好在所有的 DW_AT_low_pc 与 DW_AT_high_pc 之间, 那么就算出它位于哪个文件第几行的哪个函数了

⭐️ 通过这个方法得到的信息比 `symbolicatecrash` 脚本更加详细准确，
```
~/Desktop/OpenSource/Scripts/symbolicatecrash $ dwarfdump --lookup 0x1000886AC --arch arm64 Mixed.app.dSYM

Mixed.app.dSYM/Contents/Resources/DWARF/Mixed:  file format Mach-O arm64
0x0020f0d2: Compile Unit: length = 0x00000699, format = DWARF32, version = 0x0004, abbr_offset = 0x0000, addr_size = 0x08 (next unit at 0x0020f76f)

0x0020f0dd: DW_TAG_compile_unit
              DW_AT_producer    ("Apple Swift version 5.9.2 (swiftlang-5.9.2.2.56 clang-1500.1.0.2.5)")
              DW_AT_language    (DW_LANG_Swift)
              DW_AT_name        ("/Users/vvii/Desktop/Project/Mixed/Mixed/Classes/CrashViewController.swift")
              DW_AT_LLVM_sysroot        ("/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.sdk")
              DW_AT_APPLE_sdk   ("iPhoneOS17.2.sdk")
              DW_AT_stmt_list   (0x000633e6)
              DW_AT_comp_dir    ("/Users/vvii/Desktop/Project/Mixed")
              DW_AT_APPLE_major_runtime_vers    (0x05)
              DW_AT_low_pc      (0x0000000100087f2c)
              DW_AT_high_pc     (0x0000000100088b4c)

0x0020f226:   DW_TAG_subprogram
                DW_AT_low_pc    (0x0000000100088538)
                DW_AT_high_pc   (0x000000010008870c)
                DW_AT_frame_base        (DW_OP_reg29 W29)
                DW_AT_linkage_name      ("$s5Mixed19CrashViewControllerC12crashTest002yyF")
                DW_AT_name      ("crashTest002")
                DW_AT_decl_file ("/Users/vvii/Desktop/Project/Mixed/Mixed/Classes/CrashViewController.swift")
                DW_AT_decl_line (32)
                DW_AT_type      (0x0020f74a "$sytD")
                DW_AT_external  (true)

0x0020f253:     DW_TAG_lexical_block
                  DW_AT_low_pc  (0x0000000100088644)
                  DW_AT_high_pc (0x000000010008870c)
```
