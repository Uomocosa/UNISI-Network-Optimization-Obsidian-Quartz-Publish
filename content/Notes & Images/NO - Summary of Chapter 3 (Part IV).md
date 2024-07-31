After we define  $\left[ \overline{c}_B, \overline{c}_N \right]$ in the same way we defined $\overline{x} = \left[ \overline{x}_B ,\ \overline{x}_N \right]$, we can write the **LP**:
$$
\begin{align}
& \min \overline{c} \kern3px ^t \cdot \overline{x}
\\
& \overline{\overline{A}} \cdot \overline{x} = \overline{b}
\\
& \overline{x} \geq 0
\end{align}
$$
as:
$$
\begin{align}
& \min \overline{c}_B \kern3px ^t \cdot  \overline{x}_B + \overline{c}_N \kern3px ^t \cdot \overline{x}_N
\\
& \overline{\overline{B}} \cdot \overline{x}_B + \overline{\overline{N}} \cdot \overline{x}_N = \overline{b}
\\
& \overline{x}_B \geq 0
\\
& \overline{x}_N \geq 0
\end{align}
$$
From the equation we obtain that:
$$
\overline{x}_B = \overline{\overline{B}}^{-1} \cdot \left( \overline{b} - \overline{\overline{N}} \cdot \overline{x}_N \right)
$$

So the **LP** becomes:
$$
\begin{align}
& \min \overline{c}_B \kern3px ^t \cdot \overline{\overline{B}}^{-1} \cdot \left( \overline{b} - \overline{\overline{N}} \cdot \overline{x}_N \right) + \overline{c}_N \cdot \overline{x}_N
\\
& \overline{x}_B \geq 0
\\
& \overline{x}_N \geq 0
\end{align}
$$
