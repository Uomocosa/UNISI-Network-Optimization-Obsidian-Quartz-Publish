##### DFJ Mathematical Formulation for TSP
- **Variables**:
$b_{ij}$ : boolean, $1$ if edge $(i,j)$ belongs to $TSP^*$, $0$ otherwise.
							<br>
- **Constants**:
$c_{ij}$ : weight of arc $(i, j)$
$n$ : number of nodes
							<br>
- **Objective function**:
$$
\min \overline{b} \cdot \overline{c}
$$
							<br>
- **Constraints**:
$$
\sum_k b_{kj} + \sum_k b_{ik} = 2 \kern30px \forall \ k = 1 ,\ 2 ,\ \ldots ,\ n
$$
each node has to have exactly $2$ incident arcs.
Note that this constraint is also equivalent to:
$$
\sum_i \sum_j b_{ij} = n - 1 
$$
in the tour there are exactly $n-1$ arcs.

$$
\sum_{b \ \in \ \text{arcs}} b_{ij} <= \text{number of nodes in arcs} - 1 \kern 30px \forall \ \text{arcs} \in S
$$
- $\text{arcs}$ is a set of arcs of the graph.
- S is a set containing all possible combination of arcs in the graph. 
**no-cycles** -> Given all possible combination of arcs we have that each combination has to have a number of "active" arcs ($b_{ij} = 1$) less or equal than the number of nodes less $1$ present in the combination. (otherwise it would be a cycle)

---
##### MTZ Mathematical Formulation for TSP
*A genius way to describe the TSP*
The labelling complexity of the MTZ Formulation is $O(n^2)$ which is a lot smaller than the DFJ Formulation (which is exponential), tho the DFJ is usually better in real world application. 
- **Variables**:
$b_{ij}$ : boolean, $1$ if edge $(i,j)$ belongs to $TSP^*$, $0$ otherwise.
$p_{i}$ : integer, auxiliary variable, it creates a vector of $n$ values where each variable corresponds to node $i$ and its value corresponds to the index of node $i$ in the path that starts from node $1$ and travels across all nodes.
							<br>
- **Constants**:
$c_{ij}$ : weight of arc $(i, j)$
$n$ : number of nodes
							<br>
- **Objective function**:
$$
\min \overline{b} \cdot \overline{c}
$$
							<br>
- **Constraints**:
$$
\sum_k b_{kj} + \sum_k b_{ik} = 2 \kern30px \forall \ k = 1 ,\ 2 ,\ \ldots ,\ n
$$
each node has to have exactly $2$ incident arcs.
							<br>
$$
\begin{align}
& p_1 = 1
\\[5px]
& 2 \le p_i \le n \kern30px \forall \ i  = 1 ,\ 2 ,\ \ldots ,\ n
\\[5px]
& p_{i} - p_{j} + n \kern2px b_{ij} \le n - 1
\end{align}
$$
This constraints define a path from node $1$ that travels across all nodes.
If this path exist than there can be no cycles.
Let's see what happens to the last constraint if $b_{ij} = 0$:
-> $p_{i} - p_{j} \le n - 1$
Which is always true given the second constraint: $2 \le p_i \le n$, so we say that if $b_{ij} = 0$ this constraint are free.
What happens if $b_{ij} = 1$:
-> $p_{i} - p_{j} + n \le n - 1$
-> $p_{i} - p_{j} \le 1$
-> $p_{i} \le p_{j} +  1$
So we say that node $j$ has index $1$ more node $i$, if we put them all together for all nodes we will have an array of values starting from node $1$ with value $1$ (for the constraint $p_1 = 1$), and all the other nodes with increasing values from $2$ to $n$.
~ For example:
node number 1 = 1
node number 2 = 7
node number 3 = 2
$\vdots$