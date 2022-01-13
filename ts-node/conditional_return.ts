// これはエラー
// function func(x: number): number[] {}

// これは、tsconfig.jsonが存在するかしないかで挙動が変わる
// tsconfig.jsonが存在する場合（中身が空っぽでも）エラーにならない
// tsconfig.jsonが存在する場合は、エラーになる
function func2(x: number): number[] {
  if (x <= 0) {
    return [];
  }
}
