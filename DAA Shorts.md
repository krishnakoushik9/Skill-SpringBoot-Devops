---
# **Exam Prep: Design and Analysis of Algorithms (R-22)**

---

## **📝 Part 1: VSAQ Targets (Short Answers)**

### **Set 1: Definitions**
#### **Unit I**
- [x] **Define Space Complexity and Time Complexity**
  - **Space Complexity:** Maximum memory required by an algorithm as a function of input size.
  - **Time Complexity:** Maximum time taken by an algorithm as a function of input size.

- [x] **Define Little-oh, Omega, and Theta notations**
  - **Little-oh (o):** Strictly upper bound, grows slower than the function.
  - **Omega (Ω):** Lower bound, grows at least as fast as the function.
  - **Theta (Θ):** Tight bound, grows at the same rate as the function.

#### **Unit II**
- [ ] **Define a Priority Queue**
  - Abstract data type that prioritizes elements based on a key (e.g., min/max heap).

- [ ] **Define Disjoint Set Operations (Union/Find)**
  - **Union:** Merges two sets.
  - **Find:** Determines the root of an element’s set.

#### **Unit III**
- [ ] **Define the Principle of Optimality**
  - An optimal solution to a problem contains optimal solutions to its subproblems.

#### **Unit IV**
- [ ] **Difference between Greedy Method and Dynamic Programming**
  - **Greedy:** Makes locally optimal choices at each step.
  - **DP:** Solves subproblems, stores results, and combines them for a global solution.

#### **Unit V**
- [ ] **Define P, NP, NP-Hard, and NP-Complete classes**
  - **P:** Problems solvable in polynomial time.
  - **NP:** Problems verifiable in polynomial time.
  - **NP-Hard:** At least as hard as NP problems (not necessarily in NP).
  - **NP-Complete:** In NP and NP-Hard (e.g., SAT, TSP).

---

### **Set 2: Basic Properties & Logic**
#### **Unit I**
- [ ] **Best, Worst, and Average case complexity of Binary Search**
  - **Best:** O(1) (target is the middle element).
  - **Worst/Average:** O(log n) (halving the search space each step).

#### **Unit II**
- [ ] **Properties of a Max Heap vs Min Heap**
  - **Max Heap:** Parent ≥ children.
  - **Min Heap:** Parent ≤ children.

- [ ] **State the Graph Coloring problem**
  - Assign colors to vertices so no adjacent vertices share the same color, using the minimum number of colors.

#### **Unit III**
- [ ] **Define Reliability Design**
  - Maximizing system reliability by selecting components with optimal reliability-cost trade-offs.

#### **Unit IV**
- [ ] **Define a Minimum Spanning Tree (MST)**
  - A subset of edges connecting all vertices with the minimum total edge weight.

- [ ] **Differentiate BFS vs DFS**
  - **BFS:** Explores all neighbors level-wise (queue-based).
  - **DFS:** Explores as far as possible along a branch (stack-based).

#### **Unit V**
- [ ] **Define Non-deterministic algorithms**
  - Algorithms that can "guess" solutions and verify them in polynomial time (e.g., NP class).

---

## **📝 Part 2: Long Answer Predictions (Questions 11-15)**

### **Unit I: Introduction & Divide and Conquer**
#### **11A: Analysis & Notation**
- [ ] **Derive Big-Oh, Omega, and Theta for polynomial equations**
  - Compare growth rates of polynomial terms to determine asymptotic bounds.

- [ ] **Explain Performance Analysis (Space/Time) with examples**
  - Analyze memory usage (space) and execution steps (time) for algorithms like sorting or searching.

#### **11B: Divide & Conquer Algorithms**
- [ ] **Quick Sort: Algorithm + Best/Worst case derivation**
  - **Algorithm:** Partition array around a pivot, recursively sort subarrays.
  - **Best:** O(n log n), **Worst:** O(n²) (unbalanced partitions).

- [ ] **Merge Sort: Algorithm + Time complexity derivation**
  - **Algorithm:** Divide array into halves, merge sorted halves.
  - **Time Complexity:** O(n log n) for all cases.

- [ ] **Strassen’s Matrix Multiplication: Formulas + Complexity proof**
  - Reduces multiplications from 8 to 7 for 2x2 matrices, complexity: O(n^log₂7).

- [ ] **Binary Search: Iterative vs Recursive algorithm + Analysis**
  - **Iterative:** Uses loops, **Recursive:** Uses function calls; both O(log n).

---

### **Unit II: Disjoint Sets & Backtracking**
#### **12A: Heaps & Disjoint Sets**
- [ ] **Heap Sort: Algorithm trace on an array**
  - Build max heap, repeatedly extract max element and heapify.

- [ ] **Heap Operations: Insertion and Deletion in Max Heap**
  - **Insertion:** Add to end, heapify up.
  - **Deletion:** Remove root, replace with last element, heapify down.

- [ ] **Disjoint Sets: Weighted Union and Collapsing Find algorithms**
  - **Weighted Union:** Attach smaller tree to larger tree.
  - **Collapsing Find:** Flatten structure during find operations.

#### **12B: Backtracking Applications**
- [ ] **N-Queen’s Problem: 4 or 8 Queens solution (State Space Tree)**
  - Place queens row-wise, backtrack if conflicts arise.

- [ ] **Graph Coloring: m-coloring problem with State Space Tree**
  - Assign colors to vertices, backtrack if adjacent vertices conflict.

- [ ] **Hamiltonian Cycles: Algorithm and example trace**
  - Find a cycle visiting each vertex exactly once, backtrack if path fails.

- [ ] **Sum of Subsets: Problem with fixed set and target sum**
  - Find subsets that sum to a target, backtrack if sum exceeds.

---

### **Unit III: Dynamic Programming**
#### **13A: Classic Optimization**
- [ ] **0/1 Knapsack: Solve using DP tabular method**
  - Fill a table to maximize value without exceeding weight capacity.

- [ ] **Traveling Salesperson (TSP): Solve using DP matrix reduction**
  - Use memoization to store shortest paths between subsets of cities.

#### **13B: Shortest Paths & Trees**
- [ ] **All Pairs Shortest Path: Floyd-Warshall Algorithm**
  - Dynamic programming to compute shortest paths between all pairs of vertices.

- [ ] **Optimal Binary Search Tree (OBST): Construction and cost calculation**
  - Minimize search cost by optimizing tree structure based on key frequencies.

- [ ] **Reliability Design: Mathematical formulation and example**
  - Maximize system reliability using dynamic programming for component selection.

---

### **Unit IV: Greedy Method & Traversals**
#### **14A: Greedy Algorithms**
- [ ] **Minimum Spanning Trees: Prim’s Algorithm trace**
  - Start from a vertex, repeatedly add the cheapest edge connecting the tree to a new vertex.

- [ ] **Minimum Spanning Trees: Kruskal’s Algorithm trace**
  - Sort edges by weight, add edges that don’t form cycles.

- [ ] **Shortest Path: Dijkstra’s Single Source Algorithm**
  - Greedily select the shortest path from the source to each vertex.

- [ ] **Job Sequencing: Sequencing with Deadlines**
  - Schedule jobs in decreasing order of profit, respecting deadlines.

- [ ] **Knapsack: Fractional Knapsack Problem**
  - Select items by highest value-to-weight ratio until knapsack is full.

#### **14B: Traversals & Components**
- [ ] **Bi-connected Components: Finding Articulation Points**
  - Use DFS to identify vertices whose removal increases the number of connected components.

- [ ] **Connectivity: Connected components using BFS/DFS**
  - Traverse graph to identify groups of connected vertices.

- [ ] **Tree Traversals: Binary Tree logic (Pre/In/Post)**
  - **Pre-order:** Root → Left → Right.
  - **In-order:** Left → Root → Right.
  - **Post-order:** Left → Right → Root.

---

### **Unit V: Branch & Bound + NP Theory**
#### **15A: Branch and Bound Problems**
- [ ] **TSP (B&B): Solve using LC (Least Cost) Branch and Bound**
  - Branch on edges, bound using minimum cost estimates.

- [ ] **0/1 Knapsack (B&B): Solve using FIFO Branch and Bound**
  - Explore nodes in FIFO order, prune branches with bounds worse than the current solution.

- [ ] **0/1 Knapsack (B&B): Solve using LC Branch and Bound**
  - Prioritize branches with the highest potential value-to-weight ratio.

#### **15B: NP Hard & Complete Theory**
- [ ] **Cook’s Theorem: Statement and Proof logic**
  - SAT is NP-Complete; all NP problems can be reduced to SAT.

- [ ] **Classes: Detailed relationship between P, NP, NP-Hard, NP-Complete**
  - **P ⊆ NP ⊆ NP-Complete ⊆ NP-Hard**; NP-Complete = NP ∩ NP-Hard.

---

### **🛡️ Safety Set: Control Abstractions (General Methods)**
- [ ] **Unit I: General Method (Control Abstraction) of Divide & Conquer**
  - Divide problem into subproblems, solve recursively, combine solutions.

- [ ] **Unit II: General Method of Backtracking (Recursive or Iterative)**
  - Incrementally build solutions, abandon partial solutions if constraints fail.

- [ ] **Unit III: General Method of Dynamic Programming**
  - Store solutions to subproblems to avoid recomputation.

- [ ] **Unit IV: General Method of Greedy Strategy**
  - Make locally optimal choices at each step.

- [ ] **Unit V: General Method of Branch and Bound (FIFO vs LC search logic)**
  - **FIFO:** Explore nodes in queue order.
  - **LC:** Prioritize nodes with the best potential bounds.
