## [2017-10-24]
* elementのinnerHTML属性で、<></>の中身を触れる
* かとおもったら、そうでもない
* <div>ほげ</div>のinnerHTMLは、"<div>ほげ</div>"だった。

* elementのtextContentが、それっぽい !!!



## [2017-10-24]
* vnode　→　モデルへの伝搬は、onclickなどのイベントで
* モデル　→　vnodeへの伝搬は、{ value: xxx }や{ textContent: xxx }で
と思っておけばよいか ???


## [2017-10-26]
* viewとdomとのバインディングは、view側がdomの値のObserverになっているような感じに見えるが、そうではない
* 単純に、イベント発生時に、view関数を呼び直しているだけ
* なので、{ value: xxx }と、オブジェクトを指定しておけば、valueの値が更新される






## emacs用
Local Variables:
eval: (howm-mode)
End:
