import { expect } from "chai";
import "mocha";

import { SkipList } from "../src/skip_list"

const cmp = (x: number, y: number) => x - y

describe("skip list", () => {
  it("insert", () => {
    const s = new SkipList(10, cmp)
    s.insert(1)
    s.insert(2)
    s.insert(3)
    expect(s.size).to.be.equal(3)
    s.insert(1)
    expect(s.size).to.be.equal(3)
  })

  it("delete", () => {
    const s = new SkipList(10, cmp)
    s.insert(1)
    s.insert(2)
    s.insert(3)
    s.delete(1)
    expect(s.size).to.be.equal(2)
  })

  it("check", () => {
    const s = new SkipList(10, cmp)
    s.insert(1)
    s.insert(2)
    s.insert(3)
    expect(s.has(1)).to.be.true
    expect(s.has(10)).to.be.false
  })

  it("insert many", () => {
    const s = new SkipList(30, cmp)
    const n = 1000000
    // const n = 3
    for (let i = 0; i < n; i++) {
      s.insert(i)
    }
    expect(s.size).to.be.equal(n)
  })

  it("insert many 2", () => {
    const s = new SkipList(30, cmp)
    const n = 1000000
    for (let i = 0; i < n; i++) {
      s.insert(1)
    }
    expect(s.size).to.be.equal(1)
    let x = 0
    for (let v of s) {
      x++
      expect(v).to.be.equal(1)
    }
    expect(x).to.be.equal(1)
  })

  it("iterator", () => {
    const s = new SkipList(10, cmp)
    const n = 100
    for (let i = 0; i < n; i++) {
      s.insert(n - i)
    }
    let e = 1
    for (let v of s) {
      expect(v).to.be.equal(e++)
    }
  })
})
