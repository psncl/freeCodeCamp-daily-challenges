function secondLargest(arr) {
  let first = Number.NEGATIVE_INFINITY,
    second = Number.NEGATIVE_INFINITY;

  arr.forEach((num) => {
    if (num > first) {
      second = first;
      first = num;
    } else if (first > num && num > second) {
      second = num;
    }
    console.log(`First: ${first}, Second: ${second}`);
  });

  return second;
}
