### Pre-requisites of how functions work
![[Pasted image 20250715194310.png]]
![[Untitled-2025-07-13-2232.excalidraw_2025-07-15_14_31_16.820058.png.png]]

![[Pasted image 20250715213716.png]]

---
### Recursions
![[Pasted image 20250715215514.png]]
The code breaks because **there’s no stopping condition in the recursive function**, so it keeps calling itself endlessly. This leads to a **stack overflow error** after too many recursive calls (in this case, after ~19,000 calls).
### 🔁 Simple Breakdown:

- Each function call takes up space in memory (call stack).
- Without a `base case` to stop, the stack fills up.
- Eventually, **Java runs out of stack space** → **StackOverflowError**.
![[Pasted image 20250715220544.png]]
#### The loop is now ended cause we just added a base function
if(n == 5)
{
	return;
}
![[Pasted image 20250715221428.png]]

---

![[Recording 20250715221709.m4a]]
Break it down into Smaller Problems
#### Recurrence relation:
![[Pasted image 20250715231745.png]]

---------------------------------------------------

