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
                pass
            else:
                return False
        return True
