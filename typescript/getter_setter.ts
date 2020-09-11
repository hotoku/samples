class A {
  private _a: number

  get a(): number {
    return this._a
  }

  set a(x: number) {
    this._a = x
  }
}

const a = new A()
a.a = 100
console.log(a.a)
