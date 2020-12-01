class Solver:
    def __init__(self, task_input, **kwargs):
        self.task_input = task_input
        self.kwargs = kwargs

    def solve(self):
        output = self.find_two_expenses_summing_to(self.task_input, self.kwargs['summing_to'])
        return output

    def find_two_expenses_summing_to(self, expenses, summing_to):
        for iteration, expense in enumerate(expenses):
            for second_expense in expenses[iteration+1:]:
                if expense + second_expense == summing_to:
                    return expense * second_expense
