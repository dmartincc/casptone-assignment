# Capstone projects assignment model

We use a Constraint programming model to solve the assignment problem between teams and projects.

Decision variables:

$x_{w,t}$ = A binary variable equal to 1 if team $𝑤∈𝑊$ is working on project $t∈𝑇$ and 0 if not.

Data input:

$T_{w}$ = Number teams that can be assigned to each project $𝑤∈𝑊$.

N = Maximum number of teams working in a project.

$C_{w,t}$ = Ranking matrix of preferences for each group and project.

The model:

$$ min \sum_{w∈𝑊} \sum_{t∈𝑇} x_{w, t} · C_{w, t} $$

Subject to:

$$ \sum_{𝑤∈𝑊} \sum_{t∈𝑇} x_{w,t} · T_{w}  >= 1,  \forall 𝑤∈𝑊 $$

$$ \sum_{t∈𝑇} \sum_{w∈𝑊} x_{w,t}  <= N,  \forall 𝑤∈𝑊 $$

$$ x_{w, t} ∈ {0, 1},  \forall w∈𝑊, \forall t∈𝑇  $$



