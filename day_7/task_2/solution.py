import re


class Solver:
    def __init__(self, task_input, **kwargs):
        self.task_input = task_input
        self.kwargs = kwargs

    def solve(self):
        rules = [Rule(rule_text) for rule_text in self.task_input]
        rules = {rule.main_bag: rule.can_contain for rule in rules}

        # - 1 to remove the overall amount set in top level
        output = self._find_how_many_inside("shiny gold", rules) - 1
        return output

    def _find_how_many_inside(self, bag_name, rules):
        overall_amount = 1
        for bag, inner_bags in rules.items():
            if bag == bag_name:
                for inner_bag, amount in inner_bags.items():
                    overall_amount += int(amount) * self._find_how_many_inside(inner_bag, rules)
                    print(inner_bag, overall_amount)
        return overall_amount


class Rule:
    def __init__(self, rule_text):
        self.main_bag = None
        self.can_contain = {}
        self._decode_rule_text(rule_text)

    def _decode_rule_text(self, rule_text):
        no = re.compile(r"\d")
        splitted_text = rule_text.split()
        self.main_bag = f"{splitted_text[0]} {splitted_text[1]}"
        cut_text = splitted_text[4:]
        for index, word in enumerate(cut_text):
            if no.match(word):
                self.can_contain[f"{cut_text[index+1]} {cut_text[index+2]}"] = word
