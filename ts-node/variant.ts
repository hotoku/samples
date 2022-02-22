class X {
  x: number;
}

class Y extends X {
  y: number;
}

let xs = new Array<X>();
let ys = new Array<Y>();

xs = ys; // ok. T in Array<T> is covariant.
