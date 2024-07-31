Given the **constraints** of a **LP**: 
$$
\begin{align}
& \overline{\overline{A}} \cdot \overline{x} = \overline{b}
\\
& \overline{x} \geq 0
\end{align}
$$
we can divide the matrix $\overline{\overline{A}}$ and the vector $\overline{b}$ in [[NO - Basis and Basic Variables|bases and non-bases]], where: 
> A **base** $B$ is a set of linearly independent $m$ columns of $\overline{\overline{A}}$

So we can always write 
$$
\overline{\overline{A}} = \left[ \overline{\overline{B}} ,\ \overline{\overline{N}} \right]
$$
where: $\overline{\overline{B}}$ is the **base** of $\overline{\overline{A}}$ and $\overline{\overline{N}}$ is the **non-base**


So we have separate $x$ in the same way:
$$
\overline{x} = \left[ \overline{x}_B ,\ \overline{x}_N \right]
$$
where: $\overline{x}_B$ (**basic variables**) is the part of $\overline{x}$ that multiplies $\overline{\overline{B}}$, and $\overline{x}_N$ (**non-basic variables**) is the part that multiplies $\overline{\overline{N}}$.

