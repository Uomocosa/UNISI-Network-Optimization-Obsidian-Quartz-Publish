Knowing that the **objective function** of the **basis/non-basis** formulation of an **LP** is: 
$$
\min c_{\tiny B}^t 
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
$$
we can define a **reduced cost**:
$$
c_{\tiny N}^t - c_{\tiny B}^t \kern2px B^{-1} \kern2px N 
$$
Which is the part of the objective function that changes when increasing $x_{\tiny N}$.
Then we can say that if the reduced cost is $< 0$ than there exist a **descent direction** of $x_{\tiny N}$ such that we can find a better solution.
Because, multiplying the reduced cost, which we have said is $< 0$ , with $x_{\tiny N}$, which is $\ge 0$ (because of the constraint), then the objective function will decrease, so we have found a better solution.