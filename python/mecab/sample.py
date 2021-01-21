import MeCab
pic = "本日は晴天なり"
try:
    m = MeCab.Tagger("-Owakati")
    pic = m.parse(pic)
    pic = pic.strip()  # 先頭と末尾の空白を削除
    pic = pic.replace(' ', '_')  # 単語間に開けた空白を変換
except RuntimeError:
    pic = ""
print(pic)
