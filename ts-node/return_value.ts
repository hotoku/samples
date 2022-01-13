function func(x: number): number {
  return x + 1;
}

// これはエラー
// function func2<T>(x: T): T[] {}

// これはエラー
// export function func3<T>(f: (n: number) => T): T[] {}

const WEEK_PER_YEAR = 52;
const WEEK_3_MONTH = 12;

class Week {
  year: number;
  week: number;
  constructor(y: number, w: number) {
    this.year = y;
    this.week = w;
  }

  sub(n: number): Week {
    return this;
  }
  add(n: number): Week {
    return this;
  }
}

export function construct_training_data<Datum>(
  end_year: number,
  end_week_num: number,
  vs: number[],
  lead_weeks: number,
  make_training_datum: (
    vs: number[],
    weeks: Week[],
    target: number,
    feat_s: number,
    feat_e: number
  ) => Datum
): Datum[] {
  const num_data = vs.length;

  const end_week = new Week(end_year, end_week_num);
  const start_week = end_week.sub(num_data - 1);

  const weeks = new Array<Week>(num_data);
  for (let i = 0; i < num_data; i++) {
    weeks[i] = start_week.add(i);
  }

  const num_ret = num_data - (WEEK_PER_YEAR + WEEK_3_MONTH - 1 + lead_weeks);
  const ret = new Array<Datum>(num_ret);
  let target = num_data - 1;
  let feat_e = target - lead_weeks;
  let feat_s = feat_e - (WEEK_PER_YEAR + WEEK_3_MONTH - 1);
  for (let i = 0; i < num_ret; i++) {
    ret[num_ret - 1 - i] = make_training_datum(
      vs,
      weeks,
      target,
      feat_s,
      feat_e
    );
    target -= 1;
    feat_e -= 1;
    feat_s -= 1;
  }
}
