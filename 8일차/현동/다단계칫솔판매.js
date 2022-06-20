// https://programmers.co.kr/learn/courses/30/lessons/77486

function solution(enroll, referral, seller, amount) {
  const result = Array(enroll.length).fill(0);

  referral = referral.map((name) => {
    if (name === "-") return -1;
    return enroll.indexOf(name);
  });

  seller = seller.map((name) => enroll.indexOf(name));

  function settle(idx, profit) {
    const nextProfit = Math.floor(profit / 10);
    const currProfit = profit - nextProfit;
    result[idx] += currProfit;
    if (nextProfit === 0) return;
    if (referral[idx] === -1) return;
    settle(referral[idx], nextProfit);
  }

  seller.forEach((sellerIdx, i) => {
    settle(sellerIdx, amount[i] * 100);
  });

  return result;
}
