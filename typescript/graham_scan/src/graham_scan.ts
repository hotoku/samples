import { Point } from "./utils"
import { SkipList } from "./skip_list"

function cmp(a: Point, b: Point): number {
  if (a.x !== b.x) return a.x - b.x
  else return a.y - b.y
}

function cmp2(a: Point, b: Point): number {
  if (a.arg !== b.arg) return a.arg - b.arg
  else return a.abs - b.abs
}

export function graham_scan(data: Point[]): Point[] {
  const set = new SkipList<Point>(30, cmp)
  for (let i of data) {
    set.insert(i)
  }
  const data2 = Array.from(set).sort(cmp2)
  return []
}
