import { expect } from "chai";
import "mocha";

import { Point } from "../src/utils"
import { graham_scan } from "../src/graham_scan"

describe("graham scan", () => {
  it("triangle", () => {
    const data = [
      new Point(0, 0),
      new Point(1, 0),
      new Point(1, 1)
    ]
    const ret = graham_scan(data)
    expect(ret.length).to.be.equal(3)
  })

  it("square", () => {
    const data = [
      new Point(0, 0),
      new Point(0, 1),
      new Point(1, 1),
      new Point(1, 0),
      new Point(0.5, 0.5)
    ]
    const ret = graham_scan(data)
    expect(ret.length).to.be.equal(4)
  })

  it("robust 1", () => {
    const data = [
      new Point(7.3000000000000194, 7.3000000000000167),
      new Point(24.000000000000068, 24.000000000000071),
      new Point(24.00000000000005, 24.000000000000053),
      new Point(0.50000000000001621, 0.50000000000001243),
      new Point(8, 4),
      new Point(4, 9),
      new Point(15, 27),
      new Point(26, 25),
      new Point(19, 11)
    ]
    const ret = graham_scan(data)
    expect(ret.length).to.be.equal(6)
  })

  it("robust 2", () => {
    const data = [
      new Point(27.643564356435643, -21.881188118811881),
      new Point(83.366336633663366, 15.544554455445542),
      new Point(4, 4),
      new Point(73.415841584158414, 8.8613861386138595)
    ]
    const ret = graham_scan(data)
    expect(ret.length).to.be.equal(4)
  })

  it("robust 3", () => {
    const data = [
      new Point(24.00000000000005, 24.000000000000053),
      new Point(24, 6),
      new Point(54.85, 6),
      new Point(54.850000000000357, 61.000000000000121),
      new Point(24.000000000000068, 24.000000000000071),
      new Point(6, 6)
    ]
    const ret = graham_scan(data)
    expect(ret.length).to.be.equal(3)
  })
})
