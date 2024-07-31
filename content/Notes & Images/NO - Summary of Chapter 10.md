##### Nomenclature:
> **NOTE**:
> *In the drawings, the blue edges are the ones in the matching, while the orange ones are not.*

- **Matching**: a subset $M$ of edges such that each node is incident ("touches") at most 1 edge in $M$.
- **Perfect matching**: if the number of edges in $M^*$ is exactly half of all possible edges.
- **Maximum cardinality matching**: maximizes the number of edges in the $M^*$
- **Weighted matching**: maximizes the weights in the $M$
- **Exposed node**: no edge in $M$ is incident ("touches") to this node.
![[Pasted image 20220628151530.png]]
- **Alternating path**: A path composed of alternating edges in the matching and ones that are not.
![[Pasted image 20220628151427.png]]
- **Augmented path**: An alternating path that starts and ends with two different exposed nodes.
![[Pasted image 20220628151231.png]]
- **Matching augmentation**: edge in the matching are exchanged with edges not in the matching, a matching augmentation is only valid if the number of edges in the matching increases aferword (otherwise is useless)
![[Pasted image 20220628151047.png]]
- **Blossom**: cycle with ($2k+1$) edges -> $k$ edges will belong to the matching.
![[Pasted image 20220628150918.png]]
- **Shrinking of a blossom**:
![[Pasted image 20220628150905.png]]
---
##### Mathematical Formulation
- **Variables**:
$b_{ij}$ : boolean, $1$ if $(i,j)$ belongs to $M^*$, $0$ otherwise.
													<br>
- **Objective function**:
$$
\max \sum_{i} \sum_{j} b_{ij}
$$
- **Constraints**:
$$
\sum_{k} b_{kj} + \sum_{k}b_{ik} \le 1
$$
---
##### Edmonds's Algorithm
![[Pasted image 20220628151826.png]]

**Complexity**: $O(n^2 \kern2px m)$ operations.
- $n$ : number of nodes
- $m$ : number of arcs
