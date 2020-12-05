import re

# TODO: change to regexes
class Solver:
    def __init__(self, task_input, **kwargs):
        self.task_input = task_input
        self.kwargs = kwargs

    def solve(self):
        passport_data = self._preprocess_data(self.task_input)
        passports = [Passport(passport) for passport in passport_data]
        valid_passports = [pas.is_valid() for pas in passports]
        output = valid_passports.count(True)

        return output

    def _preprocess_data(self, unprocessed_data):
        passport_data = []
        temp_passport = {}
        for iteration, line in enumerate(unprocessed_data):
            if line != "":
                line_data = line.split(" ")
                for data in line_data:
                    temp_passport[data.split(":")[0]] = data.split(":")[1]
            elif line == "":
                passport_data.append(temp_passport)
                temp_passport = {}
            if iteration == (len(unprocessed_data) - 1):
                passport_data.append(temp_passport)
        return passport_data


class Passport:
    def __init__(self, passport_data):
        self.required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        self.optional_fields = ["cid"]
        self.passport_data = passport_data

    def is_valid(self):
        for field in self.required_fields:
            if field in self.passport_data:
                method = getattr(self, f"_{field}_rule")
                result = method(self.passport_data[field])
                if result is False:
                    return result
            else:
                return False
        return True

    def _byr_rule(self, val):
        for char in val:
            try:
                int(char)
            except:
                return False
        return 2002 >= int(val) >= 1920 and len(val) == 4

    def _iyr_rule(self, val):
        for char in val:
            try:
                int(char)
            except:
                return False
        return 2020 >= int(val) >= 2010 and len(val) == 4

    def _eyr_rule(self, val):
        for char in val:
            try:
                int(char)
            except:
                return False
        return 2030 >= int(val) >= 2020 and len(val) == 4

    def _hgt_rule(self, val):
        numbers = ""
        letters = ""
        for char in val:
            try:
                int(char)
                numbers = numbers + char
            except:
                letters = letters + char
        if letters == "cm":
            return 193 >= int(numbers) >= 150
        elif letters == "in":
            return 76 >= int(numbers) >= 59
        return False

    def _hcl_rule(self, val):
        if val[0] == "#":
            if len(val[1:]) == 6:
                for char in val[1:]:
                    pattern = re.compile(r"[a-f]|[0-9]")
                    if pattern.fullmatch(char):
                        return True
                    else:
                        return False
        return False

    def _ecl_rule(self, val):
        if val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return True
        return False

    def _pid_rule(self, val):
        if len(val) == 9:
            try:
                int(val)
                return True
            except:
                return False
        return False