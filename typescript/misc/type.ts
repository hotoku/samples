// 名前は任意だが値はstringでなくてはならない、という型になる
interface MyInterface {
  [name: string]: string;
}

const obj: MyInterface = {
  hoge: "hoge",
  fuga: "fuga",
  // piyo: 1, これはコンパイルエラーになる
};

// cf. https://qiita.com/uhyo/items/e2fdef2d3236b9bfe74a
