_comp_func() {
    echo "${COMP_WORDS[@]}" > /tmp/comp.txt
    COMPREPLY=($COMP_CWORD ${COMP_WORDS[@]})
    echo "${COMPREPLY[@]}" >> /tmp/comp.txt
}
complete -F _comp_func test_cmd

# COMP_WORDSは、ここまでで入力されている文字列の全部
# COMP_CWORDは、COMP_WORDSの長さ
# test_cmd 1 2 3 <TAB>
# とすると、
# COMP_WORD="test_cmd 1 2 3"
# となる。この時、画面に補完候補として
# 1         2         3         4         test_cmd  
# と表示された。順番がよく分からん・・
# ${COMPREPLY[@]}は、ちゃんと
# 4 test_cmd 1 2 3
# が入っている。辞書順にソートされている・・・？
# 実験：
# (pipeline) complete $ test_cmd bbb aaa cba abc abb bca 
# 7         aaa       abb       abc       bbb       bca       cba       test_cmd
# 答え：ソートされている模様。重複が排除されるのも確認した。


test_cmd() {
    exit 0
}
