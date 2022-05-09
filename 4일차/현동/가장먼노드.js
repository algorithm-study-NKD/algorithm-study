// https://programmers.co.kr/learn/courses/30/lessons/49189

function solution(n, edge) {
  let q = [1];
  let visited = Array(n + 1).fill(0);
  let Map = Array.from({ length: n + 1 }, () => []);
  visited[1] = 1;

  edge.forEach((e) => {
    Map[e[0]].push(e[1]);
    Map[e[1]].push(e[0]);
  });

  let max = 0;
  while (q.length !== 0) {
    let node = q.shift();
    Map[node].forEach((next) => {
      if (!visited[next]) {
        q.push(next);
        visited[next] = visited[node] + 1;
        max = visited[node] + 1;
      }
    });
  }

  return visited.filter((v) => v === max).length;
}
