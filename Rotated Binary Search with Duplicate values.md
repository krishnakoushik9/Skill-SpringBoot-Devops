[[Amazon Interview Question]]
```
package krsnaSolved;  
  
public class RotatedArrayDuplicateElements {  
    public static void main(String[] args) {  
        int[] arr = {4, 5, 6, 7,0,0, 1,1,1,2,2};  
        int target = 0;  
  
        int result = search(arr, target);  
        System.out.println(result);  
    }    public static int search(int[]arr,int target){  
        int pivot = findPivotDuplicate(arr);  
        if(pivot == -1){  
            return binarySearch(arr,target,0,arr.length-1);  
        }        if(arr[pivot] == target){  
            return pivot;  
        }        if(target >= arr[0]){  
            return binarySearch(arr,target,0,pivot);  
        }        else{  
            return binarySearch(arr,target,pivot+1,arr.length-1);  
        }  
    }    public static int binarySearch(int[] arr,int target,int start,int end){  
        while(start <= end){  
            int mid = start + (end - start)/2;  
            if(target == arr[mid]){  
                return mid;  
            }            else if(target > arr[mid]){  
                start = mid + 1;  
            }else {  
                end = mid - 1;  
            }        }return -1;  
    }  
    public static int findPivotDuplicate(int[] arr){  
        int start = 0;  
        int end = arr.length - 1;  
        while(start <= end){  
            int mid = start + (end - start)/2;  
            if(mid < end && arr[mid] > arr[mid + 1]){  
                return mid;  
            }            if(mid > start && arr[mid] < arr[mid - 1]){  
                return mid - 1;  
            }            //Below will conflict with Duplicate elements  
            /*if(arr[start]<=arr[mid]){                start = mid + 1;            }            else{                end = mid -1;            }*/            //Now we wanna make sure it skips the duplicates            if(arr[mid]==arr[start] && arr[mid] == arr[end]){  
                if(arr[start] > arr[start+1]){  
                    return start;  
                }start++;  
                if(arr[end] < arr[end - 1]){  
                    return end;  
                }                end --;  
            }            else if(arr[start] < arr[mid] || arr[start] == arr[mid] && arr[mid]>arr[end]){  
                start = mid + 1;  
            }else{  
                end = mid -1;  
            }        }        return -1;  
    }  
}
```

The key difference between normal Pivot based Rotation search vs this array which has duplicate values
![[Pasted image 20250711213754.png]]
The above section of Code works in such a way:
- cause the array now is int[] arr = {4, 5, 6, 7,0,0, 1,1,1,2,2};
![[Pasted image 20250711214616.png]]
for this issue not to arise we developed
```if(arr[mid]==arr[start] && arr[mid] == arr[end]){  
    if(arr[start] > arr[start+1]){  
        return start;  
    }start++;  
    if(arr[end] < arr[end - 1]){  
        return end;  
    }    end --;  
}  
else if(arr[start] < arr[mid] || arr[start] == arr[mid] && arr[mid]>arr[end]){  
    start = mid + 1;  
}else{  
    end = mid -1;  
}
```
Byeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee