The Homework [[First Homework]]
Below is my first issue:
[[Error Output]]
The Process of Solving it learnt that 
the Controller1.java and Maths.java
{These both controller's were using same 8080 port and were having a Conflict}
I Did not solve it completely but what i did was 
to add : ==**@RequestMapping("/math")**==
and ==**import org.springframework.web.bind.annotation.RequestMapping;**==
which made sure that port will now be explicitly being done from math route
![[Pasted image 20250630101252.png]]
Which has Solved it and made sure the error is fixed
[[Day 1 Homework Code]]


