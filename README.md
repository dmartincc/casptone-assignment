# Capstone projects assignment model

We use a Constraint programming model to solve the assignment problem between teams and projects.

Decision variables:

$x_{w,t}$ = A binary variable equal to 1 if team $𝑤∈𝑊$ is working on project $t∈𝑇$ and 0 if not.

Data input:

$T_{w}$ = Number teams that can be assigned to each project $𝑤∈𝑊$.

N = Maximum number of teams working in a project.

$C_{w,t}$ = Ranking matrix of preferences for each group and project.

The model:

$$ min \sum_{w∈𝑊} \sum_{t∈𝑇} x_{w, t} · C_{w, t}  (1) $$

Subject to:

$$ \sum_{𝑤∈𝑊} \sum_{t∈𝑇} x_{w,t} · T_{w}  >= 1,  \forall 𝑤∈𝑊 (2)$$

$$ \sum_{t∈𝑇} \sum_{w∈𝑊} x_{w,t}  <= N,  \forall 𝑤∈𝑊 (3) $$

$$ x_{w, t} ∈ {0, 1},  \forall w∈𝑊, \forall t∈𝑇 (4) $$


The objective function (1) tries to minimize the total ranking for all teams and projects. This means to pick the least value from the rankings, first positions. Constraint (2) makes sure that each team is assigned to one project. Constraint (3) makes sure that each project is assigned no more than N times, proportional to the fraction between teams and projects. Assignment variables (4) force to be binary 0 or 1.



