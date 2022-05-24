// https://programmers.co.kr/learn/courses/30/lessons/42627

function solution(jobs) {
  jobs.sort((a, b) => {
    if (a[0] < b[0]) return -1;
    if (a[0] > b[0]) return 1;
    if (a[0] === b[0]) {
      if (a[1] < b[1]) return -1;
      if (a[1] > b[1]) return 1;
      if (a[1] === b[1]) return 0;
    }
  });

  let q = [];
  let i = 0;
  let totalWorkTime = 0;
  let currentTime = 0;

  while (i < jobs.length || q.length > 0) {
    let n = q.length;

    if (i < jobs.length && jobs[i][0] <= currentTime) {
      q.push(jobs[i]);
      i++;
    } else if (n === 0) {
      currentTime = jobs[i][0] + jobs[i][1];
      totalWorkTime += jobs[i][1];
      i++;
    } else if (n > 0) {
      q.sort((a, b) => {
        if (a[1] < b[1]) return 1;
        if (a[1] > b[1]) return -1;
        if (a[1] === b[1]) return 0;
      });
      let job = q.pop();
      totalWorkTime += currentTime - job[0] + job[1];
      currentTime += job[1];
    }
  }
  return Math.floor(totalWorkTime / jobs.length);
}
