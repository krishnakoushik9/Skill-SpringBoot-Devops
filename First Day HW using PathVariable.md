![[Pasted image 20250630103545.png]]
Below is the Code using PathVariable:
```
package com.legion.learning.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController; 

@RestController
@RequestMapping("/math")

public class Maths {
@GetMapping("/sum/{a}/{b}")
public int sum(@PathVariable int a, @PathVariable int b) {
return a + b;
}

@GetMapping("/sub/{a}/{b}")

public int sub(@PathVariable int a, @PathVariable int b) {

return a - b;

}

  

@GetMapping("/mul/{a}/{b}")

public int mul(@PathVariable int a, @PathVariable int b) {

return a * b;

}

  

@GetMapping("/div/{a}/{b}")

public int div(@PathVariable int a, @PathVariable int b) {

return b == 0 ? 0 : a / b;

}

}
```
[[Day 1 Homework Code]]
The URL have now changed instead of using :
http://localhost:8080/math/Division?a=10&b=5
We start using :
http://localhost:8080/math2/sum/10/5
The Output of it is has Follows:
![[Pasted image 20250630103939.png]]

