![[Pasted image 20250708120920.png]]
```
package krishnayt;  
import java.util.Arrays;  
import java.util.Scanner;  
public class arrayinput {  
    public static void main(String[] args) {  
        String[] arr = new String[5];  
        Scanner in = new Scanner(System.in);  
        // Input values using index-based for loop  
        for(int i = 0; i < arr.length; i++) {  
            arr[i] = in.next();  
        }        System.out.println(Arrays.toString(arr));  
        in.close();  
    }}
```

SImple difference is instead of using Int use String
but always remember for best output use
==Arrays.toString(arr)==
