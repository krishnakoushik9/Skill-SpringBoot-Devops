# Recursion in Java

## What is Recursion?

**Recursion** is a process in which a method calls itself to solve smaller instances of a problem. It is used when a problem can be divided into similar sub-problems.

---
![[Pasted image 20250721155208.png]]
## Where is Recursion Used?

- **Mathematical computations** (e.g., factorial, Fibonacci series)
- **Tree and graph traversals**
- **Backtracking problems** (e.g., maze solving, N-Queens)
- **Divide and conquer algorithms** (e.g., Merge Sort, Quick Sort)
- **Dynamic Programming (with memoization)**

---

## How is Recursion Used?

1. Define a method that calls itself.
2. Always include a **base case** to stop the recursion.
3. Each recursive call should progress towards the base case.

---

## Important Keywords/Concepts

- **Base Case**: A condition to stop further recursive calls.
- **Recursive Case**: The part where the function calls itself.
- **Stack Overflow**: Happens if recursion goes too deep (no base case or incorrect logic).
- **Call Stack**: Java uses a call stack to manage recursive method calls.
- **Tail Recursion** (advanced): A form of recursion where the recursive call is the last action.

---

## Summary

Recursion helps simplify complex problems by solving smaller parts of the same problem using the same logic. It should be used carefully to avoid infinite loops or memory overflows.
[[Recursions - Complete]]
[[Notes-Recursions.pdf]]
[[Kunal Kushwaha]]


