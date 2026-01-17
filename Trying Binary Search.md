![[Pasted image 20250709215843.png]]
It's nowhere near to be correct of complete algorithm but this is the starting point from what i understood i am wrong or right makes a lot of sense

Worst Time complexity will be : log(n)
![[Pasted image 20250709221106.png]]
```
public static void main(String[] args) {  
    long start = System.nanoTime();  
    int[] arr = {-18,-7,0,1,4,12,23,35,44,58,72,91};  
    int target = 72;  
    int ans = binarySearch(arr,target);  
    System.out.println(ans);  
    long end = System.nanoTime();  
    System.out.println("Time taken (ms): " + (end - start) / 1_000_000.0);  
}
```
 Above was the Main Function
```
static int binarySearch(int[] arr,int target){  
    int start = 0;  
    int end = arr.length - 1;  
    while(start <= end){  
        int mid = start + (end - start)/2;  
        if(target > arr[mid]){  
            start = mid + 1;  
        }        if(target < arr[mid]){  
            end = mid -1;  
        }        else {  
            return mid;  
        }    }return -1;  
}
```
That was the Function which did the search operation

![[Pasted image 20250709233416.png]]
==It is also updates on Github Repo also==
![[Pasted image 20250709233452.png]]
The repo link is : https://github.com/krishnakoushik9/Intellij-Java/
