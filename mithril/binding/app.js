// form.xと、mdl.mmbが連動
// form.xに入力→mdl.mmbが更新
// form2.submitを押すと、mld.mmbが100にセットされる、と同時に、form.xの値も100に更新
// この例は、双方向のbindingがうまくいっている




var mdl = {
    mmb: 1,
    setter: (v) => mdl.mmb = v
};

var comp = {
    view: function(ctrl){
        return [
            m("form#form", [
                m("label", "x"),
                m("input[name=x][type=text]", {
                    oninput: m.withAttr("value", mdl.setter),
                    value: mdl.mmb
                })
            ]),
            m("form#form2", {
                onsubmit: (e) => {
                    e.preventDefault();
                    mdl.mmb = 100;
                }
            }, m("input[type=submit][value=送信]")
             )
        ];
    }
};

m.mount(document.getElementById("root"), comp);
