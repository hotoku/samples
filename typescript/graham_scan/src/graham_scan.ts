import { Point } from "./utils"
import { SkipList } from "./skip_list"
import { assert } from "chai"

function cmp(a: Point, b: Point): number {
  if (a.x !== b.x) return a.x - b.x
  else return a.y - b.y
}

function triangle_test(a: Point, b: Point, c: Point): number {
  /*
    precondition
    a.x <= b.x <= c.x or a.x >= b.x >= c.x
    return
    1: c is left of line a->b
    0: a,b,c are colinear
    -1: c is right of line a->b
  */
  if (c.y >= b.y) return 1
  if (c.y <= a.y) return -1
  return (a.x - c.x) * (b.y - c.y) - (a.y - c.y) * (b.x - c.x)
}

class Vector<T> {
  private _ps: T[]
  private _length: number
  constructor() {
    this._ps = new Array<T>()
    this._length = 0
  }
  push(p: T): void {
    this._ps[this._length] = p
    this._length += 1
  }
  pop(): T {
    this._length -= 1
    return this._ps[this._length]
  }
  at(i: number): T {
    assert(i < this._length)
    return this._ps[i]
  }
  subst(i: number, p: T) {
    assert(i < this._length)
    this._ps[i] = p
  }
  get length(): number {
    return this._length
  }
}

export function graham_scan(data: Point[]): Point[] {
  const set = new SkipList<Point>(30, cmp)
  for (let i of data) {
    set.insert(i)
  }
  const n = set.size
  const data2 = Array.from(set).sort(cmp)
  const a = data2[0]
  const b = data2[n - 1]
}
