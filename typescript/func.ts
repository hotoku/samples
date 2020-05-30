function f(s: string): string{
    return s + " in f";
}

// 以下はエラー
// f(1);
// const x: number = f("");

const x: string = f("abc");
console.log(x);
