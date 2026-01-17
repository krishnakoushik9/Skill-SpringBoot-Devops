A block of code or snippet inside it is called Function
![[Pasted image 20250708052002.png]]==This is very inefficient so we use function's==

![[Pasted image 20250708053341.png]]
**Here i created a function called solution**
- which then i called in the main function this improves code readability and any modifications will also get easier
==Using Parameters:==
![[Pasted image 20250708061436.png]]
**Parameters in Java Methods**

In Java, methods can accept values from outside when they are called. These values are passed using _parameters_. Parameters make methods flexible and reusable by allowing different inputs to be processed by the same method.

There are two main types of parameters:

1. **Formal Parameters**  
    These are the variable names declared in the method definition. They serve as placeholders for the actual values that will be passed.
    

Example:  
static int add(int a, int b)  
In this example, 'a' and 'b' are formal parameters. They exist only within the method and are used to perform operations.

2. **Actual Parameters (or Arguments)**  
    These are the real values passed to the method when it is called.
    

Example:  
int result = add(10, 20);  
Here, 10 and 20 are actual parameters. They are passed into the method and assigned to the formal parameters 'a' and 'b' respectively.

Using parameters allows you to reuse methods multiple times with different data, instead of hardcoding values each time.

---

**Example Explanation**

public class Example  
{  
public static void main(String[] args)  
{  
greet("Krishna");  
}static void greet(String name)  
{  
    System.out.println("Hello, " + name);  
}  
}

In the above example:

- The method 'greet' takes a single formal parameter called 'name'.
    
- When the method is called using greet("Krishna"), the actual parameter "Krishna" is passed into the method.
    
- As a result, the output is: Hello, Krishna

==Parameters for Strings==
![[Pasted image 20250708062628.png]]
**==Swapping of Numbers using temp==**
![[Pasted image 20250708063051.png]]
Same Swap code but now we used a Function with parameters: ![[Pasted image 20250708063405.png]]
Scope basically means you can't access other function's values into one another :
![[Pasted image 20250708070730.png]]

