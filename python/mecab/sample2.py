import MeCab
pic = "マルチボリューム識別情報"
try:
    m = MeCab.Tagger("-Owakati")
    pic = m.parse(pic)
    pic = pic.strip()  # 先頭と末尾の空白を削除
    pic = pic.replace(' ', '_')  # 単語間に開けた空白を変換
except RuntimeError:
    pic = ""
print(pic)
