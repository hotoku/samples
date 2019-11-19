var obj = {
    val: 1,
    setter: v => obj.val = v // ??? obj.val=ならOK, val=だとNG ???
}

var App = {
    view: function(vnode){
        return m("", {
            onclick: () => {
                obj.setter(obj.val + 1);
            },
            textContent: obj.val
        });
    }
};

m.mount(document.getElementById("root"), App);



/*
ブラウザのコンソールで、obj.val = "hoge"
を実行しても、画面は変わらない。が、実はメモリ上ではobjの値は変わっていて、
m.redraw()を実行すると、表示がhogeに変わる
*/
