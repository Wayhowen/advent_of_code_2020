import importlib

from utils import FileReader

DAYS = 9
TASKS = 2
SKIP_LIST = [(8, 1), (8, 2)]


def main():
    reader = FileReader()
    for day in range(1, DAYS + 1):
        for task in range(1, TASKS + 1):
            if (day, task) not in SKIP_LIST:
                try:
                    task_input = reader.read_file(f"day_{day}/input.txt")
                    module = importlib.import_module(f"day_{day}.task_{task}.solution")
                    solver = getattr(module, "Solver")(task_input)
                    answer = solver.solve()
                    print(f"t{task}d{day}:", answer)
                except (FileNotFoundError, ModuleNotFoundError) as e:
                    print(e)
                    pass


if __name__ == "__main__":
    main()
