
/*
😄 /video-no-faststart.mp4 206 bytes=0-1 0 1
😄 /video-no-faststart.mp4 206 bytes=0-2596403 0 102399
😄 /video-no-faststart.mp4 206 bytes=2572288-2596403 2572288 2596403        // 👻 封面就绪
😄 /video-no-faststart.mp4 206 bytes=102400-2572287 102400 204799
😄 /video-no-faststart.mp4 206 bytes=204800-2572287 204800 307199
😄 /video-no-faststart.mp4 206 bytes=307200-2572287 307200 409599
😄 /video-no-faststart.mp4 206 bytes=409600-2572287 409600 511999
😄 /video-no-faststart.mp4 206 bytes=512000-2572287 512000 614399
😄 /video-no-faststart.mp4 206 bytes=614400-2572287 614400 716799
😄 /video-no-faststart.mp4 206 bytes=716800-2572287 716800 819199
😄 /video-no-faststart.mp4 206 bytes=819200-2572287 819200 921599
😄 /video-no-faststart.mp4 206 bytes=921600-2572287 921600 1023999
😄 /video-no-faststart.mp4 206 bytes=1024000-2572287 1024000 1126399
😄 /video-no-faststart.mp4 206 bytes=1126400-2572287 1126400 1228799
😄 /video-no-faststart.mp4 206 bytes=1228800-2572287 1228800 1331199
😄 /video-no-faststart.mp4 206 bytes=1331200-2572287 1331200 1433599
😄 /video-no-faststart.mp4 206 bytes=1433600-2572287 1433600 1535999
😄 /video-no-faststart.mp4 206 bytes=1536000-2572287 1536000 1638399
😄 /video-no-faststart.mp4 206 bytes=1638400-2572287 1638400 1740799
😄 /video-no-faststart.mp4 206 bytes=1740800-2572287 1740800 1843199
😄 /video-no-faststart.mp4 206 bytes=1843200-2572287 1843200 1945599
😄 /video-no-faststart.mp4 206 bytes=1945600-2572287 1945600 2047999
😄 /video-no-faststart.mp4 206 bytes=2048000-2572287 2048000 2150399
😄 /video-no-faststart.mp4 206 bytes=2150400-2572287 2150400 2252799
😄 /video-no-faststart.mp4 206 bytes=2252800-2572287 2252800 2355199
😄 /video-no-faststart.mp4 206 bytes=2355200-2572287 2355200 2457599
😄 /video-no-faststart.mp4 206 bytes=2457600-2572287 2457600 2559999
😄 /video-no-faststart.mp4 206 bytes=2560000-2572287 2560000 2572287
*/

/*
😄 /video-faststart.mp4 206 bytes=0-1 0 1
😄 /video-faststart.mp4 206 bytes=0-2588576 0 102399                        // 👻 封面就绪
😄 /video-faststart.mp4 206 bytes=102400-2588576 102400 204799
😄 /video-faststart.mp4 206 bytes=204800-2588576 204800 307199
😄 /video-faststart.mp4 206 bytes=307200-2588576 307200 409599
😄 /video-faststart.mp4 206 bytes=409600-2588576 409600 511999
😄 /video-faststart.mp4 206 bytes=512000-2588576 512000 614399
😄 /video-faststart.mp4 206 bytes=614400-2588576 614400 716799
😄 /video-faststart.mp4 206 bytes=716800-2588576 716800 819199
😄 /video-faststart.mp4 206 bytes=819200-2588576 819200 921599
😄 /video-faststart.mp4 206 bytes=921600-2588576 921600 1023999
😄 /video-faststart.mp4 206 bytes=1024000-2588576 1024000 1126399
😄 /video-faststart.mp4 206 bytes=1126400-2588576 1126400 1228799
😄 /video-faststart.mp4 206 bytes=1228800-2588576 1228800 1331199
😄 /video-faststart.mp4 206 bytes=1331200-2588576 1331200 1433599
😄 /video-faststart.mp4 206 bytes=1433600-2588576 1433600 1535999
😄 /video-faststart.mp4 206 bytes=1536000-2588576 1536000 1638399
😄 /video-faststart.mp4 206 bytes=1638400-2588576 1638400 1740799
😄 /video-faststart.mp4 206 bytes=1687552-1703935 1687552 1703935
😄 /video-faststart.mp4 206 bytes=1740800-2588576 1740800 1843199
😄 /video-faststart.mp4 206 bytes=1843200-2588576 1843200 1945599
😄 /video-faststart.mp4 206 bytes=1945600-2588576 1945600 2047999
😄 /video-faststart.mp4 206 bytes=2031616-2047999 2031616 2047999
😄 /video-faststart.mp4 206 bytes=2048000-2588576 2048000 2150399
😄 /video-faststart.mp4 206 bytes=2129920-2146303 2129920 2146303
😄 /video-faststart.mp4 206 bytes=2150400-2588576 2150400 2252799
😄 /video-faststart.mp4 206 bytes=2244608-2260991 2244608 2260991
😄 /video-faststart.mp4 206 bytes=2260992-2588576 2260992 2363391
😄 /video-faststart.mp4 206 bytes=2342912-2359295 2342912 2359295
😄 /video-faststart.mp4 206 bytes=2363392-2588576 2363392 2465791
😄 /video-faststart.mp4 206 bytes=2441216-2457599 2441216 2457599
😄 /video-faststart.mp4 206 bytes=2465792-2588576 2465792 2568191
😄 /video-faststart.mp4 206 bytes=2568192-2588576 2568192 2588576
*/

// 显而易见, video-no-faststart.mp4 与 video-faststart.mp4 的请求方式有所差异 
// 1. 封面就绪, 需要加载开头或者结尾的关键数据 moov
// 2. 开始播放, Safari 需要缓冲一段时间, 10s 左右, Chrome 则不需要
// 3. 中间部分请求错误, Chrome 大约 3s 后主动重试, Safari 几乎不能恢复, 点击暂停播放没有反应, 而是需要手动修改播放时间才能触发重新下载
// 4. iOS AVPlayer 好像不支持响应 Content-Range 和请求 Range 不一致 😒 (failed strict content length check). 但是 WKWebView 可以支持
// 5. iOS 开发者模式限制网速后可以看到如下请求列表, 可以看到前几次会一直请求到剩余的完整范围, 但是由于网速不够, 后续调整了请求范围的大小 
// 总结: iOS 视频加载策略为 0-1 检测是否为视频, 尝试(多次)请求完整视频, 最后是多个离散不连续的分片. 总之 iOS 上的体验极差

/*
✅ 100ms /video-faststart.mp4 206 bytes=0-1 0 1
✅ 100ms /video-faststart.mp4 206 bytes=0-2588576 0 2588576                 // 👻 完整请求
✅ 100ms /video-faststart.mp4 206 bytes=34455-2588576 34455 2588576
✅ 100ms /video-faststart.mp4 206 bytes=589824-606207 589824 606207
✅ 500ms /video-faststart.mp4 206 bytes=933888-950271 933888 950271
✅ 100ms /video-faststart.mp4 206 bytes=1130496-1146879 1130496 1146879
✅ 100ms /video-faststart.mp4 206 bytes=1294336-1310719 1294336 1310719
✅ 100ms /video-faststart.mp4 206 bytes=1392640-1409023 1392640 1409023
✅ 100ms /video-faststart.mp4 206 bytes=1490944-1507327 1490944 1507327
✅ 100ms /video-faststart.mp4 206 bytes=1589248-1605631 1589248 1605631
✅ 100ms /video-faststart.mp4 206 bytes=1687552-1703935 1687552 1703935
✅ 100ms /video-faststart.mp4 206 bytes=1769472-1785855 1769472 1785855
✅ 500ms /video-faststart.mp4 206 bytes=1851392-1867775 1851392 1867775
✅ 500ms /video-faststart.mp4 206 bytes=2031616-2047999 2031616 2047999
✅ 100ms /video-faststart.mp4 206 bytes=2129920-2146303 2129920 2146303
✅ 100ms /video-faststart.mp4 206 bytes=2244608-2260991 2244608 2260991
✅ 100ms /video-faststart.mp4 206 bytes=2342912-2359295 2342912 2359295
✅ 100ms /video-faststart.mp4 206 bytes=2441216-2457599 2441216 2457599
*/
function clickAction() {
    // fetch('/test').then(res => {
    //     console.log(res)
    // }).catch(err => {
    //     console.log(err)
    // })
    // let video = document.querySelector('video')
    // video.src = './video/video-no-faststart.mp4'
    // if (video.paused) {
    //     video.play()
    // } else {
    //     video.currentTime = 10
    // }
    // console.log("video.currentTime", video.currentTime)

    fetch('/uploadLog', {
        method: 'POST',
        headers: {
          "Content-type": "application/octet-stream",
        },
        body: JSON.stringify({"foo": "bar", "lorem": "ipsum"}),
    }).then(res => {
        console.log(res)
    }).catch(err => {
        console.log(err)
    })
}