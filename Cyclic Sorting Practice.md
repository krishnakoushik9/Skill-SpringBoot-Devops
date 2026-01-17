```
public static void cyclicSort(int[] arr){  
    int i = 0;  
    while(i < arr.length){  
        int correct = arr[i] - 1;  
        if(arr[i] != arr[correct]){  
            swap(arr,i,correct);  
        }else{  
            i++;  
        }    }}
```

![[Pasted image 20250712204738.png]]

---
Video Explaination below:
[[2025-07-12-204808.webm]]
