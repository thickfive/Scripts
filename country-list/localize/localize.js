const { toJamos } = require('./localize-ko');
const { toHiragana, groupByJapaneseSyllables } = require('./localize-ja');
const { toPinyin } = require('./localize-zh');

const map = {
    "ko": toJamos,
    "ja": toHiragana,
    "zh": toPinyin
}

async function localizeTransform(string, countryCode) {
    let transform = map[countryCode]
    if (transform == null) {
        return string
    } else {
        let result = await transform(string)
        console.log(`transform: ${string} => ${result}`)
        return result
    }
}

function localizeSectionIndex(syllables, countryCode) {
    let index = syllables.substring(0, 1).toUpperCase()
    if (countryCode == "ja") {
        return groupByJapaneseSyllables(index)
    } else {
        return index.normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    }
}

module.exports = { 
    localizeTransform,
    localizeSectionIndex
}