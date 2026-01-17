[[Binary Search]]
Voice Note: "Recording 20250711082339.m4a" for google drive usage
![[Recording 20250711082339.m4a]]
Question 852)Peak index in a Montain Array
![[Pasted image 20250711085502.png]]
![[Pasted image 20250711085518.png]]
```
package krsnaSolved;  
  
public class mountainarrayleetcode {  
    //Bitonic Array  
    public static void main(String[] args) {  
        int[] arr = {0,2,1,0};  
        //Find the Peak largest value in the array list  
        System.out.println(peakIndexInMountainArray(arr));  
        //our answer is index:1  
    }  
    public int peakIndexInMountainArray(int[] arr){  
        int start = 0;  
        int end = arr.length - 1;  
        while(start < end){  
            int mid = start + (end - start)/2;  
            if(arr[mid] > arr[mid+1]){  
                end = mid;  
            }            else{  
                start = mid + 1;  
            }        }return start;  
    }  
}
```
==Search in Mountain array==
**LeetCode Hard**
You may recall that an array `arr` is a **mountain array** if and only if:

- `arr.length >= 3`
- There exists some `i` with `0 < i < arr.length - 1` such that:
    - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`
    - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

Given a mountain array `mountainArr`, return the **minimum** `index` such that `mountainArr.get(index) == target`. If such an `index` does not exist, return `-1`.

**You cannot access the mountain array directly.** You may only access the array using a `MountainArray` interface:

- `MountainArray.get(k)` returns the element of the array at index `k` (0-indexed).
- `MountainArray.length()` returns the length of the array.

Submissions making more than `100` calls to `MountainArray.get` will be judged _Wrong Answer_. Also, any solutions that attempt to circumvent the judge will result in disqualification.
![[Pasted image 20250711100645.png]]
Steps to solve:
- Find the Peak Element
- Binary search from start to Position of Peak element(Ascending)
- if not found move start to Peak element position and end and perform binary search Operation
```
package krsnaSolved;  
  
public class SearchInMoutainArray {  
    public static void main(String[] args) {  
        int[] arr = {0,1,2,3,5,4,1,0};  
        //Find the Peak largest value in the array list  
        int target = 4;  
        System.out.println(search(arr,target));  
        //our answer is index:1  
    }  
  
    static int search(int[] arr, int target){  
        int peak = peakIndexInMountainArray(arr);  
        int firstTry = orderChecker(arr,target,0,peak);  
        if(firstTry != -1){  
            return firstTry;  
        }return orderChecker(arr,target,peak+1,arr.length-1);  
  
    }  
    public static int peakIndexInMountainArray(int[] arr){  
        int start = 0;  
        int end = arr.length - 1;  
        while(start < end){  
            int mid = start + (end - start)/2;  
            if(arr[mid] > arr[mid+1]){  
                //we are in descending part of answer so may be the answer  
                end = mid;  
            }            else{  
                //we are in ascending part of the array  
                start = mid + 1;  
            }            //start == end {so it means that is the maximum element in each case checks above}  
        }return start;  
    }    static int orderChecker(int[] arr, int target,int start,int end){  
        //Find whether the Array is ascending or descending  
        boolean isAscending = arr[start]<arr[end];  
  
        while(start <= end){  
            int mid = start + (end - start)/2;  
            if (arr[mid] == target){  
                return mid;  
            }            if(isAscending){  
                if(target > arr[mid]){  
                    start = mid + 1;  
                }                else{  
                    end = mid -1;  
                }            }            else {  
                if(target < arr[mid]){  
                    start = mid + 1;  
                }                else{  
                    end = mid -1;  
                }            }        }return -1;  
    }}
```

