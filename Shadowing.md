**Shadowing in Java** refers to a situation where a variable declared within a certain scope (like a method or a constructor) has the **same name** as a variable declared in an **outer scope** (like a class-level field). The inner variable "shadows" or hides the outer one within that scope.
```
public class Employee {
    int salary = 50000;  // Class-level field

    void setSalary(int salary) {
        // The parameter 'salary' shadows the class field 'salary'
        this.salary = salary;  // 'this.salary' refers to the class field
    }
}
```
-----------
![[Pasted image 20250708091706.png]]
Basically using 2 variables with same name within the same scope
