import { expect } from "chai";
import "mocha";

import { LinkList } from "../src/link_list"




describe("link_list", () => {
  it("insert and delete", () => {
    const l = new LinkList<number>()
    const h = l.head
    const n1 = l.insert(1, h)
    const n2 = l.insert(2, n1)
    const n3 = l.insert(3, n2)
    expect(n1.val).to.be.equal(1)
    expect(n2.val).to.be.equal(2)
    expect(n3.val).to.be.equal(3)
  })

  it("insert", () => {
    const l = new LinkList<number>()
    const h = l.head
    const t = l.tail
    const n = l.insert(1, h)
    expect(l.head).to.be.equal(h, "l.head")
    expect(l.tail).to.be.equal(t, "l.tail")
    expect(h.next()).to.be.equal(n, "h.hext")
    expect(n.prev()).to.be.equal(h, "n.prev")
    expect(n.next()).to.be.equal(t, "n.next")
    expect(t.prev()).to.be.equal(n, "t.prev")
  })

  it("push", () => {
    const l = new LinkList<number>()
    l.push(1)
    l.push(2)
    const x = l.tail.prev()
    switch (x.kind) {
      case "LinkNode": expect(x.val).to.be.equal(2); break
      default: throw "never come here"
    }
  })

  it("iterator", () => {
    const l = new LinkList<number>()
    const ary = [1, 2, 3]
    for (let v of ary) {
      l.push(v)
    }
    const ary2 = Array.from(l)
    expect(ary2.length).to.be.equal(ary.length)
    for (let i = 0; i < ary.length; i++) {
      expect(ary2[i]).to.be.equal(ary[i])
    }
  })
})
