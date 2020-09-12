class Nullable {
  a?: number
  constructor() { }
}

var x = new Nullable()
console.log(x.a + 1)

class Nullable2 {
  a: number | undefined
  constructor() { }
}
var y = new Nullable2()
console.log(y.a + 1)
