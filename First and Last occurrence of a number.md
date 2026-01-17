Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.
If `target` is not found in the array, return `[-1, -1]`.
You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**
**Input:** nums = [5,7,7,8,8,10], target = 8
**Output:** [3,4]

**Example 2:**
**Input:** nums = [5,7,7,8,8,10], target = 6
**Output:** [-1,-1]

**Example 3:**
**Input:** nums = [], target = 0
**Output:** [-1,-1]

-------

![[Pasted image 20250710184449.png]]
![[Pasted image 20250710184522.png]]
```
package krsnaSolved;  
  
import java.util.Arrays;  
  
public class first_lastpostionarray {  
    public static void main(String[] args) {  
        int[] arr = {5,7,7,8,8,10};  
        int target = 2;  
        int[] ans = searchRange(arr,target);  
        System.out.println(Arrays.toString(ans));  
    }    public static int[] searchRange(int[] arr, int target){  
        int start = 0;  
        int firstpos = -1;  
        int lastpos = -1;  
        int end = arr.length - 1;  
        while(start <= end){  
            int mid = start + (end - start)/2;  
            if(target > arr[mid]){  
                start = mid + 1;  
            }            else if(target < arr[mid]){  
                end = mid -1;  
            }            else if(arr[mid] == target) {  
                firstpos = mid;  
                end = mid -1;  
            }        }        start = 0;  
        end = arr.length - 1;  
        while(start <= end){  
            int mid = start + (end - start)/2;  
            if(target > arr[mid]){  
                start = mid + 1;  
            }            else if(target < arr[mid]){  
                end = mid -1;  
            }            else if(arr[mid] == target) {  
                lastpos = mid;  
                start = mid + 1;  
            }            if (firstpos == -1 || lastpos == -1) {  
                return new int[]{-1, -1};  
            }        }return new int[]{firstpos,lastpos};  
    }}
```
So this was not brute force method it was basically running two binary searches....

==That was a headace==
![[Pasted image 20250710185638.png]]
