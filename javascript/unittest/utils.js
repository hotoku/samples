module.exports.add = (a, b) => {
    return a + b;
}

module.exports.square = (x) => {
    return x * x;
}

module.exports.setName = (user, fullName) => {
    var names = fullName.split(' ');
    user.firstName = names[0];
    user.lastName = names[1];
    return user;
}

module.exports.asyncAdd = (a, b, callback) => {
    setTimeout(()=>{
        callback(a+b);
    }, 1000)
}

//コールバックはC++でいうインターフェイスに近い
//定義自体は呼び出し元に記述する
module.exports.asyncSquare = (x, callback) =>{
    setTimeout(()=>{
        callback(x*x);
    }, 1500)
}
