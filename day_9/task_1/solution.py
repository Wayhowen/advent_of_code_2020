class Solver:
    def __init__(self, task_input, **kwargs):
        self.task_input = task_input
        self.kwargs = kwargs

    def solve(self):
        output = 0
        self.task_input = [int(tsk_inpt) for tsk_inpt in self.task_input]

        preamble = self.task_input[:25]
        for number in self.task_input[25:]:
            if self._preamble_adds_up(number, preamble):
                del preamble[0]
                preamble.append(number)
            else:
                output = number
                break

        return output

    def _preamble_adds_up(self, result, preamble):
        for number in preamble:
            for number2 in preamble[1:]:
                if number + number2 == result:
                    return True
        return False
