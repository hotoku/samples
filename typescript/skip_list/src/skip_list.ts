import { assert } from "chai"
type Preceder<T> = Head<T> | Elem<T>
type Follower<T> = Elem<T> | Tail<T>

class NodeBase<T>{
  protected _prev?: Preceder<T>[]
  protected _next?: Follower<T>[]
  constructor(
    protected _level: number,
    prev?: Preceder<T>[],
    next?: Follower<T>[],
    protected _val?: T
  ) {
    if (prev) {
      this._prev = []
      for (let i = 0; i < _level; i++) {
        this._prev[i] = prev[i]
      }
    }
    if (next) {
      this._next = []
      for (let i = 0; i < _level; i++) {
        this._next[i] = next[i]
      }
    }
  }
  next(l: number): Follower<T> | undefined {
    if (this._next) {
      return this._next[l]
    } else {
      return undefined
    }
  }
  prev(l: number): Preceder<T> | undefined {
    if (this._prev) {
      return this._prev[l]
    } else {
      return undefined
    }
  }
  setNext(l: number, n: Follower<T>) {
    if (this._next) {
      this._next[l] = n
    }
  }
  setPrev(l: number, n: Preceder<T>) {
    if (this._prev) {
      this._prev[l] = n
    }
  }
  get level(): number {
    return this._level
  }
}

class Head<T> extends NodeBase<T> {
  kind = "Head" as const
  protected _next: Follower<T>[]
  constructor(_level: number) {
    super(_level)
    const prevs: Head<T>[] = []
    for (let i = 0; i < _level; i++) {
      prevs[i] = this
    }
    const tail = new Tail(_level, prevs)
    this._next = []
    for (let i = 0; i < _level; i++) {
      this._next[i] = tail
    }
  }
  prev(): undefined {
    return undefined
  }
  next(l: number): Follower<T> {
    return this._next[l]
  }
}

class Tail<T> extends NodeBase<T> {
  kind = "Tail" as const
  constructor(
    protected _level: number,
    protected _prev: Preceder<T>[]
  ) {
    super(_level, _prev)
  }
  prev(l: number): Preceder<T> {
    return this._prev[l]
  }
  next(): undefined {
    return undefined
  }
}

class Elem<T> extends NodeBase<T> {
  kind = "Elem" as const
  constructor(
    protected _level: number,
    protected _prev: Preceder<T>[],
    protected _next: Follower<T>[],
    protected _val: T
  ) {
    super(_level, _prev, _next, _val)
  }
  prev(l: number): Preceder<T> {
    return this._prev[l]
  }
  next(l: number): Follower<T> {
    return this._next[l]
  }
  get val(): T {
    return this._val
  }
}

export class SkipList<T> {
  private _head: Head<T>
  private _tail: Tail<T>
  private _size: number
  private _prob: number = 0.5 as const
  private _le: (x: T) => ((y: T) => boolean)
  private _lt: (x: T) => ((y: T) => boolean)
  private _eq: (x: T) => ((y: T) => boolean)
  private _ge: (x: T) => ((y: T) => boolean)
  private _gt: (x: T) => ((y: T) => boolean)


  constructor(private _level: number, _cmp: (x: T, y: T) => number) {
    this._head = new Head<T>(_level)
    const t = this._head.next(0)
    switch (t.kind) {
      case "Tail": this._tail = t; break
      default: throw "never come here d34c78a9cd"
    }
    this._size = 0
    this._le = (x: T) => ((y: T) => _cmp(y, x) <= 0)
    this._lt = (x: T) => ((y: T) => _cmp(y, x) < 0)
    this._eq = (x: T) => ((y: T) => _cmp(y, x) === 0)
    this._ge = (x: T) => ((y: T) => _cmp(y, x) >= 0)
    this._gt = (x: T) => ((y: T) => _cmp(y, x) > 0)
  }
  private _find_level(): number {
    let ret = 1
    while (ret <= this._level && Math.random() < this._prob) {
      ret++
    }
    return ret
  }
  private _find_last_at(level: number, pos: Preceder<T>, pred: (x: T) => boolean): Preceder<T> {
    let cur = pos
    let next = cur.next(level)
    while (true) {
      switch (next.kind) {
        case "Tail": return cur
        case "Elem": {
          if (pred(next.val)) {
            cur = next
            next = cur.next(level)
          } else {
            return cur
          }
        }
      }
    }
  }
  private _find_last(pred: (x: T) => boolean): Preceder<T>[] {
    const ret: Preceder<T>[] = []
    let cur: Preceder<T> = this._head
    for (let lev = this._level - 1; lev >= 0; lev--) {
      cur = this._find_last_at(lev, cur, pred)
      ret[lev] = cur
    }
    return ret
  }
  insert(v: T) {
    const level = this._find_level()
    const pos = this._find_last(this._le(v))
    switch (pos[0].kind) {
      case "Elem": {
        if (this._eq(pos[0].val)(v)) return
      }
    }

    const prevs: Preceder<T>[] = []
    const nexts: Follower<T>[] = []
    for (let i = 0; i < level; i++) {
      prevs[i] = pos[i]
      nexts[i] = pos[i].next(i)
    }
    const node = new Elem(level, prevs, nexts, v)
    for (let i = 0; i < level; i++) {
      pos[i].setNext(i, node)
      pos[i].next(i).setPrev(i, node)
    }
    this._size++
  }
  has(v: T): boolean {
    const node = this._find_last(this._le(v))
    switch (node[0].kind) {
      case "Head": return false
      case "Elem": {
        return this._eq(v)(node[0].val)
      }
    }
  }
  get size(): number {
    return this._size
  }
  delete(v: T) {
    const preds = this._find_last(this._le(v))
    const node = preds[0]
    switch (node.kind) {
      case "Head": return
      case "Elem": {
        if (!this._eq(node.val)(v)) return
      }
    }
    this._do_delete(node, preds)
  }
  private _do_delete(node: Elem<T>, preds: Preceder<T>[]) {
    assert(node === preds[0])
    for (let lev = 0; lev < node.level; lev++) {
      const x = preds[lev]
      if (x === node) {
        const pred = x.prev(lev)
        const next = x.next(lev)
        pred.setNext(lev, next)
        next.setPrev(lev, pred)
      } else if (x.next(lev) === node) {
        const next = node.next(lev)
        x.setNext(lev, next)
        next.setPrev(lev, x)
      }
    }
  }
  *[Symbol.iterator](): Iterator<T> {
    let cur = this._head.next(0)
    while (true) {
      switch (cur.kind) {
        case "Tail": return
        case "Elem": {
          yield cur.val
          cur = cur.next(0)
        }
      }
    }
  }
}
