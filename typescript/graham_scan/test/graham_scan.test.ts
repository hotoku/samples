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
})
