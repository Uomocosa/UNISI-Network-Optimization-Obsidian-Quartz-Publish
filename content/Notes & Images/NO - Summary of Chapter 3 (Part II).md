Given the base $\overline{\overline{B}}$, we can set **non-basic variables** $\overline{x}_N = 0$ and compute 
$$
\overline{x}_B = \overline{\overline{B}}^{-1} \cdot \overline{b}
$$
If $\overline{x}_B < 0$ the **basis** is **unfeasible**.
Else if $\overline{x}_B \ge 0$ the **basis** is **feasible**.
-> So we have that a **BFS** (Basic Feasible Solution) is obtained setting $\overline{x}_B = \overline{\overline{B}}^{-1} \cdot \overline{b}$

> **NOTE**:
> It can be proven that each **vertex** corresponds to a **BFS**
