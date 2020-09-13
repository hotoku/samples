export type Preceder<T> = Head<T> | LinkNode<T>
export type Follower<T> = LinkNode<T> | Tail<T>


export class NodeBase<T> {
  protected _prev?: Preceder<T>
  protected _next?: Follower<T>


  constructor(p?: Preceder<T>, n?: Follower<T>) {
    this._prev = p
    this._next = n
  }

  prev(): Preceder<T> | undefined {
    return this._prev
  }
  next(): Follower<T> | undefined {
    return this._next
  }
}

class Head<T> extends NodeBase<T> {
  kind = "Head" as const
  prev(): undefined {
    return undefined
  }
  next(): LinkNode<T> | Tail<T> {
    if (this._next === undefined) {
      throw "Head must have next"
    }
    return this._next
  }
  setNext(n: Follower<T>) {
    this._next = n
    return n
  }
}

class Tail<T> extends NodeBase<T> {
  kind = "Tail" as const
  prev(): Preceder<T> {
    if (this._prev === undefined) {
      throw "Tail must have next"
    }
    return this._prev
  }
  next(): undefined {
    return undefined
  }
  setPrev(p: Preceder<T>) {
    this._prev = p
    return p
  }
}

export class LinkNode<T> extends NodeBase<T> {
  kind = "LinkNode" as const
  private _val: T
  constructor(p: Preceder<T>, n: Follower<T>, v: T) {
    super(p, n)
    this._val = v
  }
  prev(): Preceder<T> {
    if (this._prev === undefined) {
      throw "LinkNode must have prev"
    }
    return this._prev
  }
  next(): Follower<T> {
    if (this._next === undefined) {
      throw "LinkNode must have next"
    }
    return this._next
  }
  setPrev(p: Preceder<T>) {
    this._prev = p
    return p
  }
  setNext(n: Follower<T>) {
    this._next = n
    return n
  }
  get val(): T {
    return this._val
  }
}

export class LinkList<T> implements Iterable<T> {
  private _head: Head<T>
  private _tail: Tail<T>
  private _size: number
  constructor() {
    this._head = new Head()
    this._tail = new Tail()
    this._size = 0

    // breaking a `protected` guard
    this._head["_next"] = this._tail
    this._tail["_prev"] = this._head
  }
  get head(): Head<T> {
    return this._head
  }
  get tail(): Tail<T> {
    return this._tail
  }
  get length(): number {
    return this._size
  }
  insert(v: T, p: Preceder<T>): LinkNode<T> {
    const n = p.next()
    const ret = new LinkNode(p, n, v)
    p.setNext(ret)
    n.setPrev(ret)
    this._size++
    return ret
  }
  delete(p: LinkNode<T>): LinkNode<T> {
    p.prev().setNext(p.next())
    p.next().setPrev(p.prev())
    this._size--
    return p
  }
  push(v: T): LinkNode<T> {
    const p = this.tail.prev()
    return this.insert(v, p)
  }
  *[Symbol.iterator](): Iterator<T> {
    let n = this.head.next()
    while (true) {
      switch (n.kind) {
        case "Tail": return
        case "LinkNode": {
          yield n.val
          n = n.next()
          break
        }
        default: throw "never come here 2"
      }
    }
  }
  static find_last<T>(pred: (v: T) => boolean, node: Preceder<T>): Preceder<T> {
    let cur: Preceder<T> = node
    let next: Follower<T> = node.next()
    while (true) {
      switch (next.kind) {
        case "Tail": return cur
        case "LinkNode": {
          if (!pred(next.val)) {
            return cur
          } else {
            cur = next
            next = cur.next()
          }
          break
        }
        default: throw "never come here 1"
      }
    }
  }
}
