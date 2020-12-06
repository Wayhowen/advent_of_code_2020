import importlib

from utils import FileReader

DAYS = 6
TASKS = 2


def main():
    reader = FileReader()
    for day in range(1, DAYS + 1):
        for task in range(1, TASKS + 1):
            try:
                task_input = reader.read_file(f"day_{day}/task_{task}/input.txt")
                module = importlib.import_module(f"day_{day}.task_{task}.solution")
                solver = getattr(module, "Solver")(task_input)
                answer = solver.solve()
                print(f"t{task}d{day}: ", answer)
            except (FileNotFoundError, ModuleNotFoundError) as e:
                print(e)
                pass


if __name__ == "__main__":
    main()
