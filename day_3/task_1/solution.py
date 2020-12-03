class Solver:
    def __init__(self, task_input, **kwargs):
        self.task_input = task_input
        self.kwargs = kwargs

    def solve(self):
        lines = [Line(entry) for entry in self.task_input]
        counter = 0
        output = 0
        for line in lines[1:]:
            counter += 3
            if line[counter] == "#":
                output += 1
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
