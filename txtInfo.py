from pathlib import Path
import MeCab


def JPtoList(msg: str):
    mecab = MeCab.Tagger("-Owakati")
    JpStr = mecab.parse(msg)
    return JpStr.split()


def getDict():
    # 南十字星号（サザンクロス）の旅
    # https://ncode.syosetu.com/n6430gu/
    text = Path('ミステリアス①.txt').read_text(encoding='utf-8')
    textList = JPtoList(text)
    textDict = {'textListSize': len(textList)}
    for item in textList:
        if textDict.get(item):
            textDict.update({item: textDict.get(item) + 1})
        else:
            textDict.update({item: 1})
    return textDict


if __name__ == '__main__':
    textInfoDict = getDict()
    # 全文から１行を選ぶ
    # targetText = '僕は何をしているのだ？'
    targetText = 'それから彼は僕に言った。'
    targetTextList = JPtoList(targetText)
    generateProbabilityDict = {}
    for targetItem in targetTextList:
        generateProbabilityDict.update({targetItem: textInfoDict.get(targetItem) / textInfoDict.get('textListSize')})
    print(generateProbabilityDict)
    Path('output.txt').write_text(data=str(generateProbabilityDict), encoding='utf-8')
