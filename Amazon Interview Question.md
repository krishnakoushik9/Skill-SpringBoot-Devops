[[Interview Questions]]
![[Pasted image 20250710215345.png]]
```
package krsnaSolved;  
  
import java.util.Arrays;  
  
public class InfiniteArray {  
    public static void main(String[] args) {  
        int[] arr = {2,3,4,5,12,23,35,44,51,67,88,91,99};  
        int target = 51;  
        System.out.println(range(arr,target));  
    }  
    static int range(int[] arr, int target) {  
        int start = 0;  
        int end = 1;  
        while (true) {  
            try {  
                if (target <= arr[end]) break;  
                int new_start = end + 1;  
                end = end + (end - start + 1) * 2;  
                start = new_start;  
            } catch (ArrayIndexOutOfBoundsException e) {  
                // Simulate: We've hit the "end" of our infinite world  
                break;  
            }        }        return infiniteArray(arr, target, start, end);  
    }  
    static int infiniteArray(int[] arr,int target,int start,int end){  
  
        while(start <= end){  
            int mid = start + (end - start)/2;  
            if(target > arr[mid]){  
                start = mid + 1;  
            }            else if(target < arr[mid]){  
                end = mid -1;  
            }            else {  
                return mid;  
            }        }return -1;  
    }}
```

==This is it the logic for this to work it's nothing more than a Binary Search==
![[Pasted image 20250710215455.png]]
```
static int range(int[] arr, int target) {  
    int start = 0;  
    int end = 1;  
    while (true) {  
        try {  
            if (target <= arr[end]) break;  
            int new_start = end + 1;  
            end = end + (end - start + 1) * 2;  
            start = new_start;  
        } catch (ArrayIndexOutOfBoundsException e) {  
            // Simulate: We've hit the "end" of our infinite world  
            break;  
        }    }    return infiniteArray(arr, target, start, end);  
}
```
The error we faced is the code logic given and explained by **Kunal** did not have **ArrayIndexOutOfBoundsException** reason is his example was simpler but i really loved his approach to solve it 
[][][][][][][][][][][] <- how he did it was basically dividing the array into size chunks and then applying binary search
![[Pasted image 20250710215827.png]]
This is not the end of his class but i wanna sleep
it's 10:00PM
So chalo guys (I am not really expecting ppl to read all these but hey it's for me kadha ra)
- it is already pushed to github repo this is the [link](https://github.com/krishnakoushik9/Assignments-krsnaSolved/tree/master/src/krsnaSolved)
 