const func = ({ a }: { a: string }) => {
  return a + "b";
};

const func2 = ({ a }: { a: string; b: string }) => {
  return a + "b";
};

const func3 = (obj: { a: string }) => {
  return obj.a + "b";
};

const func4 = ({ a, b }: { a: string; b: string }) => {
  return a + b;
};

console.log(func({ a: "a" }));
// console.log(func2({ a: "a" })); これはエラー
console.log(func2({ a: "a", b: "b" }));
console.log(func3({ a: "a" }));
// console.log(func3({ a: "a", b: "b" })); これはエラー
console.log(func4({ a: "a", b: "b" }));
