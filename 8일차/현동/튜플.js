// https://programmers.co.kr/learn/courses/30/lessons/64065

function solution(s) {
  const result = [];
  s.slice(2, s.length - 2)
    .split("},{")
    .map((str) => str.split(",").map((v) => Number(v)))
    .sort((a, b) => a.length - b.length)
    .forEach((arr) => {
      arr.forEach((v) => {
        if (!result.includes(v)) result.push(v);
      });
    });
  return result;
}
