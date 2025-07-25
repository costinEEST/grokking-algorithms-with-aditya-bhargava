function binarySearch(arr: readonly number[], item: number): number | null {
  let low: number = 0;
  let high: number = arr.length - 1;

  while (low <= high) {
    const mid: number = Math.floor((low + high) / 2);
    const guess: number = arr[mid];

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

// Using const assertion for better type inference
const list = [1, 3, 5, 7, 9] as const;

console.log(binarySearch(list, 3)); // => 1
console.log(binarySearch(list, -1)); // => null
