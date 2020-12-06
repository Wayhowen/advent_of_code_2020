from utils import FileReader
from day_1.task_1.solution import Solver as Task1Day1Solver
from day_1.task_2.solution import Solver as Task2Day1Solver
from day_2.task_1.solution import Solver as Task1Day2Solver
from day_2.task_2.solution import Solver as Task2Day2Solver
from day_3.task_1.solution import Solver as Task1Day3Solver
from day_3.task_2.solution import Solver as Task2Day3Solver
from day_4.task_1.solution import Solver as Task1Day4Solver
from day_4.task_2.solution import Solver as Task2Day4Solver
from day_5.task_1.solution import Solver as Task1Day5Solver
from day_5.task_2.solution import Solver as Task2Day5Solver
from day_6.task_1.solution import Solver as Task1Day6Solver
from day_6.task_2.solution import Solver as Task2Day6Solver


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

    passports_1 = reader.read_file("day_4/task_1/input.txt")
    task1_day4_solver = Task1Day4Solver(passports_1)
    task1_day4_answer = task1_day4_solver.solve()
    print("t1d4: ", task1_day4_answer)

    passports_2 = reader.read_file("day_4/task_2/input.txt")
    task2_day4_solver = Task2Day4Solver(passports_2)
    task2_day4_answer = task2_day4_solver.solve()
    print("t2d4: ", task2_day4_answer)

    seats_1 = reader.read_file("day_5/task_1/input.txt")
    task1_day5_solver = Task1Day5Solver(seats_1)
    task1_day5_answer = task1_day5_solver.solve()
    print("t1d5: ", task1_day5_answer)

    seats_2 = reader.read_file("day_5/task_2/input.txt")
    task2_day5_solver = Task2Day5Solver(seats_2)
    task2_day5_answer = task2_day5_solver.solve()
    print("t2d5: ", task2_day5_answer)

    questions_1 = reader.read_file("day_6/task_1/input.txt")
    task1_day6_solver = Task1Day6Solver(questions_1)
    task1_day6_answer = task1_day6_solver.solve()
    print("t1d6: ", task1_day6_answer)

    questions_2 = reader.read_file("day_6/task_2/input.txt")
    task2_day6_solver = Task2Day6Solver(questions_2)
    task2_day6_answer = task2_day6_solver.solve()
    print("t2d6: ", task2_day6_answer)


if __name__ == "__main__":
    main()
