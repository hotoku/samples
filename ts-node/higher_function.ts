const mymap = <D>(f: (n: D) => D, ls: D[]): D[] => {
  const n = ls.length;
  const ret = new Array<D>(n);
  for (let i = 0; i < n; i++) {
    ret[i] = f(ls[i]);
  }
  return ret;
};

const twice = <D>(f: (n: D) => D): ((n: D) => D) => {
  return (n: D): D => f(f(n));
};

console.log(mymap((n: number) => n + 1, [1, 2, 3]));
console.log(twice((n: number): number => n + 1)(10));
