// https://programmers.co.kr/learn/courses/30/lessons/43162

function dfs(i, n, visited, computers) {
  visited[i] = true;

  for (let j = 0; j < n; j++) {
    if (visited[j] || computers[i][j] === 0) continue;
    dfs(j, n, visited, computers);
  }
}

function solution(n, computers) {
  let answer = 0;
  let visited = Array(n).fill(false);

  for (let i = 0; i < n; i++) {
    if (visited[i]) continue;
    answer++;
    dfs(i, n, visited, computers);
  }

  return answer;
}
