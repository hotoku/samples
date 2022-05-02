import React, { useState, useCallback } from "react";

const request = async (n: number): Promise<string> => {
  await new Promise((s) => setTimeout(s, n * 1000));
  return "" + n;
};

const ns = [1, 2, 3];

const updateResult = (old: string[], val: string): string[] => {
  const ret: string[] = [];
  for (let v of old) {
    ret.push(v);
  }
  ret.push(val);
  return ret;
};

export const Sample16 = () => {
  const [result, setResult] = useState<string[]>([]);
  const [isSending, setIsSending] = useState<boolean>(false);

  const sendRequest = useCallback(async () => {
    if (isSending) return;
    setResult([]);
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
        {result.map((n) => (
          <p>{n}</p>
        ))}
      </div>
    </div>
  );
};
