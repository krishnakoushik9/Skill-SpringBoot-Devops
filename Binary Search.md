What is Binary search:
- **Binary Search** is a **divide-and-conquer** algorithm that repeatedly divides the search interval in half. It compares the target value to the **middle element** of the array
- If they match, the search is complete.
- If the target is **less than** the middle element, it continues the search in the **left half**.
- If the target is **greater than** the middle element, it continues the search in the **right half**.
This process repeats until the value is found or the interval becomes empty.
---
Let's assume Array - arr
arr = {1,4,23,26,43,72,91}
Sorted in ascending order 
So let's say we are doing linear search the way it searches is from 
for(int i = 0;i<arr.length;i++)
Meaning it moves ->->->->-> Until the target integer is found
but this rises the worst time complexity of 0(n) at worst so a efficient search algorithm is Binary search

==Binary Search==
is brakes the array in half and based on value of middle value it will think either to search left half or right and then that half is again halved and the process is repeated until the desired Target Integer is found

```
Syntax or code of an Iterative version
public class BinarySearchExample {
    public static int binarySearch(int[] arr, int target) {
        int start = 0;
        int end = arr.length - 1;

        while (start <= end) {
            int mid = start + (end - start) / 2;  // safer than (start + end)/2

            if (arr[mid] == target) {
                return mid; // target found
            } else if (arr[mid] < target) {
                start = mid + 1; // search right half
            } else {
                end = mid - 1; // search left half
            }
        }

        return -1; // target not found
    }

    public static void main(String[] args) {
        int[] arr = {2, 4, 6, 8, 10, 12, 14};
        int target = 10;

        int result = binarySearch(arr, target);
        if (result != -1) {
            System.out.println("Element found at index: " + result);
        } else {
            System.out.println("Element not found.");
        }
    }
}

```
[[Trying Binary Search]]
[[Order Agnostic Binary Search]]
[[First and Last occurrence of a number]]

