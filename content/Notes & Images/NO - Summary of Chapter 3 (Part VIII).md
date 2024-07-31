The **simplex method** is an easy algorithm that let us find the **optimal solution** to any **LP**.
![[Pasted image 20220627155544.png]]

To find a starting vertex we can use the **AP** ([[NO - Simplex Method and Auxiliary Problem|Auxiliary Problem]]):
We take the matrix $A$ and variables $x$ from the original problem and we add $x_a$ new variables (same dimension as $x$).
The **AP** is defined as follows:
$$
\begin{array}{l}
& \min \sum x_a
\\
& A \kern2px x + I \kern1px x_a = b
\\
& x \ge 0
\\
& x_a \ge 0
\end{array}
$$
Then we have that:
- If the optimal solution of the AP is $= 0$: then we have that $x$ is a **vertex** of the original problem.
- If the optimal solution of the AP is $> 0$: then the original problem is **unfeasible**.
