class GetterSetter {
  private _a: number

  constructor() {
    this._a = 0
  }

  get a(): number {
    return this._a
  }

  set a(x: number) {
    this._a = x
  }
}

(() => {
  const gs = new GetterSetter()
  gs.a = 10
  console.log(gs.a)
})()
