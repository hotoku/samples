var a = function(){
  return {
    cnt: 0,
    f: function(x){
      g = () => this.cnt = x;
      g();
    }
  }
}

var obj = new a();
console.log(obj.cnt);
obj.f(100);
console.log(obj.cnt);
