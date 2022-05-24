// https://programmers.co.kr/learn/courses/30/lessons/77485

function solution(rows, columns, queries) {
  let j = 1;
  let Map = Array.from({ length: rows }, () =>
    Array(columns)
      .fill()
      .map(() => j++)
  );
  let minValues = [];

  for ([row1, col1, row2, col2] of queries) {
    let values = [];
    const intervalX = row2 - row1;
    const intervalY = col2 - col1;

    let tmp = 0;

    tmp = Map[row1 - 1][col2 - 1];
    for (let i = 1; i < intervalX + 1; i++) {
      [Map[row1 - 1 + i][col2 - 1], tmp] = [tmp, Map[row1 - 1 + i][col2 - 1]];
      values.push(tmp);
    }

    for (let i = 1; i < intervalY + 1; i++) {
      [Map[row2 - 1][col2 - 1 - i], tmp] = [tmp, Map[row2 - 1][col2 - 1 - i]];
      values.push(tmp);
    }

    for (let i = 1; i < intervalX + 1; i++) {
      [Map[row2 - 1 - i][col1 - 1], tmp] = [tmp, Map[row2 - 1 - i][col1 - 1]];
      values.push(tmp);
    }

    for (let i = 1; i < intervalY + 1; i++) {
      [Map[row1 - 1][col1 - 1 + i], tmp] = [tmp, Map[row1 - 1][col1 - 1 + i]];
      values.push(tmp);
    }

    minValues.push(Math.min(...values));
  }
  return minValues;
}
