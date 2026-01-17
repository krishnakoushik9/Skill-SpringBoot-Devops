public static int cyclicSort(int[] arr){  
    int i = 0;  
    int n = arr.length;  
    while(i < n){  
        int correct = arr[i] - 1;  
        if(arr[i] >= 1 && arr[i]<= n && arr[i] != arr[correct]){  
            swap(arr,i,correct);  
        }else{  
            i++;  
        }    }    for (int j = 0;j < n;j++){  
        if(arr[j]!=j+1){  
            return j + 1;  
        }    }return n+1;  
}  
public static void swap(int[] arr, int a, int b){  
    int temp = arr[a];  
    arr[a] = arr[b];  
    arr[b] = temp;  
}

![[Pasted image 20250712220745.png]]
LeetCode Submission
![[Pasted image 20250712220816.png]]


