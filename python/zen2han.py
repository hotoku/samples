ZEN = "".join(chr(0xff01 + i) for i in range(94))
HAN = "".join(chr(0x21 + i) for i in range(94))

ZEN2HAN = str.maketrans(ZEN, HAN)
HAN2ZEN = str.maketrans(HAN, ZEN)

print("あいうえおＡＢＣＤＥ".translate(ZEN2HAN))
print("あいうえおABCDE".translate(HAN2ZEN))
