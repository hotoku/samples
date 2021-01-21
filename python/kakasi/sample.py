import pykakasi

ss = [
    "レコード識別情報",
    "レセプト番号",
    "レセプト種別",
    "診療年月",
    "氏名",
    "性別",
    "生年月日",
    "給付割合",
    "入院年月日",
    "病棟区分",
    "一部負担金・食事療養費・生活療養費標準負担額区分",
    "レセプト突起事項",
    "病床数",
    "カルテ番号等",
    "割引点数単価",
    "予備1",
    "予備2",
    "旧診療科",
    "検索番号",
    "記録条件仕様年月情報",
    "請求情報",
    "診療科名"
]

kks = pykakasi.kakasi()


def doit(s):
    ret = kks.convert(s)
    for i in ret:
        print("{}: kana '{}', hiragana '{}', romaji '{}'".format(
            i["orig"],
            i["kana"],
            i["hira"],
            i["hepburn"]
        ))

for s in ss:
    doit(s)
    print("----")
