![[Pasted image 20251008100800.png]]
[[Training]]
![[Pasted image 20251008101101.png]]
```java
public static int singleNumber(int[] n) {
    int o = 0, t = 0;
    for (int x : n) {
        o = (o ^ x) & ~t;
        t = (t ^ x) & ~o;
    }
    return o;
}
```

This code finds the number in the array `n` that appears only once when all others appear exactly twice.

***

### Key Variables:

- `o`: Tracks bits which have appeared once so far
- `t`: Tracks bits which have appeared twice so far

***

### Explanation with Debugging Steps:

Let's take an example input array:

```java
int[] n = {2, 2, 3, 2};
```

This example is from a common "single number" variant where every number except one appears thrice, but here the function logic is for twice, let's carefully observe the flow for this.

***

### Step 1: Initial values

`o = 0 (binary 0000)`
`t = 0 (binary 0000)`

***

### Step 2: For each element in the array, update `o` and `t`

**Iteration for x = 2 (binary 0010):**

- Calculate `o`:
$$
o = (o \oplus x) \& \sim t = (0000 \oplus 0010) \& \sim 0000 = 0010 \& 1111 = 0010
$$
- Calculate `t`:

$$
 t = (t \oplus x) \& \sim o = (0000 \oplus 0010) \& \sim 0010 = 0010 \& 1101 = 0000 
$$

Output:

- `o = 0010 (decimal 2)`
- `t = 0000 (decimal 0)`

***

**Iteration for x = 2 (second element):**

- Calculate `o`:
$$
o = (0010 \oplus 0010) \& \sim 0000 = 0000 \& 1111 = 0000 
$$
- Calculate `t`:
$$
t = (0000 \oplus 0010) \& \sim 0000 = 0010 \& 1111 = 0010 
$$

Output:
- `o = 0000 (0)`
- `t = 0010 (2)`

***

**Iteration for x = 3 (binary 0011):**

- Calculate `o`:
$$
o = (0000 \oplus 0011) \& \sim 0010 = 0011 \& 1101 = 0001 
$$
- Calculate `t`:
$$
t = (0010 \oplus 0011) \& \sim 0001 = 0001 \& 1110 = 0000
$$

Output:
- `o = 0001 (1)`
- `t = 0000 (0)`
***

**Iteration for x = 2 (third element):**

- Calculate `o`:
$$
o = (0001 \oplus 0010) \& \sim 0000 = 0011 \& 1111 = 0011
$$
- Calculate `t`:
$$
t = (0000 \oplus 0010) \& \sim 0011 = 0010 \& 1100 = 0000
$$
Output:

- `o = 0011 (3)`
- `t = 0000 (0)`
***
### Final Step: Return `o` which is `3`
This matches the element that appears once.
***
### Summary:

- Bitwise `XOR` toggles bits based on presence.
- `o` tracks bits present once.
- `t` tracks bits present twice.
- The bitwise `AND` with negation ensures bits are only counted once or twice accurately.
- After processing the array, `o` holds the one-time appearing number.

This approach is an efficient, bitwise solution to find the single number in O(n) time and O(1) space.
