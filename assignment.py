
import csv
from ortools.sat.python import cp_model


def main():
    
    # Data - Ranking matrix of each worker preferences
    costs = []
    with open("rankings.tsv") as file:
        tsv_file = csv.reader(file, delimiter="\t")
        for line in tsv_file:
            costs.append([int(item) for item in line])
   
    num_workers = len(costs)
    num_tasks = len(costs[0])
    
    # Maximum total of task sizes for any worker
    total_size_max = 1
    
    # Maximum total of workers sizes for any task
    total_size_max_tasks = round(num_workers / num_tasks)

    # Model
    model = cp_model.CpModel()

    # Variables
    x = {}
    for worker in range(num_workers):
        for task in range(num_tasks):
            x[worker, task] = model.NewBoolVar(f'x[{worker},{task}]')

    # Constraints
    # Each worker is assigned to one task
    for worker in range(num_workers):
        model.Add(
            sum(x[worker, task]
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
                    print(f'Group {worker + 1} assigned to project {task + 1}.' +
                          f' Cost = {costs[worker][task]}')
    else:
        print('No solution found.')


if __name__ == '__main__':
    main()