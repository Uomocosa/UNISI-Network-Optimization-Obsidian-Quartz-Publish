Given a graph $G$ its **MSP** (Minimum Spanning Tree, defined as $T^*$) is a connected sub-graph containing **no cycles** and spanning over all the **nodes**, also the MSP has the minimum possible total cost of the arcs (each arc has cost $c_{ij}$)

The arcs of $G$ that make the MSP are called or **tree arcs**, while the one that are excluded from the MSP are called **non-tree arcs**.

---
There are 2 equivalent condition for finding the MSP of a graph:
													<br>
##### Cut Optimality
$$\forall \ (i  ,\ j) \in T^* ,\ c_{ij} \le c_{kl} ,\ k \in S ,\ l \in S'$$
where: $\left[ S ,\ S' \right]$ is the [[NO - Cutting a Graph and s-t Cut|cut]] obtained by removing the arc $(i, j)$ from $T^*$.
													<br>
##### Path Optimality
$$
\forall \ (k,l) \notin T^* ,\ c_{ij} \le c_{kl} ,\ (i, j) \in P
$$
where: $P$ is the [[NO - Graph Components Cheat-Sheet|path]] on $T^*$ from $i$ to $j$.

---
###### Formulation of MSP Problem
- **Variables**:
$b_{ij}$ : boolean, $1$ if $(i,j)$ belongs to $T^*$, $0$ otherwise.
													<br>
- **Constants**:
$c_{ij}$ : cost of arc $(i,j)$
$n$ : number of nodes
													<br>
- **Objective Functions**:
$$\min \overline{b} \cdot \overline{c}$$
(minimize the cost of the arcs in $T^*$)
													<br>
- **Constraints**:
$$
\sum_i \sum_j b_{ij} == n - 1
$$
**span over all nodes** -> the number of arcs is fixed.
$$
\sum_{b \ \in \ \text{arcs}} b_{ij} <= \text{number of nodes in arcs} - 1 \kern 30px \forall \ \text{arcs} \in S
$$
Where: 
- $\text{arcs}$ is a set of arcs of the graph.
- S is a set containing all possible combination of arcs in the graph. 
**no-cycles** -> Given all possible combination of arcs we have that each combination has to have a number of "active" arcs ($b_{ij} = 1$) less or equal than the number of nodes less $1$ present in the combination. (otherwise it would be a cycle)

---
##### Kruskal Algorithm:
![[Pasted image 20220628115234.png]]

**Complexity**: $O(m \kern3px log(m)) + O(m + n \kern3px log(n))$ operations

----
##### Prim Algorithm
*In practice the Prim Algorithm is the better one*
![[Pasted image 20220628115443.png]]

**Complexity**: $O(m + n \kern3px log(n))$ operations

---
