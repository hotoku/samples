function func(x: number): number {
  return x + 1;
}

// これはエラー
// function func2<T>(x: T): T[] {}

// これはエラー
export function func3<T>(f: (n: number) => T): T[] {}
