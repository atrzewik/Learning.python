from FileOperator import FileOperator
numbers = FileOperator("data/data21.txt").change_to_integer()

print(numbers)
print(type(numbers))


class Calculations(object):

    def __init__(self, data):
        self.data_one = data[1]
        self.right_list = data[2:]

    def how_many(self):
        one = self.data_one #do wywalenia
        all = self.right_list   #do wywalenia
        result = ""
        for i in range(0, one): #one zamienic na self.data_one
            sums = 0
            for n in all:   #all do zamiany jw.
                if i + 1 == n:
                    sums += 1
            result += " " + str(sums)
        return result


print(Calculations(numbers).how_many())
