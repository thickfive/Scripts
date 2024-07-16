// 下载
// curl https://raw.githubusercontent.com/umpirsky/country-list/master/data/en/country.json > ./input/country-en.json

const process = require('child_process')

const countryCodes = [
    "de", // 德语
    "ru", // 俄语
    "fr", // 法语
    "ko", // 韩语
    "pt", // 葡萄牙语
    "ja", // 日语
    "es", // 西班牙语
    "it", // 意大利语
    "en", // 英语
    "zh", // 汉语  
]

// 下载国家地区编码文件. 如果下载失败, 检查 countryCode 是否正确. 如果是网络连接失败导致的, 需要更改代理节点
function download() {
    console.log('download country jsons ...')
    for (let i = 0; i < countryCodes.length; i++) {
        let countryCode = countryCodes[i]
        let cmd = `curl https://raw.githubusercontent.com/umpirsky/country-list/master/data/${countryCode}/country.json > ./input/country-${countryCode}.json`
        console.log("\n>", cmd)
        process.execSync(cmd)
    }
}

download()