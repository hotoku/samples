
var x = new Array(3);
function f(a){
    a[0] = 100;
};
f(x);
console.log(JSON.stringify(x));
