class Solver:
    def __init__(self, task_input):
        self.task_input = task_input

    def solve(self):
        expenses = [int(num) for num in self.task_input]
        output = self.find_two_expenses_summing_to(expenses, summing_to=2020)
        return output

    def find_two_expenses_summing_to(self, expenses, summing_to):
        for iteration, expense in enumerate(expenses):
            for second_expense in expenses[iteration+1:]:
                if expense + second_expense == summing_to:
                    return expense * second_expense
