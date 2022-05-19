import csv
import random
from botomatic import TBot

data_file = "kindle.csv"

class BookBookGooseBot(TBot):
    debug_mode = False

    def __init__(self):
        handle = "bookbookgoose"
        super(BookBookGooseBot, self).__init__(handle)

    def run(self):
        r = csv.reader(open(data_file))
        books = list(r)
        random.shuffle(books)
        book = books.pop()

        book_text = f'{book[1]}, by {book[0]}'

        self.tweets.append(book_text[:117] + ' ' + book[2])

        self.wrap_up()

if __name__ == '__main__':
    b = BookBookGooseBot()
