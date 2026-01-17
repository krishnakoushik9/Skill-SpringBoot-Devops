[[Binary Search]]
![[Pasted image 20250711081142.png]]
```
private static boolean searchMatrix(int[][] matrix, int target) {  
    int start = 0;  
    int m = matrix.length;  
    int n = matrix[0].length;  
    int end = m * n -1;  
    int cols = matrix[0].length;  
    while(start <= end){  
        int mid = start + (end - start)/2;  
        if(target>matrix[mid / cols][mid % cols]){  
            start = mid + 1;  
        }        else if (target <matrix[mid / cols][mid % cols]){  
            end = mid - 1;  
        }        else {  
            return true;  
        }    }return false;  
}
```
----
It worked adey magic
but this was the code i submitted
![[Pasted image 20250711081543.png]]
