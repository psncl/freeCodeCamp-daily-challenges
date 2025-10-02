function isPerfectSquare(n) {
  if (n < 0) return false;

  //Used bisection search algorithm

  let low = 0;
  let high = n;

  while (low <= high) {
    const guess = Math.trunc((low + high) / 2);

    if (guess ** 2 > n) {
      high = guess - 1;
    } else if (guess ** 2 < n) {
      low = guess + 1;
    } else return true;
  }
  return false;
}
