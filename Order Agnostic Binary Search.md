![[Pasted image 20250710091347.png]]
See Previously has done in [[Binary Search]]
- The given array was in sorted way of Ascending but what if now the array is descending then simple we follow the order-agnostic method of Binary search so what is does is it will apply binary search modifying it's logic based on ascending or descending
arr = [99,87,73,65,53,43,21,10,2]
![[Pasted image 20250710094110.png]]
```
package krishnayt;  
  
public class OderAgnosticBinarySearch {  
    public static void main(String[] args) {  
        int[] arr = {99,87,73,65,53,43,21,10,2};  
        int target = 21;  
        int ans = orderChecker(arr,target);  
        System.out.println(ans);  
    }  
    static int orderChecker(int[] arr, int target){  
        int start = 0;  
        int end = arr.length - 1;  
  
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
---
