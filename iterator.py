############################################
#  Iterator
############################################

class Iterator:

    def __init__(self, string):
        self.string = string
        self._position = 0

    def __next__(self):
        try:
            value = self.string[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()

        return value

############################################
#  Iterable
############################################

class Iterable:

    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return Iterator(self.string)

############################################
#  Program Execution
############################################

MyString = Iterable('abc')
list(MyString)
Iter = iter(MyString)

while True:
    # DO
    try:
        print(next(Iter))
    except StopIteration:
        break
# ENDWHILE