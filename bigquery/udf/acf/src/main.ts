function acf1(ary: Array<number>, deg: number): number {
  let s = 0;
  for (let i = 0; i < ary.length; i++) {
    s += ary[i];
  }
  s /= ary.length;
  let s2 = 0;
  for (let i = 0; i < ary.length - deg; i++) {
    s2 += (ary[i] - s) * (ary[i + deg] - s);
  }
}

export function acf(ary: Array<number>): number {
  const n = ary.length;

  return n * 2;
}
