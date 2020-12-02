from utils import FileReader
from day_1.task_1.solution import Solver as Task1Day1Solver
from day_1.task_2.solution import Solver as Task2Day1Solver
from day_2.task_1.solution import Solver as Task1Day2Solver


def main():
    reader = FileReader()

    expenses_1 = reader.read_file("day_1/task_1/input.txt")
    task1_day1_solver = Task1Day1Solver(expenses_1, summing_to=2020)
    task1_day1_answer = task1_day1_solver.solve()
    print(task1_day1_answer)

    expenses_2 = reader.read_file("day_1/task_2/input.txt")
    task2_day1_solver = Task2Day1Solver(expenses_2, summing_to=2020)
    task2_day1_answer = task2_day1_solver.solve()
    print(task2_day1_answer)

    rules_1 = reader.read_file("day_2/task_1/input.txt")
    task1_day2_solver = Task1Day2Solver(rules_1)
    task1_day2_answer = task1_day2_solver.solve()
    print(task1_day2_answer)


if __name__ == "__main__":
    main()
