class Solver:
    def __init__(self, task_input, **kwargs):
        self.task_input = task_input
        self.kwargs = kwargs

    def solve(self):
        lines = [Line(entry) for entry in self.task_input]
        counters = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        output = 0

        for right, down in counters:
            position = 0
            trees = 0

            for iteration, line in enumerate(lines[down::down]):
                position += right
                if line[position] == "#":
                    trees += 1

            if output == 0:
                output = trees
            else:
                output = output*trees
        return output


class Line:
    def __init__(self, line):
        self.line = line
        self.line_length = len(line)

    def __getitem__(self, position):
        if position <= self.line_length-1:
            return self.line[position]
        else:
            times_crossed = int(position / self.line_length)
            actual_position = position - (times_crossed*self.line_length)
            return self.line[actual_position]
