[[Amazon Interview Question]]
**This question is asked in both Google and Amazon Interview**
There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return _the index of_ `target` _if it is in_ `nums`_, or_ `-1` _if it is not in_ `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

**Input:** nums = [4,5,6,7,0,1,2], target = 0
**Output:** 4

**Example 2:**

**Input:** nums = [4,5,6,7,0,1,2], target = 3
**Output:** -1

**Example 3:**

**Input:** nums = [1], target = 0
**Output:** -1

![[Pasted image 20250711130631.png]]

==The main thing to note is==
**All values of nums(An Array) are unique and do not repeat**
![[Pasted image 20250711144854.png]]
```
package krsnaSolved;  
  
public class SearchinsideRotatedArray {  
    public static void main(String[] args) {  
        int[] arr = {4, 5, 6, 7, 0, 1, 2};  
        int target = 0;  
  
        int result = search(arr, target);  
        System.out.println(result);  
    }  
    public static int search(int[] arr, int target) {  
        int pivot = findPivot(arr);  
  
        // Case 1: Array is not rotated  
        if (pivot == -1) {  
            return binarySearch(arr, target, 0, arr.length - 1);  
        }  
        // Case 2: Found target at pivot  
        if (arr[pivot] == target) {  
            return pivot;  
        }  
        // Case 3: Target is in left sorted portion  
        if (target >= arr[0]) {  
            return binarySearch(arr, target, 0, pivot - 1);  
        }  
        // Case 4: Target is in right portion  
        return binarySearch(arr, target, pivot + 1, arr.length - 1);  
    }  
    // Pivot finder  
    public static int findPivot(int[] arr) {  
        int start = 0;  
        int end = arr.length - 1;  
  
        while (start <= end) {  
            int mid = start + (end - start) / 2;  
  
            if (mid < end && arr[mid] > arr[mid + 1]) {  
                return mid;  
            }  
            if (mid > start && arr[mid] < arr[mid - 1]) {  
                return mid - 1;  
            }  
            if (arr[start] <= arr[mid]) {  
                start = mid + 1;  
            } else {  
                end = mid - 1;  
            }        }        return -1;  
    }  
    // Standard binary search with custom range  
    public static int binarySearch(int[] arr, int target, int start, int end) {  
        while (start <= end) {  
            int mid = start + (end - start) / 2;  
  
            if (target == arr[mid]) {  
                return mid;  
            } else if (target > arr[mid]) {  
                start = mid + 1;  
            } else {  
                end = mid - 1;  
            }        }        return -1;  
    }}
```

I spend nearly 3 hours only on this cause i was having issue with understanding this 