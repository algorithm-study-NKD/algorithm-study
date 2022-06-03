// https://programmers.co.kr/learn/courses/30/lessons/81302

const dy = [-1, 0, 1, 0];
const dx = [0, 1, 0, -1];

function checkDistance(y, x, level, visited, place) {
  if (place[y][x] === "X" || level === 3) return 1;
  if (level !== 0 && place[y][x] === "P") return 0;
  visited[y][x] = true;
  for (let i = 0; i < 4; i++) {
    const ny = y + dy[i];
    const nx = x + dx[i];
    if (ny < 0 || nx < 0 || ny >= 5 || nx >= 5) continue;
    if (place[ny][nx] === "X") continue;
    if (visited[ny][nx]) continue;
    if (checkDistance(ny, nx, level + 1, visited, place) === 0) return 0;
  }
}

function findP(place) {
  for (let y = 0; y < 5; y++) {
    for (let x = 0; x < 5; x++) {
      if (place[y][x] === "P") {
        let visited = Array.from({ length: 5 }, () => Array(5).fill(false));
        if (checkDistance(y, x, 0, visited, place) === 0) return 0;
      }
    }
  }
  return 1;
}

function solution(places) {
  let result = Array(5).fill(1);
  places.forEach((place, index) => {
    result[index] = findP(place);
  });
  return result;
}
