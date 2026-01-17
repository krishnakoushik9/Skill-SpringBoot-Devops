[[Bubble Sort]]
![[Pasted image 20250712143831.png]]
static void staticresponce(int[] arr) {  
    boolean swapped;  
    for(int i = 0 ;i<arr.length;i++){  
        swapped = false;  
        for(int j = 1;j <  arr.length - i;j++){  
            if(arr[j]<arr[j - 1]){  
                int temp = arr[j];  
                arr[j] = arr[j-1];  
                arr[j-1] = temp;  
                swapped = true;  
            }        
	    }if (!swapped)break;  
    }
   }
```
package krsnaSolved;  
  
import java.util.Arrays;  
//Bubble Sort  
public class sortarray {  
    public static void main(String[] args) {  
        int[] arr = {7,2,82,42,12,57,92,24,38,1};  
        staticresponce(arr);  
        System.out.println(Arrays.toString(arr));  
    }  
    static void staticresponce(int[] arr) {  
        boolean swapped;  
        for(int i = 0 ;i<arr.length;i++){  
            swapped = false;  
            for(int j = 1;j <  arr.length - i;j++){  
                if(arr[j]<arr[j - 1]){  
                    int temp = arr[j];  
                    arr[j] = arr[j-1];  
                    arr[j-1] = temp;  
                    swapped = true;  
                }            }if (!swapped)break;  
        }    }}
```
[[Selection Sort]]
[[Insertion Sort]]