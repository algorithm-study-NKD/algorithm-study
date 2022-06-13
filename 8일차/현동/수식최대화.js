// https://programmers.co.kr/learn/courses/30/lessons/67257

function solution(expression) {
  let operators = ["+", "-", "*"];
  let operatorsCnt = [0, 0, 0];
  let expressionArr = [];
  let result = [];

  let number = "";
  for (let str of expression.split("")) {
    if (operators.includes(str)) {
      operatorsCnt[operators.indexOf(str)] += 1;
      expressionArr.push(number);
      expressionArr.push(str);
      number = "";
    } else {
      number += str;
    }
  }
  expressionArr.push(number);

  for (let i = 0; i < 3; i++) {
    for (let ii = 0; ii < 3; ii++) {
      if (i === ii) continue;
      for (let iii = 0; iii < 3; iii++) {
        if (ii === iii) continue;
        if (i === iii) continue;
        let tmp = [...expressionArr];
        for (let oper of [i, ii, iii]) {
          let operator = operators[oper];
          let n = operatorsCnt[oper];
          while (n > 0) {
            let j = 0;
            while (j < tmp.length) {
              if (j + 1 <= tmp.length && operator === tmp[j + 1]) {
                n -= 1;
                if (operator === "+") {
                  tmp[j] = Number(tmp[j]) + Number(tmp[j + 2]);
                } else if (operator === "-") {
                  tmp[j] = Number(tmp[j]) - Number(tmp[j + 2]);
                } else if (operator === "*") {
                  tmp[j] = Number(tmp[j]) * Number(tmp[j + 2]);
                }
                tmp.splice(j + 1, 2);
              } else {
                j += 1;
              }
            }
          }
        }
        result.push(Math.abs(tmp[0]));
      }
    }
  }

  return Math.max(...result);
}
