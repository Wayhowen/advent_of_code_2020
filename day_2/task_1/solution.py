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
        self.min_times = int(rule["min_times"])
        self.max_times = int(rule["max_times"])
        self.letter = rule["letter"]
        self.password = self._extract_password_to_letters_dict(rule["password"])

    def _extract_passoword(self, entry):
        rule = {}
        data = entry.split()
        numbers = data[0].split("-")
        rule["min_times"], rule["max_times"] = numbers
        rule["letter"] = data[1].replace(":", "")
        rule["password"] = data[2].strip()
        return rule

    def _extract_password_to_letters_dict(self, password):
        letters = {}
        for letter in password:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        return letters

    def is_valid(self):
        if self.letter in self.password:
            if self.min_times <= self.password[self.letter] <= self.max_times:
                return True
        return False
