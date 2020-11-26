import React, { useState, useEffect } from "react";

const sleep = (msec: number) =>
  new Promise((resolve) => setTimeout(resolve, msec));

const getLogitFromProb = async (p: number) => {
  console.log("getLogitFromProb", p);
  const ret = Math.log(p / (1 - p));
  await sleep(500);
  return ret;
};

const getProbFromLogit = async (l: number) => {
  console.log("getProbFromLogit", l);
  const ret = 1 / (1 + Math.exp(-l));
  await sleep(500);
  return ret;
};

export const Sample14 = () => {
  const [prob, setProb] = useState(0.5);
  const [logit, setLogit] = useState(0);
  console.log("sample14");

  return (
    <div>
      <form onSubmit={(e) => e.preventDefault()}>
        <label htmlFor="logit">logit</label>
        <input
          id="logit"
          type="number"
          value={logit}
          onChange={(e) => {
            console.log("logit change: ", e.target.value);
            const logit = parseFloat(e.target.value);
            setLogit(logit);
            (async () => {
              const p = await getProbFromLogit(logit);
              setProb(p);
            })();
          }}
        />
        <label htmlFor="prob">prob</label>
        <input
          id="prob"
          type="number"
          value={prob}
          onChange={(e) => {
            console.log("prob change: ", e.target.value);
            const prob = parseFloat(e.target.value);
            setProb(prob);
            (async () => {
              const l = await getLogitFromProb(prob);
              setLogit(l);
            })();
          }}
        />
      </form>
    </div>
  );
};
