const Kuroshiro = require('kuroshiro').default;
const KuromojiAnalyzer = require("kuroshiro-analyzer-kuromoji");

const kuroshiro = new Kuroshiro();
const analyzer = new KuromojiAnalyzer();

async function _toHiragana(string) {
    let kana = await kuroshiro.convert(string, {mode:"normal", to: "hiragana"});
    return Kuroshiro.Util.kanaToHiragna(kana)
}

async function toHiragana(string) {
    if (kuroshiro._analyzer == null) {
        await kuroshiro.init(analyzer) // 必须初始化完成后才能转换
    }
    return await _toHiragana(string)
}

// (async function test() {
//     let string = "アイスランド"
//     let result = await toHiragana(string)
//     console.log(string, result)

//     let startCode = 0x3041
//     let endCode = 0x30a1
//     for (let i = startCode; i < endCode; i++) {
//         let char = String.fromCharCode(i)
//         let romaji = Kuroshiro.Util.kanaToRomaji(char, 'nippon')
//         console.log(i.toString(16), char, romaji)
//     }
// })()

function groupByJapaneseSyllables(index) {
    let chars = [
        'ぁ', // 3041 ぁ a, 3042 あ a
        'か', // 304b か ka, 304c が ga
        'さ', // 3055 さ sa, 3056 ざ za
        'た', // 305f た ta, 3060 だ da
        'な', // 306a な na
        'は', // 306f は ha, 3070 ば ba
        'ま', // 307e ま ma
        'ゃ', // 3083 ゃ ya, 3084 や ya
        'ら', // 3089 ら ra
        'ゎ', // 308e ゎ wa, 308f わ wa
        'わ', // 放在结尾方便计算
    ]
    let charCode = index.charCodeAt(0)
    for (let i = 0; i < 10; i++) {
        let startCode = chars[i].charCodeAt(0)
        let endCode = chars[i + 1].charCodeAt(0)
        if (charCode >= startCode && charCode < endCode) {
            return String.fromCharCode(startCode)
        }
    }
    return index
}

// exports
module.exports = { 
    toHiragana,
    groupByJapaneseSyllables
}