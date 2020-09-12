class Nullable {
  a?: number
  constructor() { }
}

class Nullable2 {
  a: number | undefined
  constructor() { }
}

(() => {
  var x = new Nullable()
  console.log(x.a + 1) // compile error

  var y = new Nullable2() // compile error
  console.log(y.a + 1)
})()
