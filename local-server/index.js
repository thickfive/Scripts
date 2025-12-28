const os = require('os')
const fs = require('fs')
const path = require('path')
const express = require('express')
const bodyParser = require('body-parser')
const multer = require('multer')
const { randomInt, randomUUID } = require('crypto')
const app = express()

app.use(function (req, res, next) {
    let uuid = randomUUID()
    console.log(`------------------------- ${uuid} -------------------------`)
    console.log(new Date(), req.method, req.url, req.headers, req.body)
    next()
    console.log(`------------------------- ${uuid} -------------------------`)
})

let options = {
    limit: '1024mb', // bodyParser.raw 默认 100kb
    type: (req) => {
        return true // bodyParser.raw 默认 content-type = application/octet-stream, 自定义 type 解除限制
    }
}

// ...handlers, 可以同时使用多个 handlers
app.post('/stream', bodyParser.raw(options), function (req, res, next) {
    console.log('/stream')
    fs.writeFile('temp.txt', req.body, (err) => {
        console.log(err ?? 'ok')
    })
    res.status(200)
    res.json({"msg": "ok"})
})

// ...handlers, 可以同时使用多个 handlers
app.post('/uploadLog', bodyParser.raw(options), function (req, res, next) {
    fs.writeFile('xlog/temp.xlog', req.body, (err) => {
        console.log(err ?? 'ok')
    })
    res.status(200)
    res.json({"msg": "ok"})
})

app.post('/uploadCrash', multer({dest: 'crash/cache'}).single('reports'), function (req, res, next) {
    fs.readFile(req.file.path, (err, data) => {
        let crashes = JSON.parse(String(data))
        for (let i = 0; i < crashes.length; i++) {
            console.log("\n==================== crash info >>>>>>>>>>>>>>>>>>>>")
            let crash = crashes[i]
            if (typeof crash == 'object') { // json 格式
                for (let i = 0; i < crash.binary_images.length; i++) {
                    let image = crash.binary_images[i]
                    if (image.crash_info_message) {
                        console.log(`crash image: ${image.name}`)
                        console.log(`crash info message: ${image.crash_info_message}\n`)
                    }
                }
                for (let i = 0; i < crash.crash.threads.length; i++) {
                    let thread = crash.crash.threads[i]
                    console.log(`thread: ${thread.index}, crashed: ${thread.crashed}`)
                    for (let i = 0; i < thread.backtrace.contents.length; i++) {
                        let content = thread.backtrace.contents[i]
                        let image_addr = content.object_addr ? `0x${content.object_addr.toString(16)}` : undefined
                        let image_name = content.object_name ? content.object_name.padEnd(40, ' ') : undefined
                        let symbol_addr = content.symbol_addr ? `0x${content.symbol_addr.toString(16)}` : undefined
                        let symbol_name = content.symbol_name
                        let offset = `+${content.instruction_addr - content.symbol_addr}` // 指的是当前指令地址相对函数起始地址的偏移值
                        console.log(image_addr, image_name, symbol_addr, symbol_name, offset)
                    }
                    console.log(`-------------------- thread: ${thread.index} --------------------\n`)
                }
            } else if (typeof crash == 'string') { // apple 格式
                fs.writeFile('apple.crash', crash, (err) => {
                    console.log(` ${crash.length} > apple.crash, error: ${err}`)
                })
            }
            console.log("==================== crash info <<<<<<<<<<<<<<<<<<<<\n")
        }
    })
    res.status(200)
    res.json({"msg": "ok"})
})

app.use('/test', function (req, res, next) {
    res.status(200)
    let data = fs.readFileSync("./response.json")
    setTimeout(() => {
        res.send(data)
    }, 1000)
    console.log(String(data))
})

app.use('/test2', (req, res) => {
    res.status(200)
    // 必须设置这些头，让浏览器知道是分块传输
    res.set({
        'Content-Type': 'text/plain; charset=utf-8',
        'Transfer-Encoding': 'chunked',  // 关键：启用 chunked
        'Cache-Control': 'no-cache',
    });
    setTimeout(() => {
        // let timeoutIntervalForRequest = 15 // 表示每一次 write 间隔不能超过 15s
        // let timeoutIntervalForResource = 60 // 总超时时间, 从请求开始到结束不能超过 60s
        // 先发送第一部分
        res.write('Hello');
        res.write(' ');
        setTimeout(() => {
            // 再发送第二部分
            res.write('World');
            res.end();  // 必须调用 end() 结束响应
        }, 16 * 1000);
    }, 14 * 1000);
})

app.use('/video', function (req, res, next) {
    let video_dir = path.resolve(__dirname, 'public', 'video')
    let video_path = video_dir + req.url
    let buffer = fs.readFileSync(video_path)

    let range = (req.header('range') || "").replace('bytes=', '').split('-')
    let start = parseInt(range[0] || 0)
    let end = parseInt(range[1] || buffer.length - 1)

    // 限制 100K (AVPlayer 不支持请求的 range 与响应不一致, ijkplayer 支持并且视频播放需要的缓冲时间比 AVPlayer 短)
    if (start < end - 1024 * 100) {
        end = start + 1024 * 100 - 1
    }

    res.status(206)                                  // 可选
    res.header('Accept-Ranges', 'bytes')             // 可选
    res.header('Content-Length', end - start + 1)    // 可选
    res.header('Content-Range', `bytes ${start}-${end}/${buffer.length}`)   // 必须 // 以 Apple 为例, 第一次请求 0-1 响应 Content-Range: bytes 0-1/24517104, 就能知道完整视频长度
    res.header('Content-Type', 'video/mp4')          // 可选

    let data = buffer.subarray(start, end + 1)
    // 模拟延时
    let scale = start / (1024 * 100) % 10
    let delay = (scale > 8) ? 1000 : 500
    setTimeout(() => {
        if (start > 0 && randomInt(100) < 1) {
            res.send() // 模拟失败
            console.log(`❌ ${delay}ms`, req.url, res.statusCode, req.header('range'), start, end)
        } else {
            res.send(data)
            console.log(`✅ ${delay}ms`, req.url, res.statusCode, req.header('range'), start, end)
        }
    }, delay)
})

app.use(express.static('public'))

function getLocalIP() {
    const interfaces = os.networkInterfaces();
    for (let devName in interfaces) {
        const iface = interfaces[devName];
        for (let i = 0; i < iface.length; i++) {
            const alias = iface[i];
            // 筛选条件：IPv4、非回环地址、且是有效的地址
            if (alias.family === 'IPv4' && alias.address !== '127.0.0.1' && !alias.internal) {
                return alias.address;
            }
        }
    }
}

app.listen(8000, () => {
    const localhost = getLocalIP() || "127.0.0.1"
    console.log(`express server running at: ${localhost}:8000`)
})



