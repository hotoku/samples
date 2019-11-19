var a=function(msg){
  var m = "piyo";
  return {
    g: function(){
      console.log(this.m);
      [1, 2, 3].map(this.f); // ここのfの呼び出しは(f自体は期待通りにこのオブジェクトの中のfを指しているが)、
                             // mapの中での関数呼び出しになるので、thisはこのオブジェクトではない何かを指している
    },
    f: function(x){
      console.log(this.m + ": f(" + x + ")");
    },
    m: msg
  }
};

var m = "fuga";

var obj = new a("hoge");
console.log(obj.m);
obj.g(); // ここのgの呼び出しは、objに対するメソッド呼び出しなので、gの中のthisはobjに束縛される
