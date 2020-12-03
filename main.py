from utils import FileReader
from day_1.task_1.solution import Solver as Task1Day1Solver
from day_1.task_2.solution import Solver as Task2Day1Solver
from day_2.task_1.solution import Solver as Task1Day2Solver
from day_2.task_2.solution import Solver as Task2Day2Solver
from day_3.task_1.solution import Solver as Task1Day3Solver
from day_3.task_2.solution import Solver as Task2Day3Solver


def main():
    reader = FileReader()

    expenses_1 = reader.read_file("day_1/task_1/input.txt")
    task1_day1_solver = Task1Day1Solver(expenses_1, summing_to=2020)
    task1_day1_answer = task1_day1_solver.solve()
    print("t1d1: ", task1_day1_answer)

    expenses_2 = reader.read_file("day_1/task_2/input.txt")
    task2_day1_solver = Task2Day1Solver(expenses_2, summing_to=2020)
    task2_day1_answer = task2_day1_solver.solve()
    print("t2d1: ", task2_day1_answer)

    rules_1 = reader.read_file("day_2/task_1/input.txt")
    task1_day2_solver = Task1Day2Solver(rules_1)
    task1_day2_answer = task1_day2_solver.solve()
    print("t1d2: ", task1_day2_answer)

    rules_2 = reader.read_file("day_2/task_2/input.txt")
    task2_day2_solver = Task2Day2Solver(rules_2)
    task2_day2_answer = task2_day2_solver.solve()
    print("t2d2: ", task2_day2_answer)

    lines_1 = reader.read_file("day_3/task_1/input.txt")
    task1_day3_solver = Task1Day3Solver(lines_1)
    task1_day3_answer = task1_day3_solver.solve()
    print("t1d3: ", task1_day3_answer)

    lines_2 = reader.read_file("day_3/task_2/input.txt")
    task2_day3_solver = Task2Day3Solver(lines_2)
    task2_day3_answer = task2_day3_solver.solve()
    print("t2d3: ", task2_day3_answer)

if __name__ == "__main__":
    main()
