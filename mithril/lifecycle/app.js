var App = {
  view: function(vnode){
    console.log("view: " + new Date());
    return m("div", [
      m("div", "hoge"),
      m("button", {
        onclick: () => console.log("onclick: " + new Date())
      }, "ボタン")
    ]);
  },
  oninit: function(vnode){
    console.log("oninit: " + new Date());
  },
  onbeforeupdate: function(vnode){
    console.log("onbeforeupdate: " + new Date());
  },
  oncreate: function(vnode){
    console.log("oncreate: " + new Date());
  },
  onupdate: function(vnode){
    console.log("onupdate: " + new Date());
  }
};


m.route(document.body, "home", {
  "home": {
    render: function(vnode){
      return m(App, vnode.attrs);
    },
    onmatch: function(vnode){
      console.log("onmatch: " + new Date());
    }
  }
});
