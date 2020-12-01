from utils import FileReader
from task_1.solution import Solver as Task1Solver
from task_2.solution import Solver as Task2Solver


def main():
    reader = FileReader()

    expenses_1 = reader.read_file("task_1/input.txt")
    task_1_solver = Task1Solver(expenses_1, summing_to=2020)
    task_1_answer = task_1_solver.solve()
    print(task_1_answer)

    expenses_2 = reader.read_file("task_2/input.txt")
    task_2_solver = Task2Solver(expenses_2, summing_to=2020)
    task_2_answer = task_2_solver.solve()
    print(task_2_answer)


if __name__ == "__main__":
    main()
