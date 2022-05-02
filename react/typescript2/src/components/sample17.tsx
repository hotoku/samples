import React, { useState, useCallback } from "react";

const request = async (n: number): Promise<string> => {
  await new Promise((s) => setTimeout(s, n * 1000));
  return "" + n;
};

const ns = [1, 2, 3, 4, 5];

type Result = {
  [key: string]: string;
};

const updateResult = (old: Result, val: string): Result => {
  console.log(old);
  const ret: Result = {};
  for (let v in Object.keys(old)) {
    ret[v] = old[v];
  }
  ret[val] = val;
  return ret;
};

export const Sample17 = () => {
  const [result, setResult] = useState<Result>({});
  const [isSending, setIsSending] = useState<boolean>(false);

  const sendRequest = useCallback(async () => {
    if (isSending) return;
    setResult((_) => {
      return {};
    });
    setIsSending(true);
    await Promise.all(
      ns.map((n) =>
        request(n).then((val) => {
          setResult((old) => updateResult(old, val));
        })
      )
    );
    setIsSending(false);
  }, [isSending]);

  return (
    <div>
      <div>
        <button disabled={isSending} onClick={sendRequest}>
          send
        </button>{" "}
        {Object.keys(result).map((n) => (
          <p>{n}</p>
        ))}
      </div>
    </div>
  );
};
