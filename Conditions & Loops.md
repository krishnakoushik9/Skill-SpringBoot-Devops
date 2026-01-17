==Example:1==
![[Pasted image 20250707185009.png]]
```
import java.util.Scanner;  
  
public class Conditionals {  
    public static void main(String[] args) {  
        Scanner scanner = new Scanner(System.in);  
        int salary;  
        int bonus = 2000;  
        int bonus2 = 1000;  
        salary = scanner.nextInt();  
        if(salary > 10000){  
            System.out.println("Bonus of 2000 is given");  
            salary += bonus;  
            System.out.println(salary);  
        }        else  
        {  
            salary += bonus2;  
            System.out.println("Bonus of 1000 is given");  
            System.out.println(salary);  
        }        scanner.close();  
    }}
```
==Example 2==
For loop:
```
public class loops {  
    public static void main(String[] args) {  
        //Print numbers from 1 to 5  
        for(int i = 1; i<=5 ; i++)  
        {            System.out.println(i);  
        }  
    }}
```
![[Pasted image 20250707191405.png]]
==example 3==
dynamic input for loop 
![[Pasted image 20250707191730.png]]
```
import java.util.Scanner;  
  
public class loops {  
    public static void main(String[] args) {  
        //Print numbers from 1 to n  
        int n;  
        Scanner scanner = new Scanner(System.in);  
        n = scanner.nextInt();  
        for(int i = 1; i<=n ; i++)  
        {            System.out.println(i);  
        }    scanner.close();  
    }}
```

**==While loop==**
![[Pasted image 20250707192418.png]]
- if you dont know how many times a loop needs to run then we need to use a while loop
==Problem using Conditionals==
![[Pasted image 20250707210716.png]]
