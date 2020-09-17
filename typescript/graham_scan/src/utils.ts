export class Point {
  private _abs: number
  private _arg: number
  constructor(public x: number, public y: number) {
    this._abs = Math.sqrt(this.x * this.x + this.y * this.y)
    if (x === 0) {
      this._arg = y > 0 ? Math.PI / 2 : -Math.PI / 2
    } else {
      this._arg = Math.acos(y / x)
    }

  }

  get abs(): number {
    return this._abs
  }

  get arg(): number {
    return this._arg
  }
}
