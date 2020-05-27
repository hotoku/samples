var a = require("./a")

function b(x){
  const ret = a.a(x)
  return ret * 200
}

module.exports = {
  b: b
}
