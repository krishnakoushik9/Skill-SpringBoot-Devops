![[Pasted image 20250712144029.png]]
So that is selection sort
![[Pasted image 20250712171224.png]]
```
static void selectionSort(int[] arr) {  
    int size = arr.length;  
    for (int i = 0; i < size - 1; i++) {  
        int minIndex = i;  
        // Find the index of the minimum element in the remaining array  
        for (int j = i + 1; j < size; j++) {  
            if (arr[j] < arr[minIndex]) {  
                minIndex = j;  
            }        }        // Swap the found minimum element with the first element  
        if (minIndex != i) {  
            int temp = arr[minIndex];  
            arr[minIndex] = arr[i];  
            arr[i] = temp;  
        }    }}
        
```
