"""
Author : Efe Yılmaz Taşyürek

"""

import sys
import time

class library:

    lines = []
    books = []

    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = open(file_name, mode)

    def reading_file(self):
        context = ""
        context = self.file.read()
        context = context.rstrip("\n")
        self.lines = context.splitlines()
        self.lines = list(filter(None, map(str.strip, self.lines)))

    def show_to_list(self):
        self.books = []
        count = 0
        for i in self.lines:
            book = self.lines[count].split(",")
            self.books.append(book)
            count += 1

        index_for_list = 0
        for i in self.books:
            print(f"{index_for_list+1}.book name: {self.books[index_for_list][0]}, Author: {self.books[index_for_list][1]}")
            index_for_list +=1

    def add_book(self):
        input_str = input("Enter book name, author, release date, number of pages separated by commas: ")
        book_name, author, release_date, number_of_pages = list(map(str.strip, input_str.split(",")))

        if not (book_name and author and release_date and number_of_pages):
            print("Invalid input. Please provide all the required information.")
            return

        book = "\n" + book_name + "," + author + "," + release_date + "," + number_of_pages
        self.file.write(book)

    def remove_book(self):

        remove_book = input("Enter the title of the book to remove")
        self.books = []
        count = 0
        for i in self.lines:
            book = self.lines[count].split(",")
            self.books.append(book)
            count += 1

        index_for_iter = 0
        for i in self.books:
            if(self.books[index_for_iter][0] == remove_book):
                del self.books[index_for_iter]
            index_for_iter +=1

        self.file.close()
        with open("Book.txt", "w") as file:
            file.write("")
            for index_for_write_iter, book in enumerate(self.books[:-1]):
                line = ','.join(map(str, book))
                line = line + "\n"
                file.write(line)

            last_line = ','.join(map(str, self.books[-1]))
            file.write(last_line)
            file.close()


    def __del__(self):
        self.file.close()


file = "Book.txt"
selection = ""


default_mode = "r"
append_mode = "+a"
write_mode = "w"
write_and_read_mode = "+r"

while True:
    print("\n")
    print("1-)List Books")
    print("2-)Add Book")
    print("3-)Remove Book")
    print("İf you want to quit please press \"q\" button.")
    selection = input("Select the action you want to perform: ")
    print("\n")


    if(selection == "1"):
        lib = library(file, default_mode)
        lib.reading_file()
        print("Books are listed...")
        time.sleep(1)
        lib.show_to_list()
        lib.__del__()

    elif(selection == "2"):
        lib = library(file, append_mode)
        lib.add_book()
        print("Book added to the list.")
        time.sleep(1)
        lib.__del__()

    elif(selection == "3"):
        lib = library(file, write_and_read_mode)
        lib.reading_file()
        lib.remove_book()
        print("The book is being removed")
        time.sleep(1)

    elif(selection == "q"):
        print("System is shutting down.")
        time.sleep(1)
        sys.exit()

    else:
        print("You have logged in incorrectly, please try again.\n")