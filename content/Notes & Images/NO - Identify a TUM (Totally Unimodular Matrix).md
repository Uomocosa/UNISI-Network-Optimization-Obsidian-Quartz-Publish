- Original Source: [Wikipedia](https://en.wikipedia.org/wiki/Unimodular_matrix#:~:text=be%20totally%20unimodular%3A-,Every%20entry%20in,.,-It%20was%20realized)

---
A Matrix $M$ is **TU** (Totally Unimodular) if:
1. Every entry in $M$ is $0$, $+1$, or $−1$.
2. Every column of $M$ contains **at most** two non-zero (i.e., $+1$ or $−1$) entries
3. Assert that it is possible to divide the **rows** of $M$ in 2 groups ($\mathcal{B}$ and $\mathcal{C}$) respecting the following rules:
-> If two non-zero entries in a **column** of $M$ have the **same sign**, then the row of one is in the $\mathcal{B}$ group and the other one in the $\mathcal{C}$ group
-> If two non-zero entries in a **column** of $M$ have **opposite signs**, then the rows of both are in the $\mathcal{B}$ group, or are both in the $\mathcal{C}$ group.

> **NOTE**:
> If one of the 2 groups ($\mathcal{B}$ or $\mathcal{C}$) is empty then the related **IP** ([[NO - IP (Integer Programs)|Integer Problem]]) is **unbounded**

---
###### ~ Ex.: $2 \times 2$ Matrix
$$
\left[
\begin{array}{cc}
1 & -1
\\
1 & 1
\end{array}
\right]
$$
✓ All elements are either $-1$, $0$, $+1$
✓ In each column we have at most 2 non-zero elements
✗ According to the first column the 2 rows must be in the same group, but according to the second column the 2 rows must also be in different groups
-> This matrix is not TU

---
###### ~ Ex.: $4 \times 4$ Matrix
$$
\left[
\begin{array}{cc}
1 & -1 & -1 & 0
\\
-1 & 0 & 0 & -1
\\
0 & 1 & 0 & -1
\\
0 & 0 & 1 & 0
\end{array}
\right]
$$
✓ All elements are either $-1$, $0$, $+1$
✓ In each column we have at most 2 non-zero elements
✓ $\text{row}_1 \in \mathcal{B}$, $\text{row}_2 \in \mathcal{B}$
✓ $\text{row}_1 \in \mathcal{B}$, $\text{row}_3 \in \mathcal{B}$
✓ $\text{row}_1 \in \mathcal{B}$, $\text{row}_4 \in \mathcal{B}$
✓ $\text{row}_2 \in \mathcal{B}$, $\text{row}_3 \in \mathcal{C}$
$$
\begin{array}{cc}
\begin{array}{c}
\mathcal{B}
\\
\mathcal{B}
\\
\mathcal{C}
\\
\mathcal{B}
\end{array}
&
\left[
\begin{array}{cc}
1 & -1 & -1 & 0
\\
-1 & 0 & 0 & -1
\\
0 & 1 & 0 & -1
\\
0 & 0 & 1 & 0
\end{array}
\right]
\end{array}
$$
-> This matrix is TU
