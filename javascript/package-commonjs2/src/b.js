var a = require("./a")

function b(){
  const ret = a.a()
  return ret + ":b"
}

module.exports = {
  b: b
}
