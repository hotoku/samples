// javascriptでは、クラスを定義する構文がない。
// 代わりに、関数をnewを付けて呼び出すと、オブジェクトのコンストラクタとして働くようになっている
// これで、見た目上、普通のオブジェクト指向言語のようにインスタンス化が出来る
var MyClass = function(){
    this.a = 1;
};
x = new MyClass();
console.log(x.a); // => 1


var MyClass2 = function(a){
    this.a = a;
};
x = new MyClass2(100);
console.log(x.a); // => 100

// returnで、オブジェクトを返すと、returnの引数が返される
var MyClass3 = function(a){
    this.a = 1;
    this.b = 100;
    return {
        a: a
    };
};
x = new MyClass3(200);
console.log(x.a); // => 200
console.log(x.b); // => undefined
