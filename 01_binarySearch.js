function binarySearch(arr, item) {
  let low = 0,
    high = arr.length - 1;

  while (low <= high) {
    let mid = Math.floor((low + high) / 2);
    let guess = arr[mid];

    if (guess === item) {
      return mid;
    } else if (guess > item) {
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }

  return null;
}

const list = [1, 3, 5, 7, 9];

console.log(binarySearch(list, 3)); // => 1
console.log(binarySearch(list, -1)); // => null
