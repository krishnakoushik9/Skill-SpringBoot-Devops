[[Kunal Kushwaha]]

- Big O notation describes the upper bound of an algorithm's time or space complexity. It shows the worst-case scenario of how performance grows with input size.
- Big Omega notation is the opposite. It shows the lower bound, meaning the best-case scenario.
- Little o notation shows an upper bound that is not tight, so the algorithm grows slower than the given function.
- Little omega notation is the opposite of little o. It shows a lower bound that isn’t tight, so the algorithm grows faster than the given function.
- [x] <img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="540"/>
# Deep Dive into the Mathematics of Asymptotic Notations

As a Computer Science student passionate about AI and ML, understanding the mathematical foundations of asymptotic notations like Big O, Big Omega, little o, and little omega is crucial for analyzing algorithm efficiency, especially in optimizing LLMs or game development in Unreal Engine. Below, I'll break down each notation mathematically, including formal definitions, examples, and key properties. We'll use LaTeX for precise mathematical expressions.

## Big O Notation (O)

Big O notation describes an upper bound on the growth rate of a function, typically used for worst-case complexity analysis.

### Formal Definition

A function $f(n)$ is said to be $O(g(n))$ if there exist positive constants $c$ and $n_0$ such that for all $n \geq n_0$,

$$
0 \leq f(n) \leq c \cdot g(n).
$$

This means $f(n)$ grows no faster than $g(n)$ asymptotically.

### Example

For $f(n) = 3n^2 + 2n + 1$, we can say $f(n) = O(n^2)$ because choosing $c = 6$ and $n_0 = 1$ satisfies the inequality for large $n$.

### Key Properties

- **Transitivity**: If $f(n) = O(g(n))$ and $g(n) = O(h(n))$, then $f(n) = O(h(n))$.
- **Addition**: If $f_1(n) = O(g(n))$ and $f_2(n) = O(g(n))$, then $f_1(n) + f_2(n) = O(g(n))$.
- Commonly used in algorithm analysis to bound time or space complexity from above.


## Big Omega Notation (Ω)

Big Omega provides a lower bound, often for best-case scenarios or to indicate that a function grows at least as fast as another.

### Formal Definition

$f(n)$ is $\Omega(g(n))$ if there exist positive constants $c$ and $n_0$ such that for all $n \geq n_0$,

$$
0 \leq c \cdot g(n) \leq f(n).
$$

This captures the idea that $f(n)$ is at least on the order of $g(n)$.

### Example

For $f(n) = 3n^2 + 2n + 1$, $f(n) = \Omega(n^2)$ with $c = 1$ and $n_0 = 1$, as $n^2 \leq f(n)$ for large $n$.

### Key Properties

- **Transitivity**: Similar to Big O, if $f(n) = \Omega(g(n))$ and $g(n) = \Omega(h(n))$, then $f(n) = \Omega(h(n))$.
- **Relation to Big O**: If $f(n) = \Omega(g(n))$, then $g(n) = O(f(n))$.
- Useful in proving that an algorithm cannot perform better than a certain bound, like in sorting algorithms where $\Omega(n \log n)$ is a lower bound for comparison-based sorts.


## Little o Notation (o)

Little o is a stricter upper bound than Big O, indicating that $f(n)$ grows strictly slower than $g(n)$.

### Formal Definition

$f(n) = o(g(n))$ if

$$
\lim_{n \to \infty} \frac{f(n)}{g(n)} = 0.
$$

Unlike Big O, there's no constant $c$ that works for all sufficiently large $n$; the ratio approaches zero.

### Example

$f(n) = n$ is $o(n^2)$ because $\lim_{n \to \infty} \frac{n}{n^2} = 0$.

### Key Properties

- Implies $f(n) = O(g(n))$, but not vice versa (e.g., $n^2 = O(n^2)$, but not $o(n^2)$).
- Used when we need to emphasize that one function is negligible compared to another asymptotically.
## Little Omega Notation (ω)

Little omega is the strict lower bound counterpart to little o, showing that $f(n)$ grows strictly faster than $g(n)$.
### Formal Definition

$f(n) = \omega(g(n))$ if

$$
\lim_{n \to \infty} \frac{f(n)}{g(n)} = \infty.
$$

The ratio diverges to infinity.
### Example

$f(n) = n^2$ is $\omega(n)$ because $\lim_{n \to \infty} \frac{n^2}{n} = \infty$.

### Key Properties

- Implies $f(n) = \Omega(g(n))$, but stricter.
- **Relation to little o**: $f(n) = \omega(g(n))$ if and only if $g(n) = o(f(n))$.
- Helpful in scenarios like analyzing superlinear growth in ML model training complexities.


## Theta Notation (Θ) - Tight Bound

While not explicitly mentioned, Theta combines Big O and Big Omega for a tight bound.

### Formal Definition

$f(n) = \Theta(g(n))$ if $f(n) = O(g(n))$ and $f(n) = \Omega(g(n))$, or equivalently, there exist constants $c_1, c_2 > 0$ and $n_0$ such that

$$
c_1 \cdot g(n) \leq f(n) \leq c_2 \cdot g(n)
$$

for all $n \geq n_0$.
### Example

$f(n) = 3n^2 + 2n + 1 = \Theta(n^2)$.

This notation is particularly relevant in your AI/ML work for precise complexity analysis in optimization algorithms. If you'd like examples tailored to Unreal Engine or LLMs, let me know!
