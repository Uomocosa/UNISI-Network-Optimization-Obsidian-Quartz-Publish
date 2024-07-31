![[Chapter 18_220308_111415_8.jpg]]
![[Chapter 18_220308_111415_9.jpg]]

> **NOTE**:
> It makes sense that being a penalizing cost $\lambda (C \kern2px x - d)$, with $\lambda \ge 0$, to find the best **UB** for our original problem we have to search for the $\max L(\lambda)$, (if the original problem is a minimization problem, else the $\min L(\lambda)$).
> [Wikipedia](https://en.wikipedia.org/wiki/Lagrangian_relaxation#:~:text=The%20above%20inequality%20tells%20us%20that%20if%20we%20minimize%20the%20maximum%20value%20we%20obtain%20from%20the%20relaxed%20problem%2C%20we%20obtain%20a%20tighter%20limit%20on%20the%20objective%20value%20of%20our%20original%20problem.)

> **NOTE**:
> To understand why the $\max L(\lambda)$ problem yields the best bound think of $\lambda$ not as a set weights previously decided but as another variable other then $x$.

The optimal result to the Lagrangian relaxation problem will be no smaller than the optimal result to the original problem.
[Wikipedia](https://en.wikipedia.org/wiki/Lagrangian_relaxation#:~:text=the%20optimal%20result%20to%20the%20Lagrangian%20relaxation%20problem%20will%20be%20no%20smaller%20than%20the%20optimal%20result%20to%20the%20original%20problem)

We can also solve the $\max L(\lambda)$ problem, with the **sub-gradient optimization method**, which result in an UB really tight which can be used as an approximate solution to the original problem.

A Lagrangian relaxation algorithm thus proceeds to explore the range of feasible $\lambda$ values while seeking to minimize the result returned by the inner problem. 
Each value returned by the inner problem is a candidate upper bound to the problem, the smallest of which is kept as the best upper bound. 
If we additionally employ a heuristic, probably seeded by the $x$ values returned by the inner problem, to find feasible solutions to the original problem, then we can iterate until the best upper bound and the cost of the best feasible solution converge to a desired tolerance (**sub-gradient optimization method**).
[Wikipedia](https://en.wikipedia.org/wiki/Lagrangian_relaxation#:~:text=A%20Lagrangian%20relaxation,a%20desired%20tolerance.)

![[Chapter 18_220308_111415_10.jpg]]
![[Chapter 18_220308_111415_11.jpg]]
![[Chapter 18_220308_111415_12.jpg]]
![[Chapter 18_220308_111415_13.jpg]]
![[Chapter 18_220308_111415_14.jpg]]
