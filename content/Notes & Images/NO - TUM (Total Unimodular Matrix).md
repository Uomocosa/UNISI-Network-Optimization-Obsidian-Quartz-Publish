![[Chapter 5_220309_113959_8.jpg]]
![[Chapter 5_220309_113959_9.jpg]]

---
###### More Information: *How can we identify a TU Matrix*
![[NO - Identify a TUM (Totally Unimodular Matrix)]]

---
Another explanation I found on YouTube is reported [[NO - Identify a TUM (Totally Unimodular Matrix) (Bad Example)|here]]

---
![[Chapter 5_220309_113959_11.jpg]]

---
###### More Information: *Why are TUM Matrices important ?*
- Original Source: [Wikipedia]()

From [[NO - P (Polynomial) and NP (Non-deterministic Polynomial) Problems|previous slides]] we have seen that **Pure LP** (Linear Problems) are $\mathcal{P}$ problems (solvable in **polynomial time**), due to the fact that all vertices of the **feasible** solution are **local optima** and one of them is the **optimal solution**, (or the problem is **unbounded** or **unfeasible**), we have also seen one algorithm (the [[NO - Simplex Method and Auxiliary Problem|simplex method]]) to find the optimal solution.

So if a given **IP** have all **integer vertices** we can use the same method, to easily see if that is the case we assert that the $A$ matrix of the canonical formulation is a **TUM** (Totally Unimodular Matrix).

If it is than we can say that the **feasible region** of the problem is an **integer polyhedron** an all vertices of the problem are in fact integers.

A TU Matrix is most often found in graph-related problems, for example take the [[NO - Incidence Matrix|incidence matrix]] of a graph, its elements can only be $\{0 ,\ -1 ,\ +1\}$.