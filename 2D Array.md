initialization = int[][]arr = new int[][]![[Pasted image 20250708204005.png]]
Individual size of those arrays can be different also

==Input of Array==
&
==Output of Array==
![[Pasted image 20250708211002.png]]
```
package krishnayt;  
  
import java.util.Arrays;  
import java.util.Scanner;  
  
public class arraylist {  
    public static void main(String[] args) {  
        Scanner scanner = new Scanner(System.in);  
        int m = scanner.nextInt();  
        int n = scanner.nextInt();  
        int arr2d[][] = new int[m][n];  
        //input  
        for (int i = 0;i<m;i++){  
            for(int j = 0;j<n;j++){  
                arr2d[i][j] = scanner.nextInt();  
            }        }        //output  
        for (int i = 0;i<m;i++){  
            for(int j = 0;j<n;j++){  
                System.out.print(arr2d[i][j] + " ");  
            }            System.out.println();  
        }        scanner.close();  
    }}
```
- **Yes i get it it's weird but yea we need to concentrate a lot on how to work on loops**
hey we get better output look when we use the below:
![[Pasted image 20250708211537.png]]
```
for (int i = 0; i < m; i++) {  
    /*for (int j = 0; j < n; j++) {  
        System.out.print(arr2d[i][j] + " ");    }    System.out.println();*/    System.out.println(Arrays.toString(arr2d[i]));  
}
```
->This makes sure the output of array is graphically also better.
**==Enhanced For Loop**==
![[Pasted image 20250708211919.png]]
```
for (int[] a: arr2d){  
    System.out.println(Arrays.toString(a));  
}
```
[[Array-List]]