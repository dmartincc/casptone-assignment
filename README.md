# Capstone projects assignment model

We use a Constraint programming model to solve the assignment problem between teams and projects.

Data input $C_{w,t}$: A ranking matrix of preferences for each group and project.

Decision variables:

$x_{w,t}$ Binary variable: 1 if worker $𝑤∈𝑊$ is working on task $𝑡∈𝑇$ and 0 if not.

The model:


$$ min \sum_{𝑤∈𝑊} \sum_{𝑡∈𝑇} x_{w, t} · C_{w, t} $$

Subject to:

$$ \sum_{𝑡∈𝑇} x_{w,t} = 1 \forall 𝑤∈𝑊 $$


