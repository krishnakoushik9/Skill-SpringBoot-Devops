![[Pasted image 20250708221518.png]]
**Find whether 14 exists in Array or not**
- arr = [18,12,9,14,77,50]
==Time Complexity==
- Best case of Time Complexity is : 0(1)
- Worst case of Time Complexity is : 0(N) {N = Size of Array}
Below is out Example of Linear Search
![[Pasted image 20250708224848.png]]

------------
Trying to understand the linear search 
basically 
[][][][][][][][][][][]
Let the above boxes be memory location's of our arrays
[]<-So the search the first box and then continue until the required number value is caught
->input from user = ==Target==
->Create a loop to iterate the linear search of all the array values to search       for the target
**Jenny's Lecture**
![[Pasted image 20250709083952.png]]
Array given = **15,5,20,35,2,42,67,17**
search for ==42==
![[Pasted image 20250709084406.png]]
The code which is written by me is:
![[Pasted image 20250709084935.png]]
Similar to what https://www.youtube.com/watch?v=_HRA37X8N_Q&list=PL9gnSGHSqcnr_DxHsP7AW9ftq0AtAyYqJ&index=13
Kunal has said heheeee

---
Search char in a String
![[Pasted image 20250709091415.png]]
```
package krishnayt;  
  
public class SearchInStrings {  
    public static void main(String[] args) {  
        String name = "Krishna";  
        char tsearch = 'i';  
        System.out.println(search(name,tsearch));  
    }    static boolean search(String str,char tsearch){  
        for(int i = 0 ;i<str.length();i++){  
            if(tsearch == str.charAt(i))  
            {                return true;  
            }        }        return false;  
    }}
```
![[Pasted image 20250709092248.png]]
||Something which i tried to write||

----
Range Question:
![[Pasted image 20250709095732.png]]
```
package krishnayt;  
  
public class RangeSearch {  
    public static void main(String[] args) {  
        int[] arr = {1, 3, 6, 7, 8, 33, 2, -1};  
        int target = 33;  
        int start = 1;  
        int end = 6;  
        int ans = linearSearch(arr, target,start,end);  
        System.out.println("Target number found at: "+ans + " in range of " + start + "&" + end);  
    }    static int linearSearch(int[] arr, int target,int start,int end) {  
        int i;  
        for (i = start; i < end; i++) {  
            if (arr[i] == target) {  
                return i;  
            }        }        return -1;  
    }}
```

----
Minimum of an Array
![[Pasted image 20250709101355.png]]
```
package krishnayt;  
  
public class FIndMin {  
    public static void main(String[] args) {  
        int[] arr = {1, 3, 6, 7, 8,-1, 33, 2, -11};  
        int Min = MinSearch(arr);  
        System.out.println(Min);  
    }  
    static int MinSearch(int[] arr){  
        int ans = arr[0];  
        for (int i = 1;i<arr.length;i++){  
            if (arr[i] < ans){  
                ans = arr[i];  
  
            }        }        return ans;  
    }}
```

---
==Search in 2d Array==
![[Pasted image 20250709142924.png]]
```
package krishnayt;  
  
import java.util.Arrays;  
import java.util.Scanner;  
  
public class SeachIn2dArray {  
    public static void main(String[] args) {  
        int[][] arr = {  
                {23,4,1},  
                {3,6,4,8},  
                {12,88}  
        };        Scanner in = new Scanner(System.in);  
        int target = in.nextInt();  
        int[] ans = search(arr,target);  
        System.out.println(Arrays.toString(ans));  
        in.close();  
    }    static int[] search(int[][] arr, int target){  
        int row;  
        int col;  
        for(row = 0;row<arr.length;row++){  
            for(col = 0;col < arr[row].length;col++){  
                if(arr[row][col]==target){  
                    return new int[]{row,col};  
                }            }        }        return new int[]{-1,-1};  
    }}
```
----
==static int printer(int[][] arr){  
   for(int [] row:arr){  
       for(int val : row){  
           System.out.print(val + " ");  
       }   }System.out.println();  
   return -1;  
}==
**The above code can be used to print the 2d Array in a single line**
