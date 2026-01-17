i)Statement of Proposition : It is a declarative sentence with true or false
We typically denote propositions using lowercase letters: p,q,r,s,…
- **Examples** : 
- Sun rises in the east (True Statement)
- 5+2 = 7 (True Statement)
- **Non-Examples (Not Propositions) :**
- "What time is it?" (Interrogative/Question)
- "Close the door!" (Imperative/Command)
ii)Types of Propositions :
- Atomic / Simple / Primary / Primitive type of Proposition
- Compound Propositions
- **Atomic Proposition Example :** 
- The Proposition where it can no longer be divided any further and it doesn't contain any connectives.
- **Compound :**
- It is a Proposition which is a combination and addition of several Connectives.
----
##### Logical Connectives
i) **Negation (NOT)**
- **Symbol:** ¬p or ∼p or pˉ​
- **Definition:** The negation of p is the statement "It is not the case that p."
- **Rule:** It simply flips the truth value.
ii) **Conjunction (AND)**
- **Symbol:** p∧q
- **Definition:** The conjunction of p and q is "p and q".
- **Rule:** p∧q is True **only if both** p and q are True. Otherwise, it is False.
iii) **Disjunctive (Inclusive OR)**
- **Symbol:** p∨q
- **Definition:** The disjunction of p and q is "p or q".
- **Rule:** p∨q is True if **at least one** of the propositions is True. It is False only if _both_ are False.
- _Note:_ In logic, "OR" is inclusive. It means "p or q or both."
iv) **Exclusive OR (XOR)**
- **Symbol:** p⊕q
- **Definition:** "Either p or q, but not both."
- **Rule:** True only when p and q have **different** truth values.

 ----
 ### ***Truth Tables & Precedence***
 
 **Order of Precedence (Standard)**
1. **Parentheses** () — _Always solve innermost first._
2. **Negation** ¬
3. **Conjunction** ∧
4. **Disjunction** ∨
5. **Implication** →
6. **Biconditional** ↔
----
# PYQ's
# GATE Level Discrete Math Practice (Propositional Logic)

**Q1.** Let $P$, $Q$, and $R$ be propositions. Which of the following compound propositions is a **Tautology**?
- [ ] $((P \rightarrow Q) \land (Q \rightarrow R)) \rightarrow (P \rightarrow R)$
- [ ] $(P \rightarrow Q) \leftrightarrow (\neg Q \rightarrow \neg P)$
- [ ] $((P \lor Q) \land \neg P) \rightarrow Q$
- [x] All of the above

**Q2.** Which of the following is logically equivalent to the statement: *"If it rains, then I will not go to the park"*?
- [ ] It rains and I go to the park.
- [x] It does not rain or I do not go to the park.
- [ ] It does not rain and I go to the park.
- [ ] If I do not go to the park, then it rains.

**Q3.** Consider the statement form: $(P \rightarrow Q) \rightarrow (Q \rightarrow P)$. This statement is:
- [ ] A Tautology
- [ ] A Contradiction
- [ ] Logically equivalent to $P \leftrightarrow Q$
- [x] A Contingency (neither tautology nor contradiction)

**Q4.** Let $p, q, r, s$ be four propositions. To prove that $(p \land q \land r) \rightarrow s$ is a tautology, how many rows in the truth table must generally be checked?
- [ ] 4
- [ ] 8
- [x] 16
- [ ] 32

**Q5.** Which of the following propositions is a **Contradiction**?
- [ ] $P \lor \neg P$
- [ ] $P \land \neg P$
- [ ] $(P \rightarrow Q) \land (P \land \neg Q)$
- [x] Both (b) and (c)

**Q6.** The statement $(\neg P \leftrightarrow Q)$ is logically equivalent to:
- [ ] $P \leftrightarrow \neg Q$
- [ ] $\neg (P \leftrightarrow Q)$
- [ ] $(P \land Q) \lor (\neg P \land \neg Q)$
- [ ] Both (a) and (b)

**Q7.** Which one of the following is **NOT** logically equivalent to $(p \leftrightarrow q)$?
- [ ] $(p \land q) \lor (\neg p \land \neg q)$
- [ ] $(p \rightarrow q) \land (q \rightarrow p)$
- [ ] $(\neg p \lor q) \land (\neg q \lor p)$
- [ ] $(\neg p \land q) \lor (p \land \neg q)$

**Q8.** Identify the valid argument (Rule of Inference) from the following:
- [ ] $P \rightarrow Q, Q \vdash P$
- [ ] $P \rightarrow Q, \neg P \vdash \neg Q$
- [ ] $P \rightarrow Q, \neg Q \vdash \neg P$
- [ ] $P \lor Q, P \vdash \neg Q$

**Q9.** Let $S$ be the statement: $((P \rightarrow Q) \land P) \rightarrow Q$. Let $T$ be the statement: $((P \rightarrow Q) \land \neg Q) \rightarrow \neg P$.
- [ ] $S$ is a tautology, $T$ is a contradiction.
- [ ] $S$ is a contradiction, $T$ is a tautology.
- [ ] Both $S$ and $T$ are tautologies.
- [ ] Both $S$ and $T$ are contingencies.

**Q10.** The proposition $P \land (P \rightarrow Q)$ is logically equivalent to:
- [ ] $P \lor Q$
- [ ] $P \land Q$
- [ ] $P \rightarrow Q$
- [ ] $\neg P \lor Q$

**Q11.** What is the negation of the statement: *"If $x$ is prime, then $x$ is odd or $x$ is 2"*?
- [ ] $x$ is prime and $x$ is not odd and $x$ is not 2.
- [ ] If $x$ is not prime, then $x$ is odd or $x$ is 2.
- [ ] $x$ is prime or $x$ is not odd or $x$ is not 2.
- [ ] $x$ is not prime and ($x$ is odd or $x$ is 2).

**Q12.** A set of connectives is called "Functionally Complete" if any boolean function can be expressed using only connectives from that set. Which set is **NOT** functionally complete?
- [ ] $\{ \neg, \land \}$
- [ ] $\{ \downarrow \}$ (NOR operator)
- [ ] $\{ \rightarrow, \neg \}$
- [ ] $\{ \rightarrow, \lor \}$

**Q13.** The proposition $(P \rightarrow Q) \land (Q \rightarrow R) \land (R \rightarrow S)$ implies which of the following?
- [ ] $P \rightarrow S$
- [ ] $P \land S$
- [ ] $\neg P \rightarrow S$
- [ ] $S \rightarrow P$

**Q14.** If the proposition $\neg(p \rightarrow q)$ is True, then the truth values of $p$ and $q$ are respectively:
- [ ] True, True
- [ ] True, False
- [ ] False, True
- [ ] False, False

**Q15.** The dual of a proposition is obtained by swapping $\lor$ with $\land$, and $T$ with $F$. What is the dual of $(P \lor T) \land (Q \lor F)$?
- [ ] $(P \land F) \lor (Q \land T)$
- [ ] $(P \land T) \lor (Q \land F)$
- [ ] $(P \lor F) \land (Q \lor T)$
- [ ] $\neg P \land \neg Q$

**Q16.** "You cannot ride the roller coaster if you are under 4 feet tall unless you are older than 16 years old." Let $Q$, $R$, $S$ represent "You can ride", "You are under 4 feet", and "You are older than 16" respectively. Translating to logic:
- [ ] $(R \land \neg S) \rightarrow \neg Q$
- [ ] $(S \land \neg R) \rightarrow Q$
- [ ] $R \rightarrow (\neg S \rightarrow \neg Q)$
- [ ] Both (a) and (c)

**Q17.** How many distinct truth tables can be constructed for expressions involving $n$ propositional variables?
- [ ] $2^n$
- [ ] $2^{2^n}$
- [ ] $n^2$
- [ ] $2n$

**Q18.** Which of the following is equivalent to $\neg (P \leftrightarrow Q)$ (Exclusive OR)?
- [ ] $(P \land \neg Q) \lor (\neg P \land Q)$
- [ ] $(P \lor Q) \land \neg(P \land Q)$
- [ ] $P \oplus Q$
- [ ] All of the above

**Q19.** Consider the statement: *"If I am tired or hungry, I cannot study."* Which of the following is logically equivalent to the contrapositive of this statement?
- [ ] If I can study, then I am neither tired nor hungry.
- [ ] If I can study, then I am not tired or not hungry.
- [ ] If I cannot study, then I am tired or hungry.
- [ ] If I am neither tired nor hungry, then I can study.

**Q20.** The compound statement $(P \rightarrow (Q \rightarrow R)) \rightarrow ((P \rightarrow Q) \rightarrow (P \rightarrow R))$ is a:
- [ ] Tautology
- [ ] Contradiction
- [ ] Contingency
- [ ] None of the above

---
### **Answer Key**
1. [d]
2. [b]
3. [d]
4. [c]
5. [d]
6. [d]
7. [d]
8. [c]
9. [c]
10. [b]
11. [a]
12. [d]
13. [a]
14. [b]
15. [a]
16. [d]
17. [b]
18. [d]
19. [a]
20. [a]



