// import { NodeBase, LinkNode, Preceder, Follower, LinkList } from "./link_list"

// class SkipListNodeBase<T>{
//   protected _level: number
//   constructor(protected _pointer: NodeBase<T>[], protected _val?: T) {
//     this._level = _pointer.length
//   }
//   get level(): number {
//     return this._level
//   }
//   get val(): T | undefined {
//     return this._val
//   }
//   node(level: number): NodeBase<T> {
//     return this._pointer[level]
//   }
// }

// class SkipListNodeEdge<T> extends SkipListNodeBase<T> {
//   constructor(p: Node<T>[]) {
//     super(p, undefined)
//   }
//   get val(): undefined {
//     return undefined
//   }
// }

// class SkipListNode<T> extends SkipListNodeBase<T>{
//   constructor(p: LinkNode<T>[], v: T) {
//     super(p, v)
//   }
//   get val(): T {
//     switch (this._val) {
//       case undefined: throw "never come here"
//       default: return this._val
//     }
//   }
// }

// export class SkipList<T>{
//   // -1: l < r, 1: l > r, 0: l=r
//   private _cmp: (l: T, r: T) => number
//   private _list: LinkList<T>[]
//   private _maxh: number
//   private _height: number
//   private _size: number
//   private _head: SkipListNodeEdge<T>
//   private _tail: SkipListNodeEdge<T>
//   constructor(cmp: (l: T, r: T) => number, h: number) {
//     this._cmp = cmp
//     this._list = [];
//     this._maxh = h
//     this._height = 1
//     this._size = 0

//     for (let i = 0; i < h; i++) {
//       this._list[i] = new LinkList<T>()
//     }
//     const heads = this._list.map(l => l.head)
//     const tails = this._list.map(l => l.tail)
//     this._head = new SkipListNodeEdge<T>(heads)
//     this._tail = new SkipListNodeEdge<T>(tails)
//   }



//   search(v: T): SkipListNode<T> {
//     const le = (x: T) => this._cmp(x, v) <= 0
//     for (let i = this._height - 1; i >= 0; i--) {
//       let l = this._head.node(i)
//       LinkList.find_last(le, l)
//     }
//   }
// }
