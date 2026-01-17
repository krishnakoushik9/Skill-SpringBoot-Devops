[[Training]]
1st Problem:
Change first,last,second last:
```
package krsnaSolved;  
  
public class enhancedFirstAndLast {  
    public static void main(String[] args) {  
        System.out.println(changeSecondLast(3462));  
        System.out.println(changeLast(3462));  
        System.out.println(changeFirst(3670));  
    }    public static int changeSecondLast(int n){  
        int l = n % 10;  
        n = n - (n%100);  
        n = n + l + 8 * 10;  
        return n;  
    }    public static int changeLast(int n){  
        n = n - n % 10;  
        n = n + 5;  
        return n;  
    }    public static int changeFirst(int n){  
        int a = (int) (Math.log10(n) + 1);  
        int b = (int) (n % Math.pow(10,a-1));  
        b = (int) (b + 2 * Math.pow(10,a-1));  
        return b;  
    }}
```

2nd Problem Find next unique year:
```
package krsnaSolved;  
//Cantilever Training  
public class findYear {  
    public static void main(String[] args) {  
        System.out.println(findNextYear(1800));  
    }    public static int findNextYear(int year){  
        year += 1;  
        while(!isUniqueYear(year)){  
            year ++;  
        }        return year;  
    }    public static boolean isUniqueYear(int year){  
        int l = year % 10;  
        int ls = (year % 100 / 10);  
        int fs = (year % 1000 /100);  
        int f = (year % 10000/1000);  
        return f != ls && f != fs && f != l && fs != ls && fs != l && ls != l;  
    }}
```

Array Reversal Question:
```
package krsnaSolved;  
  
import java.util.Arrays;  
  
public class arrayReversal {  
    public static void main(String[] args) {  
        int[] arr = {1,2,3,4,5,6,7,8,9};  
        int[] ans = arrayReversalMethod(arr);  
        System.out.println(Arrays.toString(ans));  
    }  
    public static int[] arrayReversalMethod(int[] arr) {  
        int left = 0;  
        int right = arr.length - 1;  
        while (left < right) {  
            // Swap characters  
            if(arr[left] % 2 == 0 && arr[right] % 2 == 0){  
                int temp = arr[left];  
                arr[left] = arr[right];  
                arr[right] = temp;  
            }            left ++;  
            right --;  
        }        return arr;  
    }  
}
```

Move even Numbers in array to start:
```
package krsnaSolved;  
  
import java.util.Arrays;  
  
public class moveEven {  
    public static void main(String[] args) {  
        int [] arr = {2, 3, 6, 8, 5, 9, 4};  
        System.out.println(Arrays.toString(evenFirstSwap(arr)));  
    }  
    public static int[] evenFirstSwap(int[] arr) {  
        int left = 0;  
        int right = arr.length - 1;  
  
        while (left < right) {  
            if (arr[left] % 2 != 0 && arr[right] % 2 == 0) {  
                swap(arr, left, right);  
                left++;  
                right--;  
            }            if (arr[left] % 2 == 0) {  
                left++;  
            }            if (arr[right] % 2 != 0) {  
                right--;  
            }        }        return arr;  
    }  
    public static void swap(int[] arr, int i, int j) {  
        int temp = arr[i];  
        arr[i] = arr[j];  
        arr[j] = temp;  
    }}
```