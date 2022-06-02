// https://programmers.co.kr/learn/courses/30/lessons/17677

function makeSet(str) {
  strArr = [...str];
  let result = {};
  const patternEng = /[a-zA-Z]/;

  for (let i = 0; i < strArr.length - 1; i++) {
    const firstChar = strArr[i];
    const secondChar = strArr[i + 1];

    if (!patternEng.test(firstChar) || !patternEng.test(secondChar)) continue;

    const word = firstChar.toUpperCase() + secondChar.toUpperCase();

    if (result[word]) {
      result[word] += 1;
    } else {
      result[word] = 1;
    }
  }

  return result;
}

function union(set1, set2) {
  let result = {};
  Object.keys(set1).forEach((w) => {
    if (set2[w]) {
      result[w] = Math.max(set1[w], set2[w]);
    } else {
      result[w] = set1[w];
    }
  });
  Object.keys(set2).forEach((w) => {
    if (!result[w]) {
      result[w] = set2[w];
    }
  });
  return Object.values(result).reduce((acc, cur) => acc + cur, 0);
}

function intersection(set1, set2) {
  let result = {};
  Object.keys(set1).forEach((w) => {
    if (set2[w]) {
      result[w] = Math.min(set1[w], set2[w]);
    }
  });
  return Object.values(result).reduce((acc, cur) => acc + cur, 0);
}

function solution(str1, str2) {
  const set1 = makeSet(str1);
  const set2 = makeSet(str2);
  const unionSetCnt = union(set1, set2);
  const intersectionSetCnt = intersection(set1, set2);
  if (!unionSetCnt && !intersectionSetCnt) return 65536;
  return Math.floor((intersectionSetCnt / unionSetCnt) * 65536);
}
