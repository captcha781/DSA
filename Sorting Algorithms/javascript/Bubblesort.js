function bubbleSort(arr, n) {
  for (let i = 0; i < n - 1; i++) {
    for (let j = 0; j < n - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        let temp = arr[j + 1];
        arr[j + 1] = arr[j];
        arr[j] = temp;
      }
    }
  }
  return arr;
}

function recursiveBubbleSort(arr, n) {
  if (n == 1) return arr;
  for (let i = 0; i < n - 1; i++) {
    if (arr[i] > arr[i + 1]) {
      let temp = arr[i + 1];
      arr[i + 1] = arr[i];
      arr[i] = temp;
    }
  }
  return recursiveBubbleSort(arr, n - 1);
}

var arr = [64, 34, 25, 12, 22, 11, 90];
var n = arr.length;
console.log(recursiveBubbleSort(arr, n));
