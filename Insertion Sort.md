![[Pasted image 20250712170939.png]]
![[Pasted image 20250712171024.png]]
![[Pasted image 20250712174532.png]]
Worst case Time Complexity == 0(N^2)
Best Case is 0(N)
Below is the code for it :
package krsnaSolved;  
import java.util.Arrays;  
  
public class insertionSort {  
    public static void main(String[] args) {  
        int[] arr = {7,2,82,42,12,57,92,24,38,1};  
        staticResponce(arr);  
        System.out.println(Arrays.toString(arr));  
    }    static void staticResponce(int[] arr) {  
        for(int i = 0;i<arr.length-1;i++){  
            for(int j = i+1;j>0;j--){  
                if(arr[j]<arr[j-1]){  
                    swap(arr,j,j-1);  
                }else{  
                    break;  
                }            }        }    }   
                
static void swap(int[] arr, int a, int b) {  
        int temp = arr[a];  
        arr[a] = arr[b];  
        arr[b] = temp;  
    }}


![[Pasted image 20250712200632.png]]
