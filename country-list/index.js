const fs = require('fs');
const { localizeTransform, localizeSectionIndex } = require('./localize/localize');
// const path = require('path');

const countryCode = "ja"    // 语言编码

const path1 = './input/calling.json'                    // 模版
const path2 = `./input/country-${countryCode}.json`     // 国家地区编码
const path3 = `./output/country-${countryCode}.json`    // 输出

async function readFile(path) {
   return new Promise((resolve, reject) => {
        fs.readFile(path, 'utf8', (err, data) => {
            if (err) {
                reject(err)
            } else {
                resolve(data)
            }
        })
   })
}

async function writeFile(path, data) {
    return new Promise((resolve, reject) => {
         fs.writeFile(path, data, (err) => {
            if (err) {
                reject(err)
            } else {
                resolve()
            }
         })
    })
 }

async function readJSON(path) {
    return readFile(path).then(res => JSON.parse(res))
}

async function writeJSON(path, data) {
    await writeFile(path, JSON.stringify(data, undefined, 2))
}

//  Item:
//  {
//     regionName: 'Ascension Island',
//     callingCode: '+247',
//     regionCode: 'AC',
//     regionFlag: '🇦🇨',
//     regionSyllables: []
//  }
//
// 匹配
function mapByCountryCode(list, map) {
    // 如果路径相同, 不需要匹配
    if (path1 == path2) {
        return list
    }
    // console.log(list, map)
    for (let i = 0; i < list.length; i++) {
        let item = list[i]
        if (map[item.regionCode] == undefined) {
            console.log(`region code not found: ${item.regionCode}`)
        } else {
            item.regionName = map[item.regionCode]
        }
        list[i] = item
    }
    return list
}

// 分组 & 排序
async function groupByCountryName(list) {
    // 分组 {"A": [...], "B": [...]}
    let dict = {}
    for (let i = 0; i < list.length; i++) {
        let item = list[i]
        // 转换音标
        let syllables = await localizeTransform(item.regionName, countryCode)
        // 设置分组索引
        item.index = localizeSectionIndex(syllables, countryCode)
        item.syllables = syllables
        // 分组
        let key = item.index
        if (dict[key] == undefined) {
            dict[key] = []
        }
        dict[key].push(item)
    }
    // 组内排序 
    let sections = []
    for (let key in dict) {
        let section = dict[key]
        section.sort(function (a, b) {
            if (a.syllables < b.syllables) {
                return -1
            } else if (a.syllables == b.syllables) {
                return 0
            } else {
                return 1
            }
        })
        sections.push({
            "index": key,
            "items": section
        })
    }
    // 索引排序 [{"index": "A", "items": [...]}, ...]
    sections.sort(function (a, b) {
        if (a.index < b.index) {
            return -1
        } else if (a.index == b.index) {
            return 0
        } else {
            return 1
        }
    })
    console.log("section indexs:", sections.map(res => { return res.index }))
    return sections
}

// 入口
async function main() {
    let list = await readJSON(path1)
    let map = await readJSON(path2)
    let res1 = mapByCountryCode(list, map)
    let res2 = await groupByCountryName(res1)
    await writeJSON(path3, res2)
}

main()