class Board(object):

    def __init__(self, number_of_fields):
        self.number_of_fields = number_of_fields
        self.capacity = self.calculate_capacity()
        self.fields = []
        for i in range(number_of_fields):
            self.fields.append(["-"] * number_of_fields)

    def __str__(self):
        new_board = ""
        for row in self.fields:
            new_board += " ".join(row) + "\n"
        return new_board

    def calculate_capacity(self):
        return self.number_of_fields * self.number_of_fields

    def mark_field(self, row, column, sign):
        if self.fields[int(row)][int(column)] != "-":
            raise AttributeError("This field %s, %s is busy." % (row, column))
        else:
            self.fields[int(row)][int(column)] = sign

    def row_winning_condition(self, sign):
        for row_number in range(self.number_of_fields):
            count = 0
            for column_number in range(self.number_of_fields):
                if self.fields[row_number][column_number] == sign:
                    count += 1
            if count == self.number_of_fields:
                return True

    def column_winning_condition(self, sign):
        for row_number in range(self.number_of_fields):
            count = 0
            for column_number in range(self.number_of_fields):
                if self.fields[column_number][row_number] == sign:
                        count += 1
            if count == self.number_of_fields:
                return True

    def diagonal_top_condition(self, sign):
        maximum_value_of_column = self.number_of_fields-1
        for row_number in range(self.number_of_fields):
            count = 0
            for column_number in range(self.number_of_fields):
                if self.fields[column_number][maximum_value_of_column-column_number] == sign:
                    count += 1
            if count == self.number_of_fields:
                return True

    def diagonal_down_condition(self, sign):
        for row_number in range(self.number_of_fields):
            count = 0
            for column_number in range(self.number_of_fields):
                if self.fields[column_number][column_number] == sign:
                    count += 1
            if count == self.number_of_fields:
                return True

    def check_the_winner(self, sign):
        return self.row_winning_condition(sign) or self.column_winning_condition(sign) or self.diagonal_top_condition(
            sign) or self.diagonal_down_condition(sign)


class Game(object):

    def __init__(self):
        self.turn = 0
        print("Hello!", "\n ...")
        self.board = Board(self.get_number_of_fields())
        while True:
            print("Turn: ", self.turn)
            print(self.board)
            self.make_move()
            if not self.continue_game():
                print(self.board)
                break
            self.turn += 1

    def get_number_of_fields(self):
        number = int(input("Please pick number of fields from 2 to 20: "))
        try:
            if number < 2 or number > 20:
                raise AttributeError
        except AttributeError:
            print("You pick wrong number of fields!")
            self.get_number_of_fields()
        else:
            return number

    def whose_move(self):
        if self.turn % 2 == 0:
            return "o"
        else:
            return "x"

    def make_move(self):
        sign = self.whose_move()
        maximum_pick = self.board.number_of_fields - 1
        row = input("Please, enter your row(0-%s) for %s:" % (maximum_pick, sign))
        column = input("Please, enter your column(0-%s) for %s:" % (maximum_pick, sign))
        try:
            self.board.mark_field(row, column, sign)
        except AttributeError:
            print(AttributeError)
            print("You pick wrong answer! Try again")
            self.make_move()

    def continue_game(self):
        sign = self.whose_move()
        if self.board.check_the_winner(sign):
            print("The winner is %s" % sign)
            return False
        elif self.turn == self.board.capacity:
            print("Remis!")
            return False
        else:
            return True


# print(Game())

def test_winning_condition_row():
    number_of_fields = 3
    board = Board(number_of_fields)
    board.mark_field(0, 0, 'O')
    board.mark_field(0, 1, 'O')
    board.mark_field(0, 2, 'O')
    print("wywololuje sie?>")
    assert board.check_the_winner('O')


# board = Board(5)
# board.mark_field(0,0,"o")
# board.mark_field(2,3,"x")
# board.mark_field(0,0,"x")
# print (board)
test_winning_condition_row()
print(Game())
