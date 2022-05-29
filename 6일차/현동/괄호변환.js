// https://programmers.co.kr/learn/courses/30/lessons/60058

function makeU(words) {
  let cntLeft = 0;
  let cntRight = 0;
  let u = [];
  words.split("").some((w) => {
    if (w === "(") {
      cntLeft++;
    } else {
      cntRight++;
    }
    u.push(w);
    return cntLeft === cntRight;
  });

  return u.join("");
}

function isCorrect(words) {
  let wordsArray = words.split("");
  let stack = [];
  for (w of wordsArray) {
    if (w === ")") {
      if (stack.length === 0) {
        return false;
      }
      if (stack[stack.length - 1] === "(") {
        stack.pop();
        continue;
      }
    }
    stack.push(w);
  }
  return stack.length === 0;
}

function makeWord(words) {
  if (words === "") return "";
  let u = makeU(words);
  let v = words.slice(u.length);
  if (isCorrect(u)) {
    return u + makeWord(v);
  } else {
    let newU = u
      .slice(1, u.length - 1)
      .split("")
      .map((w) => (w === "(" ? ")" : "("))
      .join("");
    return "(" + makeWord(v) + ")" + newU;
  }
}

function solution(p) {
  if (p === "") return "";
  let u = makeU(p);
  let v = p.slice(u.length);
  if (isCorrect(u)) {
    return u + solution(v);
  } else {
    let newU = u
      .slice(1, u.length - 1)
      .split("")
      .map((w) => (w === "(" ? ")" : "("))
      .join("");
    return "(" + solution(v) + ")" + newU;
  }
}
