const http = require('http')
const url = require('url')
const path = require('path')
const {stat, readFile} = require('fs/promises')
const crypto = require('crypto')

http.createServer(async (req, res) => {
    let {pathname} = url.parse(req.url)
    filename = (pathname == "/") 
        ? path.join(__dirname, "public", pathname, "index.html")
        : path.join(__dirname, "public", pathname)
    console.log(filename)
    try {
        let statObj = await stat(filename)
        if (statObj.isFile()) {
            let file = await readFile(filename)
            // 强制缓存
            res.setHeader("Expires", new Date(new Date().getTime() + 1000 * 10).toGMTString())
            res.setHeader("Cache-Control", "max-age=10")
            // 协商缓存 1
            let ctime = statObj.ctime.toGMTString()
            res.setHeader("Last-Modified", ctime)
            if (req.headers["if-modified-since"] === ctime) {
                return (res.statusCode = 304) && res.end()
            }
            // 协商缓存 2
            let hash = crypto.createHash("md5").update(file).digest("base64")
            res.setHeader("ETag", hash)
            if (req.headers["if-none-match"] === hash) {
                return (res.statusCode = 304) && res.end()
            }
            res.statusCode = 200
            res.end(file)
        } else {
            res.statusCode = 404
            res.end("404 Not Found")
        }
    } catch (err) {
        // console.log(err)
        res.statusCode = 500
        res.end("500 Internal Server Error")
    }
}).listen(3000)