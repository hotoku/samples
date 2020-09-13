import { NodeBase, Head, Tail, LinkNode, Preceder, Follower, LinkList } from "./link_list"

class SkipListNodeBase<T>{
  protected _level: number
  constructor(protected _pointer: NodeBase<T>[], protected _val?: T) {
    this._level = _pointer.length
  }
  get level(): number {
    return this._level
  }
  get val(): T | undefined {
    return this._val
  }
  node(level: number): NodeBase<T> {
    return this._pointer[level]
  }
}

class SkipListNodeHead<T> extends SkipListNodeBase<T> {
  protected _pointer: Head<T>[]
  constructor(p: Head<T>[]) {
    super(p, undefined)
    this._pointer = p
  }
  get val(): undefined {
    return undefined
  }
  node(level: number): Head<T> {
    return this._pointer[level]
  }
}

class SkipListNodeTail<T> extends SkipListNodeBase<T> {
  protected _pointer: Tail<T>[]
  constructor(p: Tail<T>[]) {
    super(p, undefined)
    this._pointer = p
  }
  get val(): undefined {
    return undefined
  }
  node(level: number): Tail<T> {
    return this._pointer[level]
  }
}

class SkipListNode<T> extends SkipListNodeBase<T>{
  protected _pointer: LinkNode<T>[]
  constructor(p: LinkNode<T>[], v: T) {
    super(p, v)
    this._pointer = p
  }
  get val(): T {
    switch (this._val) {
      case undefined: throw "never come here 4d4d1ff6b0"
      default: return this._val
    }
  }
  node(level: number): LinkNode<T> {
    return this._pointer[level]
  }
}

export class SkipList<T>{
  private _cmp: (l: T, r: T) => number // -1: l < r, 1: l > r, 0: l=r
  private _list: LinkList<T>[]
  private _maxh: number
  private _height: number
  private _size: number
  private _head: SkipListNodeHead<T>
  private _tail: SkipListNodeTail<T>
  constructor(cmp: (l: T, r: T) => number, h: number) {
    this._cmp = cmp
    this._list = [];
    this._maxh = h
    this._height = 1
    this._size = 0

    for (let i = 0; i < h; i++) {
      this._list[i] = new LinkList<T>()
    }
    const heads = this._list.map(l => l.head)
    const tails = this._list.map(l => l.tail)
    this._head = new SkipListNodeHead<T>(heads)
    this._tail = new SkipListNodeTail<T>(tails)
  }

  search(v: T): SkipListNode<T> {
    const le = (x: T) => this._cmp(x, v) <= 0
    let l: Preceder<T> = this._head.node(this._height - 1)
    for (let i = this._height - 1; i >= 0; i--) {
      let n = LinkList.find_last(le, l)
    }
  }
}
