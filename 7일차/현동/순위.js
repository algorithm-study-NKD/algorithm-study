// https://programmers.co.kr/learn/courses/30/lessons/49191

function find(player, visited, rankMap, result) {
  if (visited[player]) return;
  visited[player] = true;

  for (let i = 1; i < visited.length; i++) {
    if (result === "win" && rankMap[player][i] === 1) {
      find(i, visited, rankMap, result);
    } else if (result === "lose" && rankMap[i][player] === 1) {
      find(i, visited, rankMap, result);
    }
  }
}

function solution(n, results) {
  let answer = 0;
  let rankMap = Array.from({ length: n + 1 }, () => Array(n + 1).fill(0));

  results.forEach((result) => {
    let winner = result[0];
    let loser = result[1];
    rankMap[winner][loser] = 1;
  });

  for (let player = 1; player < n + 1; player++) {
    let visited = Array(n + 1).fill(false);
    visited[player] = true;

    for (let i = 1; i < n + 1; i++) {
      if (rankMap[player][i] === 1) {
        //                 플레이어가 i선수를 이겼다.
        find(i, visited, rankMap, "win");
      }
      if (rankMap[i][player] === 1) {
        //                 플레이어가 i선수에게 졌다.
        find(i, visited, rankMap, "lose");
      }
    }

    if (visited.filter((v) => v).length === n) answer += 1;
  }
  return answer;
}
