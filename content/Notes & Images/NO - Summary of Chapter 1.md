A general **MP** ([[NO - Mathematical Program|Mathematical Program]]) consists of **variables**, **constraints**, and an **objective function**, where:
- **Constants and variables** are the information we work with and what we can *change*.
- **Constraints** are the *rules* we set to the problem.
- **Objective function** is what we want to achive.

---
A **solution** can be either **feasible** or **unfeasible**, **local** or **optimal**/**global**
- A solution that respects the **constraints** is defined as **feasible**, else it is defined as **unfeasible**.
- A **feasible** solution can be defined as a **local optima**, if in its [[NO - Neighbourhood of a Solution|neighbourhood]] we cannot find a better solution, while if the solution is the best possible solution, we define it as the **optimal solution** or as the **global optima**.

---
An **MP** can be either [[NO - Relaxation & Restriction of an MP|relaxed or restricted]]:
- A **relaxation** consists in **removing** some **constraints**, or more generally changing them such that the number of solutions to the initial problem $P$ *increases*:
![[Pasted image 20220627115417.png]]
where: $P$ is the **original** problem, $P'$ is the new **relaxed** problem
- Viceversa a **restriction** reduces the number of possible solution of the original problem $P$:
![[Pasted image 20220627120331.png]]

> **NOTE**:
> - A **relaxed** problem can find a better solution, but it might be **unfeasible**
> - A **restricted** problem always find a **feasible** solution, but might not be the **optimal** one.
> 
> We usually **relax** or **restrict** a problem to facilitate the computation

---
An **MP** can be defined as [[NO - Convex Program|convex]] if the **local solution** of the problem is also the **global one**, so it has only 1 **local solution**
###### ~ Ex.: 2D Convex Function:
![[Pasted image 20220627120054.png]]
