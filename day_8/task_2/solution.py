import copy


class Solver:
    def __init__(self, task_input, **kwargs):
        self.task_input = task_input
        self.kwargs = kwargs
        self.accumulator = 0
        self.current_instruction = 0
        self.used_instructions = {0}
        self.terminating = False

    def solve(self):
        instructions = {number: Instruction(instruction) for number, instruction in
                        enumerate(self.task_input)}

        datasets = self._create_datasets(instructions)

        output = None
        for dataset in datasets:
            self._find_if_looping(dataset)
            if self.terminating:
                output = self.accumulator
                break

        return output

    def _create_datasets(self, instructions):
        datasets = []
        for no, instruction in instructions.items():
            new_dataset = copy.deepcopy(instructions)
            if new_dataset[no].command == "nop":
                new_dataset[no].command = "jmp"
                datasets.append(new_dataset)
            elif new_dataset[no].command == "jmp":
                new_dataset[no].command = "nop"
                datasets.append(new_dataset)
        return datasets

    def _find_if_looping(self, instructions):
        while True:
            new_instruction_no = self._execute_instruction(instructions)
            if self._is_instruction_repeated(new_instruction_no):
                self.accumulator = 0
                self.current_instruction = 0
                self.used_instructions = {0}
                break
            elif self._is_terminating(new_instruction_no, len(instructions)):
                self.terminating = True
                break
        return True

    def _execute_instruction(self, instructions):
        instruction = instructions[self.current_instruction]
        if instruction.command == "acc":
            self.accumulator += instruction.value
            self.current_instruction += 1
        elif instruction.command == "jmp":
            self.current_instruction += instruction.value
        elif instruction.command == "nop":
            self.current_instruction += 1
        return self.current_instruction

    def _is_instruction_repeated(self, instruction_no):
        if instruction_no in self.used_instructions:
            return True
        self.used_instructions.add(instruction_no)
        return False

    def _is_terminating(self, instructon_no, len_of_instructions):
        if instructon_no == len_of_instructions:
            return True
        return False

class Instruction:
    def __init__(self, line):
        self.command = line.split(" ")[0]
        self.value = int(line.split(" ")[1])

    def __repr__(self):
        return f"{self.command} {self.value}"
