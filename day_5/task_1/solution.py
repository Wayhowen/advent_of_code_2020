from math import ceil


class Solver:
    def __init__(self, task_input, **kwargs):
        self.task_input = task_input
        self.kwargs = kwargs

    def solve(self):
        seats = [Seat(seat_input) for seat_input in self.task_input]
        output = 0

        for seat in seats:
            if seat.id > output:
                output = seat.id

        return output

class Seat:
    def __init__(self, binary_encoding):
        self.row = self._get_row(binary_encoding[:7])
        self.column = self._get_column(binary_encoding[7:])
        self.id = self._calculate_seat_id()

    def _get_row(self, binary_encoding):
        return self._decode_binary(binary_encoding, seats=[0, 127])

    def _get_column(self, binary_encoding):
        return self._decode_binary(binary_encoding, seats=[0, 7])

    def _decode_binary(self, binary_encoding, seats=None):
        for letter in binary_encoding:
            # upper
            if letter in ["B", "R"]:
                seats[0] += ceil((seats[1]-seats[0])/2)
            # lower
            elif letter in ["F", "L"]:
                seats[1] -= ceil((seats[1]-seats[0])/2)
        if seats[0] == seats[1]:
            return seats[0]

    def _calculate_seat_id(self):
        return (self.row * 8) + self.column
