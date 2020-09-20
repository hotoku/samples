import { Point } from "./utils"
import { SkipList } from "./skip_list"
import { assert } from "chai"

function cmp(a: Point, b: Point): number {
  if (a.x !== b.x) return a.x - b.x
  else return a.y - b.y
}

function triangle_test(a: Point, b: Point, c: Point): boolean {
  if (c.y >= b.y) return true
  if (c.y <= a.y) return false
  return (a.x - c.x) * (b.y - c.y) - (a.y - c.y) * (b.x - c.x) > 0
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

function make_half_convex_hull(ps: Generator<Point>): Vector<Point> {
  const vec = new Vector<Point>()
  for (let p of ps) {
    vec.push(p)
    let m = vec.length
    while (m >= 3 && triangle_test(vec.at(m - 3), vec.at(m - 2), vec.at(m - 1))) {
      vec.subst(m - 2, vec.at(m - 1))
      vec.pop()
    }
  }

  return vec
}


export function graham_scan(data: Point[]): Point[] {
  const set = new SkipList<Point>(30, cmp)
  for (let i of data) {
    set.insert(i)
  }
  const n = set.size
  const data2 = Array.from(set).sort(cmp)
  if (n <= 3) {
    return data2
  }
  function* temp() {
    for (let p of data2) {
      yield p
    }
  }
  function* temp2() {
    for (let i = data2.length - 1; i >= 0; i--) {
      yield data2[i]
    }
  }
  const vec = make_half_convex_hull(temp())
  const vec2 = make_half_convex_hull(temp2())
  const ret = new Array<Point>()
  let i = 0
  for (; i < vec.length; i++) {
    ret[i] = vec.at(i)
  }
  for (let j = 1; j < vec2.length - 1; j++) {
    ret[i] = vec.at(j)
  }
  return ret
}
