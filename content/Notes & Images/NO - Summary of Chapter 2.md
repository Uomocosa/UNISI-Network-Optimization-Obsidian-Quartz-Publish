An **LP** ([[NO - Linear Program|Linear Program]]) is a special case of **MP**, where:
- **variables** are all *real numbers* ($x \in \mathbb{R}$)
- **constraints** and **objective function** are all *linear* ($a^t x \geq b$, $\min c^t x$)

---
An **LP**, can always be brought in its **standard form**:
$$
\begin{align}
& \min \overline{c} \kern3px ^t \cdot \overline{x}
\\
& \overline{\overline{A}} \cdot \overline{x} = \overline{b}
\\
& \overline{x} \geq 0
\end{align}
$$
Because:
$$
\max f(z) = - \min f(-z)
$$
Inequalities can be written as equalities using **slack variables** (for less-or-equal inequalities):
$$
\begin{array}{lll}
& ax \leq b & \rightarrow &
	\begin{array}{l}
	ax = (b - s)
	\\
	s \geq 0
	\end{array}
\end{array}
$$

or **surplus variables** (for greater-or-equal inequalities):
$$
\begin{array}{lll}
& ax \geq b & \rightarrow &
	\begin{array}{l}
	ax = (b + t)
	\\
	t \geq 0
	\end{array}
\end{array}
$$


---
We can describe an **LP** geometrically:
![[Pasted image 20220627141743.png]]
![[Pasted image 20220627141753.png]]
![[Pasted image 20220627141804.png]]
![[Pasted image 20220627141819.png]]

---
A problem is defined as:
- **feasible** and **bounded**, if a solution exist and is finite
- **feasible** and **unbounded**, if a solution exist and is infinite
- **unfeasible** if a solution does not exist

---
Given a **polyhedron** we have a [[NO - Extreme Points and Vertices|vertex]] is defined as one of its extreme points:
![[Pasted image 20220627142214.png]]

==If the **LP** admits an **optimal solution**, then it exist at least one **optimal vertex**.==
