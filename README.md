# Capstone projects assignment model

We use a Constraint programming model to solve the assignment problem between teams and projects.

Data input $C_{i,j}$: A ranking matrix of preferences for each group and project.

Decision variables:

$x_{i,j bvc}$ Binary variable: 1 if worker 𝑤∈𝑊 is working on task 𝑡∈𝑇 and 0 if not.

The model:


$$ min z = \sum_{k=1} x_{i, j} · C_{i,j} $$


