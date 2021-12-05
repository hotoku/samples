const vals = ["a", "b", "c"] as const;
type Val = typeof vals[number]; // Valは"a" | "b" | "c"

const a: Val = "a";
// 👇はtype errorになる
// const d: Val = "d";
