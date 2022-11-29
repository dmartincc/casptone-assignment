# Capstone projects assignment model

We use a Constraint programming model to solve the assignment problem between teams and projects.

Data input: 

$C_{w,t}$ = Ranking matrix of preferences for each group and project.

Decision variables:

$x_{w,t}$ = A binary variable equal to 1 if worker $𝑤∈𝑊$ is working on task $t∈𝑇$ and 0 if not.

Constants:

$T_{w}$ = Number workers that can be assigned to each task $𝑤∈𝑊$.

N = Maximum number of workers working in a task.

The model:


$$ min \sum_{w∈𝑊} \sum_{t∈𝑇} x_{w, t} · C_{w, t} $$

Subject to:

$$ \sum_{𝑤∈𝑊} \sum_{t∈𝑇} x_{w,t} · T_{w}  >= 1 \> \forall 𝑤∈𝑊 $$

$$ \sum_{t∈𝑇} \sum_{w∈𝑊} x_{w,t}  <= N \> \forall 𝑤∈𝑊 $$

$$ x_{w, t} ∈ {0, 1} \>  \forall w∈𝑊, \forall t∈𝑇  $$



