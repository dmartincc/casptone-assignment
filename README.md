# Capstone projects assignment model

We use a Constraint programming model to solve the assignment problem between teams and projects.

Decision variables:

$x_{w,t}$ = A binary variable equal to 1 if team $๐คโ๐$ is working on project $tโ๐$ and 0 if not.

Data input:

$T_{w}$ = Number teams that can be assigned to each project $๐คโ๐$.

N = Maximum number of teams working in a project.

$C_{w,t}$ = Ranking matrix of preferences for each group and project.

The model:

$$ min \sum_{wโ๐} \sum_{tโ๐} x_{w, t} ยท C_{w, t}  (1) $$

Subject to:

$$ \sum_{๐คโ๐} \sum_{tโ๐} x_{w,t} ยท T_{w}  >= 1,  \forall ๐คโ๐ (2)$$

$$ \sum_{tโ๐} \sum_{wโ๐} x_{w,t}  <= N,  \forall ๐คโ๐ (3) $$

$$ x_{w, t} โ {0, 1},  \forall wโ๐, \forall tโ๐ (4) $$


The objective function (1) tries to minimize the total ranking for all teams and projects. This means to pick the least value from the rankings, first positions. Constraint (2) makes sure that each team is assigned to one project. Constraint (3) makes sure that each project is assigned no more than N times, proportional to the fraction between teams and projects. Assignment variables (4) force to be binary 0 or 1.



