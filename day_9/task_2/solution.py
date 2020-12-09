class Solver:
    def __init__(self, task_input, **kwargs):
        self.task_input = task_input
        self.kwargs = kwargs

    def solve(self):
        output = 0
        self.task_input = [int(tsk_inpt) for tsk_inpt in self.task_input]

        desired_number = 776203571
        additional_numbers = 1
        while True:
            if additional_numbers > 999:
                break
            for index, number in enumerate(self.task_input):
                if index + additional_numbers < len(self.task_input):
                    numbers = [number] + [self.task_input[num+1] for num in range(index, index+additional_numbers)]
                    if self._numbers_add_up_to(numbers, desired_number):
                        output = min(numbers) + max(numbers)
                        break
            additional_numbers += 1

        return output

    def _numbers_add_up_to(self, numbers, result):
        addition_result = 0
        for number in numbers:
            addition_result += number
        return addition_result == result
