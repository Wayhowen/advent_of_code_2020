class Solver:
    def __init__(self, task_input, **kwargs):
        self.task_input = task_input
        self.kwargs = kwargs

    def solve(self):
        expenses = [int(num) for num in self.task_input]
        output = self.find_three_expenses_summing_to(expenses, self.kwargs['summing_to'])
        return output

    def find_three_expenses_summing_to(self, expenses, summing_to):
        for iteration, expense in enumerate(expenses):
            for second_expense in expenses[iteration+1:]:
                for third_expense in expenses[iteration+2:]:
                    if expense + second_expense + third_expense == summing_to:
                        return expense * second_expense * third_expense
