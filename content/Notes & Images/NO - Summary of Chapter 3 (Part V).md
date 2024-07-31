Given the **basis/non-basis** formulation of an **LP**: (dropping *overline*s *cdot*s)
$$
\begin{align}
& \min c_{\tiny B}^t 
\kern2px
B^{-1} 
\left( 
	b - N 
	\kern1px
	x_{\tiny N} 
\right) + 
c_{\tiny N}
\kern2px 
x_{\tiny N}
\\
& x_{\tiny N} \geq 0
\\
& x_{\tiny N} \geq 0
\end{align}
$$
We can say that, if $x$ is a vertex, then:
$$
\begin{align}
& x_{\tiny B} = B^{-1} \kern2px b
\\
& x_{\tiny N} = 0
\end{align}
$$
Also one of the constraints enforces that:
$$
x_{\tiny N} \ge 0
$$
If we increase $x_{\tiny N}$ we have a change in the whole $A$ matrix, such that $B$ and $N$ exchange variables, so with these changes we can re-calculate $x_{\tiny B} = B^{-1} \kern2px b - B^{-1} N x_{\tiny N}$

> **NOTE**: 
> $x_{\tiny B}$ can increase or decrease but we need to have $x_{\tiny B} \ge 0$ (constraint)

And find a new vertex of the problem, which might be a better solution.