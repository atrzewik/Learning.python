from FileOperator import FileOperator
letters = FileOperator("data/data25.txt").get_data_splitted_by_separator()


class MatchingWords(object):

    def __init__(self, data):
        self.data = data

    def matching(self):
        words = []
        letter = self.data
        index = 0
        for i in range(0, 300):
            word = letter[index]
            del letter[index]
            if word in letter:
                words.append(word)
        return words

    def words(self):
        right_words = []
        letter = self.matching()
        index = 0
        for i in range(0, len(letter)):
            word = letter[index]
            del letter[index]
            if word in letter:
                continue
            else:
                right_words.append(word)
        return right_words

    def sorting(self):
        words = self.words()
        words.sort()
        sorted_words = ""
        for word in words:
            sorted_words += " " + word
        return sorted_words


print(MatchingWords(letters).sorting())

