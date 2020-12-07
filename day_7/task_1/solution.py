import re


class Solver:
    def __init__(self, task_input, **kwargs):
        self.task_input = task_input
        self.kwargs = kwargs

    def solve(self):
        rules = [Rule(rule_text) for rule_text in self.task_input]
        rules = {rule.main_bag: rule.can_contain for rule in rules}

        rules_containing = self._find_all_rules_containing("shiny gold", rules)
        output = len(rules_containing)
        return output

    def _find_all_rules_containing(self, bag_name, rules):
        bags = set()
        for bag, inner_bags in rules.items():
            for inner_bag in inner_bags:
                if inner_bag == bag_name:
                    additional_bags = self._find_all_rules_containing(bag, rules)
                    if additional_bags:
                        for additional_bag in additional_bags:
                            bags.add(additional_bag)
                    bags.add(bag)
        return bags

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
