class Solver:
    def __init__(self, task_input, **kwargs):
        self.task_input = task_input
        self.kwargs = kwargs

    def solve(self):
        rules = [Rule(entry) for entry in self.task_input]
        output = [rule.is_valid() for rule in rules].count(True)
        return output


class Rule:
    def __init__(self, entry):
        rule = self._extract_passoword(entry)
        self.first_position = int(rule["first_position"])-1
        self.second_position = int(rule["second_position"])-1
        self.letter = rule["letter"]
        self.password = rule["password"]

    def _extract_passoword(self, entry):
        rule = {}
        data = entry.split()
        numbers = data[0].split("-")
        rule["first_position"], rule["second_position"] = numbers
        rule["letter"] = data[1].replace(":", "")
        rule["password"] = data[2].strip()
        return rule

    def is_valid(self):
        letters = self.password[self.first_position] + self.password[self.second_position]
        if letters.count(self.letter) == 1:
            return True
        return False
