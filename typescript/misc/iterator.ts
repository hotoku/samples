class Itr implements Iterable<number>{
  constructor(private n: number) { }

  *[Symbol.iterator](): Iterator<number> {
    for (let i = 0; i < this.n; i++) {
      yield i
    }
  }
}

(() => {
  const a = new Itr(3)
  for (let i of a) {
    console.log(i)
  }
})()
