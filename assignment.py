from ortools.sat.python import cp_model


def main():
    
    # Data - Ranking matrix of each worker preferences
    costs = [
        [7,	1,	7,	4,	6,	6,	5,	6],
        [8,	6,	4,	2,	2,	4,	4,	6],
        [6,	6,	6,	1,	4,	2,	8,	8],
        [1,	1,	7,	3,	7,	1,	6,	3],
        [8,	1,	8,	1,	4,	7,	2,	3],
        [5,	4,	2,	1,	2,	4,	1,	8],
        [2,	1,	4,	3,	2,	7,	6,	1],
        [5,	5,	2,	6,	6,	4,	5,	4],
        [1,	2,	5,	1,	6,	2,	4,	4],
        [7,	5,	6,	8,	7,	2,	2,	7],
        [4,	2,	8,	4,	3,	5,	5,	3],
        [8,	6, 1,	2,	3,	8,	3,	5],
        [8,	2,	2,	3,	7,	2,	1,	7],
        [3,	2,	1,	7,	1,	5,	7,	2],
        [2,	5,	8,	4,	8,	2,	1,	5]
    ]
    num_workers = len(costs)
    num_tasks = len(costs[0])

    task_sizes = [2, 2, 2, 2, 2, 2, 2, 2]
    
    # Maximum total of task sizes for any worker
    total_size_max = 1
    
    # Maximum total of workers sizes for any task
    total_size_max_tasks = 2

    # Model
    model = cp_model.CpModel()

    # Variables
    x = {}
    for worker in range(num_workers):
        for task in range(num_tasks):
            x[worker, task] = model.NewBoolVar(f'x[{worker},{task}]')

    # Constraints
    # Each worker is assigned at one task
    for worker in range(num_workers):
        model.Add(
            sum(task_sizes[task] * x[worker, task]
                for task in range(num_tasks)) >= total_size_max)

    # Each task is assigned to no more than two workers
    for task in range(num_tasks):
        model.Add(
            sum(x[worker, task]
                for worker in range(num_workers)) <= total_size_max_tasks)

    # Objective
    objective_terms = []
    for worker in range(num_workers):
        for task in range(num_tasks):
            objective_terms.append(costs[worker][task] * x[worker, task])
    model.Minimize(sum(objective_terms))

    # Solve
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Print solution.
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f'Total cost = {solver.ObjectiveValue()}\n')
        for worker in range(num_workers):
            for task in range(num_tasks):
                if solver.BooleanValue(x[worker, task]):
                    print(f'Group {worker} assigned to project {task}.' +
                          f' Cost = {costs[worker][task]}')
    else:
        print('No solution found.')


if __name__ == '__main__':
    main()