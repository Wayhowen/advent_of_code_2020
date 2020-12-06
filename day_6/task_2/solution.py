class Solver:
    def __init__(self, task_input, **kwargs):
        self.task_input = task_input
        self.kwargs = kwargs

    def solve(self):
        groups = self._preprocess_data(self.task_input)
        answer_groups = [GroupAnswer(group) for group in groups]

        output = 0
        for answer_group in answer_groups:
            output += answer_group.yes_count

        return output

    def _preprocess_data(self, data):
        groups = []
        group = []
        for iteration, line in enumerate(data):
            if line != "":
                group.append(line)
            else:
                groups.append(group)
                group = []
            if iteration == (len(data) - 1):
                groups.append(group)
        return groups


class GroupAnswer:
    def __init__(self, group_data):
        self.letters = {}
        self.yes_count = 0
        self._count_all_answers(group_data)
        self._count_all_mutual_yes_answers(group_data)

    def _count_all_answers(self, group_data):
        for data in group_data:
            for letter in data:
                if letter not in self.letters:
                    self.letters[letter] = 1
                else:
                    self.letters[letter] += 1

    def _count_all_mutual_yes_answers(self, group):
        for occurences in self.letters.values():
            if occurences == len(group):
                self.yes_count += 1
