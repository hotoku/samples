import { Preceder, Follower, LinkList } from "./link_list"

export class SkipList<T>{
  private _cmp: (l: T, r: T) => number
  private _list: LinkList<T>[]
  private _maxh: number
  private _height: number
  private _size: number
  constructor(cmp: (l: T, r: T) => number, h: number) {
    this._cmp = cmp
    this._list = [];
    this._maxh = h
    this._height = 1
    this._size = 0

    for (let i = 0; i < h; i++) {
      this._list[i] = new LinkList<T>()
    }
  }

  private top(): LinkList<T> {
    return this._list[this._height]
  }

  search_up(v: T, node: Preceder): Follower<T> {
    const l1 = this.top()
    const gt = (x: T) => this._cmp(v, x) >= 0
    const n = l1.find_first(gt)
  }
}
