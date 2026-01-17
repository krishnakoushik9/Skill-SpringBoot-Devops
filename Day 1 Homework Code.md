Using ==RestController==
package com.legion.learning.demo;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/math")
public class Maths {
@GetMapping("/sum")
public int sum(int a, int b)
{
return a + b;
}
@GetMapping("/sub")
public int sub(int a,int b)
{
return a - b;
}
@GetMapping("/mul")
public int mul(int a,int b)
{
return a * b;
}
@GetMapping("/Division")
public int Division(int a,int b)
{
return a / b;
}
}
Screen shot has been added
![[Pasted image 20250630101459.png]]
The ouput :
[[Day 1 H.W Output using RestController]]
