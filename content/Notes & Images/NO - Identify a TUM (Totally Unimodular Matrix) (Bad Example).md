###### *How can we identify a TU Matrix*
- Original Source [Youtube](https://youtu.be/WD1nrAw8lyU?t=113)

![[Pasted image 20220623165829.png]]
![[Pasted image 20220623171546.png]]
In summary, we have that for each row we have that taken two partition $M_1$ and $M_2$ (which contains some of the elements in that row, taken arbitrarily) and we have that:
- $M_1$ and $M_2$ are **not empty**
- $sum(M_1) - sum(M_2) = 0$

###### ~ Ex.:
![[Pasted image 20220623170606.png]]
This is TUM, because:
✓ All elements are either $-1$, $0$, $+1$
✓ In each column we have at most 2 non-zero elements
✓ $M_{11}$ = {-1} , $M_{11}$ = {-1} ->  $sum(M_1) - sum(M_2) = 0$
✓ $M_{11}$ = {0, -1} , $M_{11}$ = {0, -1} ->  $sum(M_1) - sum(M_2) = 0$
✓ $M_{11}$ = {0} , $M_{11}$ = {0} ->  $sum(M_1) - sum(M_2) = 0$
✓ $M_{11}$ = {0} , $M_{11}$ = {0} ->  $sum(M_1) - sum(M_2) = 0$

###### ~ Ex.:
![[Pasted image 20220623171150.png]]
This is **not** TUM, because:
✓ All elements are either $-1$, $0$, $+1$
✓ In each column we have at most 2 non-zero elements
✗ $M_{11}$ = {1} , $M_{11}$ = {-1} ->  $sum(M_1) - sum(M_2) = 2$
✓ $M_{11}$ = {1} , $M_{11}$ = {1} ->  $sum(M_1) - sum(M_2) = 0$

> **NOTE**:
> This goes in conflict with the *Sufficient Condition 2* of the video, so probably the $M_1$, $M_2$ condition not as i said.
