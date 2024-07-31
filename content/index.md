# NO
###### Network Optimization
- Corso del 1° Anno di Magistrale (2° Semestre).
- Docente: **Marco Pranzo**.
- [Link to Moodle with Video Lectures](https://elearning.unisi.it/course/view.php?id=7799)
										<br>
---
## Perquisites:
- [[Python - Index|Python Programming Language]]

---
## Contents and Program:
- ###### *Introduction*
	- *Nothing to report*
---
# Index - All Notes:
- ### [[NO - Definitions and Need-to-Know Stuff|Definitions and Need-to-Know Stuff]]
<br>
##### All Notes
1. ***[[NO - Chapter 1 (Modified). A quick introduction to Mathematical Programming I|A quick introduction to Mathematical Programming I]]*** ([[NO - Summary of Chapter 1|Summary]])
- [[NO - Mathematical Program]]
- [[NO - Feasible and Optimal Solution]]
- [[NO - Local and Global Optima]]
- [[NO - Relaxation & Restriction of an MP]]
- [[NO - Convex Program]]
										<br>
2. ***[[NO - Chapter 2 (Modified). A quick introduction to Mathematical Programming II|A quick introduction to Mathematical Programming II]]*** ([[NO - Summary of Chapter 2|Summary]])
- [[NO - Linear Program]]
- [[NO - Standard Form of a Linear Program]]
- [[NO - Feasible Solutions for LP (Linear Programs)]]
- [[NO - Optimal Solution for LP (Linear Programs)]]
- [[NO - Geometrical Description of LP (Linear Programs)]]
- [[NO - Classification of LP (Linear Programs)]]
- [[NO - Extreme Points and Vertices]]
- [[NO - Basis and Basic Variables]]
- [[NO - BFS (Basic Feasible Solutions)]]
- [[NO - Degenerate BFS (Basic Feasible Solutions)]]
- [[NO - Find the Optimal Solution in a LP (Linear Program)]]
										<br>
3. ***[[NO - Chapter 3 (Modified). How to solve a Linear Program|How to solve a Linear Program]]*** ([[NO - Summary of Chapter 3|Summary]])
- [[NO - Reduced Costs and Descent Direction]]
- [[NO - Pivot Operation]]
- [[NO - Simplex Method and Auxiliary Problem]]
- [[NO - Approaching a LP (Linear Program)]]
										<br>
4. ***[[NO - Chapter 4. A quick introduction to Complexity|A quick introduction to Complexity]]***
$\mathcal{P}$ problems (**polynomial time**): solved in $O(1)$, $O(n)$, $O(n^2)$, $\ldots$
$\mathcal{NP}$ problems (**non-polynomial time**): solved in $O(2^n)$, $O(n!)$, $O(n^n)$, $\ldots$
Pure **LP** are $\mathcal{P}$ problems, so they can be solved in **polynomial time** (with the *ellipsoid method*) tho in practice the [[NO - Simplex Method and Auxiliary Problem|simplex method]] $O(n!)$ is more efficient.
- [[NO - P (Polynomial) and NP (Non-deterministic Polynomial) Problems]]
										<br>
5. ***[[NO - Chapter 5. A quick introduction to Integer Programming|A quick introduction to Integer Programming]]***
**IP** are a [[NO - Relaxation & Restriction of an MP|restriction]] of **LP** where there is a new constraint where all variables are **integers** ($x \in \mathbb{N}$), so we cannot use the previous seen methods to solve it (there are no more vertices).
An IP can be **Pure** ($x \in \mathbb{N}$), **BIP** (Binary IP, $x \in \{0 ,\ 1 \}$), and **MIP** (Mixed IP, some $x \in \mathbb{N}$ other $x \in \mathbb{R}$)
A few IP have all the vertices as integers (especially graph-related problems), to easily see if the **feasible region** of an IP is an **integer polyhedron** (all vertices of the polyhedron are integer), we can see if the $A$ matrix is a **TUM** (Total Unimodular Matrix).
- [[NO - IP (Integer Programs)]]
- [[NO - TUM (Total Unimodular Matrix)]]
										<br>
6. ***[[NO - Chapter 6. How to solve a MIP (Mixed Integer Program)|How to solve a MIP (Mixed Integer Program)]]***
Here is a collection of **building blocks** or ideas used to solve a **MIP**, remember that these ideas, do no lead to a stand alone algorithm.
Rather they are mixed and adopted in **branch&cut**, **column generations** and more complex algorithmic schemes.
The **Convex Hull** is the **integer polyhedron** (all **integer vertices**) containing all the **feasible integer solutions**.
We can **Cut** the **feasible region** adding a single constraint at a time reducing the **LP** related solution space, but always leaving the entire convex hull intact.
We can create smaller sub-problems (**children**) for a given **parent problem**, these problems are easier to solve, and once we solve all of them we will have that the **optimal solution** of the **children** is the same as the **parent**, for integer problems for example we can fix one variable value and create sub-problems for all possible value that variable can assume.
The inverse of branching is **Bounding** where we find the solution to a relaxed version of the problelm, setting an **UP** Upper Bound to the solution, for integer problems for example we can create a dual **LP** where the constraint of "**integrity**" is void.
- [[NO - Convex Hull]]
- [[NO - Cutting Plane]]
- [[NO - Branching]]
- [[NO - Bounding]]
										<br>
7. ***[[NO - Chapter 7. A quick introduction to Graphs|A quick introduction to Graphs]]***
##### [[NO - Graph Components Cheat-Sheet|Graph Components Cheat-Sheet]] #TODO 
- [[NO - Graph and its components]] (networks, arcs/edges, nodes, network information, multiarcs/loop, path, cycle)
- [[NO - Connected Graph]]
- [[NO - Tree Graph and Forest Graph]]
- [[NO - Bipartite Graph]]
- [[NO - Cutting a Graph and s-t Cut]]
- [[NO - Incidence Matrix]]
- [[NO - Adjacency Matrix]]
- [[NO - Incidence List]]
										<br>
8. ***[[NO - Chapter 8. Max Flow & Min Cut|Max Flow & Min Cut]]***
Max flow and Min Cut problems are a dual-pair problem, that is the minimum capacity of the network is equal to its maximum flow, the Ford-Fulkerson Algorithm is one to find the max flow (and so also the minimum cut), for a visual explanation watch this [video](https://www.youtube.com/watch?v=Tl90tNtKvxs).
> **NOTE**:
> For **Maximum Flow** we mean the maximum possible flow from the **source node** to the **sink node**.
> For **Minimum Cut** we mean the minimum flow across all possible **cut** of the network.
- [[NO - Max Flow & Min Cut Problems]]
- [[NO - Ford-Fulkerson Algorithm]]
										<br>
9. ***[[NO - Chapter 9 (Modified). Minimum Spanning Tree|Minimum Spanning Tree]]*** ([[NO - Summary of Chapter 9|Summary]])

- [[NO - Spanning Tree Graph]]
- [[NO - Differences between Tree Graphs and Spanning Tree Graphs]] #TODO 
- [[NO - Cut Optimality for Spanning Tree Graphs]]
- [[NO - Path Optimality for Spanning Tree Graphs]]
- [[NO - Kruskal and Prim Algorithms of MST (Minimum Spanning Tree)]]
										<br>
10. ***[[NO - Chapter 10 (Modified). Matching|Matching]]*** ([[NO - Summary of Chapter 10|Summary]])
- [[NO - Matching]]
- [[NO - Maximum Cardinality Matching Problem and Solution Algorithms]]
- [[NO - Edmonds Algorithm (Srhinking Blossoms)]]
										<br>
11. ***[[NO - Chapter 11 (Modified). TSP (Travelling Salesman Problem)|TSP (Travelling Salesman Problem)]]***
***Elerian cycle***: cycle that passes once over all **edges** of the graph.
***Hamiltonian cycle***: cycle that passes once over all **nodes** of the graph.
***Triangle inequality***: a property a graph can have, that states that in the graph there are **no shortcuts**.
***Complete Graph***: a graph where every node is connected to all other nodes, also a weighted graph can always be considered completed if we put an infinite cost on the missing arcs.
- [[NO - Eulerian Cycles]]
- [[NO - Hamiltonian Cycles]]
- [[NO - Triangle Inequality]]
- [[NO - TSP (Travelling Salesman Problem)]]
 										<br>
12. ***[[NO - Chapter 12 (Modified). Classification of algorithms|Classification of algorithms]]***
***Exact Algorithms***: search for the exact solution, for example the *mathematica formulation*, and *dynamic programming*.
***Approximate Algorithms***: use properties of the problem to calculate an approximation ration.
***Heuristic Algorithms***: the more time we give the algorithm the better the result.
***Greedy*** Heuristic Algorithms: build a decision at a time, without changing the previous decisions, divide the problem in smaller subproblems that iteratevely find a solution (it might not be the optimal one).
***Metaheuristic*** Algorithms: *exploration* vs. *exploitation* algorithms, some example are: the *local search based algorithm* and the *population based algorithm* (genetic algorithm)
- [[NO - Solution Algorithms (Exact, Approximate, Heuristic)]]
- [[NO - Exact Algorithms]]
- [[NO - Approximate Algorithms]]
- [[NO - Heuristic Algorithms]]
-> [[NO - Greedy (Heuristic) Algorithms]]
-> [[NO - Metaheuristic (Heuristic)  Algorithms]]
										<br>
13. ***[[NO - Chapter 13 (Modified). Construction heuristics for TSP]]***
- [[NO - TSP (Travelling Salesman Problem) Tour Construction]] (***Greedy*** Heuristic Algorithm)
- **Starting point**: 
-> Usually a random city
- **Selection Criteria**:
-> [[NO - TSP (Travelling Salesman Problem) Arbitrary Insertion]]
-> [[NO - TSP (Travelling Salesman Problem) Nearest Neighbour]]
- **Insertion Criteria**:
-> [[NO - TSP (Travelling Salesman Problem) Nearest Addition]]
-> [[NO - TSP (Travelling Salesman Problem) Farthest Addition]]
-> [[NO - TSP (Travelling Salesman Problem) Nearest Merge]]
- Given a TSP$^*$ (optima Travelling Salesman Problem) we have that removing any edge yields a MST, so given a MST how can we create a solution for the TSP
-> [[NO - TSP (Travelling Salesman Problem) & MST (Minimum Spanning Tree)]]
-> [[NO - Christofides's algorithm]] (**Approximate** Algorithm)
										<br>
14. ***[[NO - Chapter 14 (Modified). A quick introduction to Local Search|A quick introduction to Local Search]]***
Given an **initial feasible solution** we **explore** its **neighbours** in the **feasible solutions space** and we search for a better solution.
We explore the neighbourhood of a feasible solution altering the problem variables and see if the new result it's better then the previous.
- [[NO - Local Search]]
- [[NO - Neighbourhood of a Solution]]
- [[NO - Evaluation Function]]
- [[NO - Exploration of the Neighbourhood of a Solution]]
										<br>
15. ***[[NO - Chapter 15 (Modified). Local Search for TSP|Local Search for TSP]]***
For a TSP we can first find a feasible solution, (for example with the [[NO - Christofides's algorithm|Christofides's algorithm]]) then we search for 2 (or more generally $r$ arcs) arcs in the solution such that if they are exchanged (arcs $(i,j)$, $(x,y)$ becomes: arcs $(i,y)$, $(x,j)$) the solution improves.
- [[NO - TSP Edge Exchange r-opt]]
- [[NO - Speed Up for Edge Exchange]]
- [[NO - Data Structure Optimization]] #USEFUL
										<br>
16. ***[[NO - Chapter 16 (Modified). Mathematical Formulation of the TSP|Mathematical Formulation of the TSP]]*** ([[NO - Summary of Chapter 16|Summary]])
- [[NO - Mathematical Formulation of the TSP]]
- [[NO - DFJ Formulation for TSP]]
- [[NO - Strong & Weak Mathematical Formulation]]
- [[NO - MTZ Formulation for the TSP]]
										<br>
17. ***[[NO - Chapter 17 Modified). A quick introduction to Duality|A quick introduction to Duality]]***
> **NOTE**:
> The professor in the slides defined the result of a **Relaxation** as a **LB** (Lower Bound), this is true as long as the original problem is a **minimization problem**, the **feasible solution space** of a relaxation is bigger than that of the original problem, so there is more solution to choose from and in the minimization problem we can find a better solution which will be **LOWER** than the optimal solution of the original problem.
- [[NO - Upper & Lower Bound]]
- [[NO - Relaxing & Restricting]]
- [[NO - Duality]]
- [[NO - Weak Duality]]
- [[NO - Strong Duality]]
										<br>
18. ***[[NO - Chapter 18 (Modified). A quick introduction to Lagrangian Relaxation|A quick introduction to Lagrangian Relaxation]]***
> **NOTE**:
> The professor in the slides defined the result of a **Relaxation** as a **LB** (Lower Bound), this is true as long as the original problem is a **minimization problem**, the **feasible solution space** of a relaxation is bigger than that of the original problem, so there is more solution to choose from and in the minimization problem we can find a better solution which will be **LOWER** than the optimal solution of the original problem.
- [[NO - Legrangean Relaxation]]
- [[NO - Legrangean Problem]]
										<br>
19. ***[[NO - Chapter 19 (Modified). Lower Bounds for TSP|Lower Bounds for TSP]]***
- [[NO - Linear Relaxation]]
- [[NO - Assignment Problem]]
- [[NO - 1-Tree]]
- [[NO - Legrangean Relaxation for TSP]]
										<br>
20. ***[[NO - Chapter 20 (Modified). A quick introduction to Branch&Bound|A quick introduction to Branch&Bound]]***
- [[NO - Branch & Bound]]
- [[NO - Pruned & Solved Problems]]
- [[NO - Ingredients for Branch & Bound]]
- [[NO - Visit Rules for Branch & Bound]]
										<br>
21. ***[[NO - Chapter 21 (Modified). Branch & Bounds for TSP|Branch & Bounds for TSP]]***
- [[NO - Branch & Bound for TSP]]
										<br>
22. ***[[NO - Chapter 22 (Modified). A quick introduction to Cutting Plane|A quick introduction to Cutting Plane]]***
- [[NO - Cutting Plane]]
										<br>
23. ***[[NO - Chapter 23 (Modified). Cutting plane for TSP|Cutting plane for TSP]]***
- [[NO - Cutting Plane for TSP]]
										<br>
24. ***[[NO - Chapter 24 (Modified). A quick introduction to Branch&Cut|A quick introduction to Branch&Cut]]***
![[Pasted image 20220629115024.png]]
- [[NO - Branch & Cut]]
										<br>
25. ***[[NO - Chapter 25. Branch&Cut for TSP|Brunch&Cut for TSP]]***
- [[NO - Branch&Cut for TSP]]
										<br>
##### All Original Slides
- [[NO - Chapter 1. A quick introduction to Mathematical Programming I]]
- [[NO - Chapter 2. A quick introduction to Mathematical Programming II]]
- [[NO - Chapter 3. How to solve a Linear Program]]
- [[NO - Chapter 4. A quick introduction to Complexity]]
- [[NO - Chapter 5. A quick introduction to Integer Programming]]
- [[NO - Chapter 6. How to solve a MIP (Mixed Integer Program)]]
- [[NO - Chapter 7. A quick introduction to Graphs]]
- [[NO - Chapter 8. Max Flow & Min Cut]]
- [[NO - Chapter 9. Minimum Spanning Tree]]
- [[NO - Chapter 10. Matching]]
- [[NO - Chapter 11. TSP (Travelling Salesman Problem)]]
- [[NO - Chapter 12. Classification of algorithms]]
- [[NO - Chapter 13. Construction heuristics for TSP]]
- [[NO - Chapter 14. A quick introduction to Local Search]]
- [[NO - Chapter 15. Local Search for TSP]]
- [[NO - Chapter 16. Mathematical Formulation of the TSP]]
- [[NO - Chapter 17. A quick introduction to Duality]]
- [[NO - Chapter 18. A quick introduction to Lagrangian Relaxation]]
- [[NO - Chapter 19. Lower Bounds for TSP]]
- [[NO - Chapter 20. A quick introduction to Branch&Bound]]
- [[NO - Chapter 21. Branch & Bounds for TSP]]
- [[NO - Chapter 22. A quick introduction to Cutting Plane]]
- [[NO - Chapter 23. Cutting plane for TSP]]
- [[NO - Chapter 24. A quick introduction to Branch&Cut]]
- [[NO - Chapter 25. Branch&Cut for TSP]]

---
## Python Scripts:
- ###### Train Scheduling Problem
![[NO_Project_Exercise_3_v4_GUROBI.ipynb]]
![[no_project_exercise_3_v4_gurobi.py]]
										<br>
- ###### Train Scheduling Problem (Fake Data, no need to access Google to solve it)
![[NO_Project_Exercise_3_v5_GUROBI.ipynb]]
![[no_project_exercise_3_v5_gurobi.py]]
----
###### All My Notes
For the best experience in reading these and all other notes, and also if you wish to EDIT them, do as follows: 
1. Install [Obsidian](https://obsidian.md), or another markdown editor.
2. Go to the Github link of this or another note
3. Download all the repo or if you know git just the 'content/' folder
4. Extract just the 'content/' folder from the repo zip file
5. Open Obsidian >> Menage Vaults >> Open Folder as Vault >> and select the 'content/' folder you just extracted

==PLEASE NOTE==:
- These notes were not revised by the professors, so take all of them with a grain of salt.
- However if you download them since they are made in markdown you can EDIT them, please do so.
- If you edit and "upgrade" them, please pass the new ones to the other students and professors.

Here are all the links to my notes:
- ***Github***: [UNISI-Sensors-and-Microsystems-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-Sensors-and-Microsystems-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-Sensors-and-Microsystems-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-Sensors-and-Microsystems-Obsidian-Quartz-Publish).
- ***Github***: [UNISI-Complex-Dynamic-Systems-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-Complex-Dynamic-Systems-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-Complex-Dynamic-Systems-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-Complex-Dynamic-Systems-Obsidian-Quartz-Publish).
- ***Github***: [UNISI-Discrete-Event-Systems-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-Discrete-Event-Systems-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-Discrete-Event-Systems-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-Discrete-Event-Systems-Obsidian-Quartz-Publish).
- ***Github***: [UNISI-System-Identification-and-Data-Analysis-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-System-Identification-and-Data-Analysis-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-System-Identification-and-Data-Analysis-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-System-Identification-and-Data-Analysis-Obsidian-Quartz-Publish).
- ***Github***: [UNISI-Multivariable-NonLinear-and-Robust-Control-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-Multivariable-NonLinear-and-Robust-Control-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-Multivariable-NonLinear-and-Robust-Control-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-Multivariable-NonLinear-and-Robust-Control-Obsidian-Quartz-Publish).
- ***Github***: [UNISI-Artificial-Intelligence-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-Artificial-Intelligence-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-Artificial-Intelligence-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-Artificial-Intelligence-Obsidian-Quartz-Publish).
- ***Github***: [UNISI-Human-Centered-Robotics-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-Human-Centered-Robotics-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-Human-Centered-Robotics-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-Human-Centered-Robotics-Obsidian-Quartz-Publish).
- ***Github***: [UNISI-Machine-Learning-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-Machine-Learning-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-Machine-Learning-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-Machine-Learning-Obsidian-Quartz-Publish).
- ***Github***: [UNISI-Bioinformatics-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-Bioinformatics-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-Bioinformatics-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-Bioinformatics-Obsidian-Quartz-Publish).
- ***Github***: [UNISI-Network-Optimization-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-Network-Optimization-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-Network-Optimization-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-Network-Optimization-Obsidian-Quartz-Publish).
- ***Github***: [UNISI-Mathematical-Methods-for-Engineering-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-Mathematical-Methods-for-Engineering-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-Mathematical-Methods-for-Engineering-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-Mathematical-Methods-for-Engineering-Obsidian-Quartz-Publish).
