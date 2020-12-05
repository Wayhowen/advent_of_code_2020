from math import ceil


class Solver:
    def __init__(self, task_input, **kwargs):
        self.task_input = task_input
        self.kwargs = kwargs

    def solve(self):
        seats = [Seat(seat_input) for seat_input in self.task_input]

        present_seats = self._get_present_seats(seats)
        missing_seats = self._find_missing_seats(present_seats)

        seat_ids = {seat.id for seat in seats}

        output = self._find_my_seat(missing_seats, seat_ids)
        return output

    def _get_present_seats(self, seats):
        present_seats = {}
        for seat in seats:
            if present_seats.get(seat.row):
                present_seats[seat.row].add(seat.column)
            else:
                present_seats[seat.row] = {seat.column}
        return present_seats

    def _find_missing_seats(self, present_seats):
        missing_seats = {}
        for row, column in present_seats.items():
            for seat_no in range(0, 7):
                if seat_no not in column:
                    missing_seats[row] = {0, 1, 2, 3, 4, 5, 6, 7} - column
        return missing_seats

    def _find_my_seat(self, missing_seats, seat_ids):
        for row, seats in missing_seats.items():
            multiplied_row = row * 8
            for seat in seats:
                seat_id = multiplied_row + seat
                if seat_id + 1 in seat_ids and seat_id - 1 in seat_ids:
                    return seat_id


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
