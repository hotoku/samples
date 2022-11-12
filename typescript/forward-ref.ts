class Hoge {
  constructor() {}
  get(): Fuga {
    return new Fuga();
  }
}

class Fuga {
  constructor() {}
}

const h = new Hoge();
console.log(h.get());
