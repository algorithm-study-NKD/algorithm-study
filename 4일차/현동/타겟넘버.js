// https://programmers.co.kr/learn/courses/30/lessons/43165

function solution(numbers, target) {
  let answer = 0;

  function dfs(total, level) {
    if (level == numbers.length) {
      if (total == target) {
        ++answer;
      }
      return;
    }

    dfs(total + numbers[level], level + 1);
    dfs(total - numbers[level], level + 1);
  }

  dfs(numbers[0], 1);
  dfs(-numbers[0], 1);

  return answer;
}
