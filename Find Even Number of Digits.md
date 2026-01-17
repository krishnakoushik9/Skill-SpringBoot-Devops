![[Pasted image 20250709151122.png]]
**Question 1)**
->We need to find numbers inside the array which are even in count 
- Meaning example 18,1764,98
->First we make a count = 0 (Cause we still did not meet a even size number)
![[Pasted image 20250709152705.png]]
```
package KunalDSA;  
  
public class EvenNumbers {  
    public static void main(String[] args) {  
        int[] arr = {18, 124, 9, 1764, 98, 1};  
        System.out.println(countEvenDigitNumbers(arr));  
    }  
    static int countEvenDigitNumbers(int[] arr) {  
        int count = 0;  
        for (int num : arr) {  
            if (String.valueOf(num).length() % 2 == 0) {  
                count++;  
            }        }        return count;  
    }}
```
