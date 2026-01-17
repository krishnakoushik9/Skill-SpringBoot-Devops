Leetcode medium still using -> [[Binary Search]]

![[Pasted image 20250712111614.png]]

----
So how will we solve this:
![[Pasted image 20250712114046.png]]
![[Pasted image 20250712114055.png]]
```
static boolean search(int[][] matrix,int target){  
    int row = 0;  
    int col = matrix[0].length - 1;  
    while(row < matrix.length && col >= 0){  
        if(matrix[row][col] == target){  
            return true;  
        }        if(matrix[row][col] < target){  
            row ++;  
        }else{  
            col --;  
        }    }return false;  
}
```

Below is the Video Explanation: 

![[2025-07-12-114233.webm]]
