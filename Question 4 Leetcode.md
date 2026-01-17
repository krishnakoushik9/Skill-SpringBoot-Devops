![[Pasted image 20250720180054.png]]
```
package krsnaSolved;  
  
public class MedianofTwoSortedArraysNOTOPTMISED {  
    public static void main(String[] args) {  
        int[] arr1 = {1,2,5};  
        int[] arr2 = {3,4,9};  
        int[] merged = nonoptimisedsol(arr1, arr2);  
        sort(merged);  
        double ans = mid(merged);  
        System.out.println(ans);  
    }    public static int[] nonoptimisedsol(int[] arr1,int[] arr2){  
        //let's sort it here  
        int[] result = new int[arr1.length + arr2.length];  
        for(int i = 0;i< arr1.length;i++){  
            result[i] = arr1[i];  
        }        for(int i = 0;i< arr2.length;i++){  
            result[arr1.length + i] = arr2[i];  
        }        return result;  
    }    public static void sort (int[] result){  
        for(int i = 0;i<result.length - 1;i++){  
            for(int j = 0;j < result.length - i - 1;j++){  
                if (result[j] > result[j+1]){  
                    swap(result,j,j+1);  
                }            }        }    }    public static void swap(int[] result,int a,int b){  
        int temp = result[a];  
        result[a] = result[b];  
        result[b] = temp;  
    }    public static double mid(int[] result){  
        int n = result.length;  
        if (n % 2 == 0) {  
            return (result[n / 2] + result[n / 2 - 1]) / 2.0;  
        } else {  
            return result[n / 2];  
        }    }}
```


The code above is very unoptimised
feat: add brute-force solution for finding median of two sorted arrays  
- Implemented array concatenation method to merge two input arrays  
- Added bubble sort logic to sort the merged array  
- Added swap helper method for sorting  
- Calculated median based on even/odd length of sorted array  
- Current solution runs in O((m+n)^2) time due to bubble sort

> [!NOTE] With the Un-Optimized version the runtime was 28ms which is very bad
> ![[Pasted image 20250720182107.png]]

## Code :
```
class Solution {

public double findMedianSortedArrays(int[] nums1, int[] nums2) {

int[] merged = mergeArrays(nums1, nums2);

sort(merged);

return getMedian(merged);

}

  

private int[] mergeArrays(int[] arr1, int[] arr2) {

int[] result = new int[arr1.length + arr2.length];

for (int i = 0; i < arr1.length; i++) {

result[i] = arr1[i];

}

for (int i = 0; i < arr2.length; i++) {

result[arr1.length + i] = arr2[i];

}

return result;

}

  

private void sort(int[] arr) {

for (int i = 0; i < arr.length - 1; i++) {

for (int j = 0; j < arr.length - i - 1; j++) {

if (arr[j] > arr[j + 1]) {

swap(arr, j, j + 1);

}

}

}

}

  

private void swap(int[] arr, int a, int b) {

int temp = arr[a];

arr[a] = arr[b];

arr[b] = temp;

}

  

private double getMedian(int[] arr) {

int n = arr.length;

if (n % 2 == 0) {

return (arr[n / 2] + arr[n / 2 - 1]) / 2.0;

} else {

return arr[n / 2];

}

}

}
```
![[Pasted image 20250720182539.png]]
