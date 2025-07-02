class library():
    def __init__(self):
        self.__book_list = ["Python Basics", "Java Programming", "C++ Guide", "OOP Concepts"]
    def display_books(self):
        print("Available books: ")
        for books in self.__book_list:
            print(f"{books}")
    def lend_book(self,books):
       found = False
       for b in self.__book_list:
           if b.lower() == books.lower():
               print(f"You have borrowed '{b}'")
               self.__book_list.remove(b)
               found = True
               break
       if not found:
           print("Sorry, book is not available.")
    def add_book(self, books):
       self.__book_list.append(books)
       print(f"The '{books}' is added to the list")

class student(library):
    def __init__(self, student_name):
        super().__init__()
        self.__student_name = student_name
    def get_student_name(self):
        return self.__student_name
    def request_book(self):
        books = input("Enter a book you want to lend:")
        self.lend_book(books)
    def return_book(self):
        books = input("Enter the name of the book you return: ")
        self.add_book(books)

print("📚 Welcome to the College Library!\n")

name = input("Enter your name: ")
stu = student(name)

while True:
    print("\n====== Library Menu ======")
    print("1. Display Available Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        stu.display_books()
    elif choice == '2':
        stu.request_book()
    elif choice == '3':
        stu.return_book()
    elif choice == '4':
        print(f"\nThank you for visiting, {stu.get_student_name()}! See you again.")
        break
    else:
        print("Invalid choice. Please select a valid option (1-4).")
        
        
        
