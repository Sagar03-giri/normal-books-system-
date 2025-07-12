class Library:
    def _init_(self, book_list):
        self.available_books = book_list

    def display_books(self):
        print("\nAvailable Books:")
        if not self.available_books:
            print("  No books are currently available.")
        else:
            for book in self.available_books:
                print("  -", book)

    def borrow_book(self, book_name):
        if book_name in self.available_books:
            self.available_books.remove(book_name)
            print(f"✅ You have borrowed '{book_name}'.")
        else:
            print(f"❌ Sorry, '{book_name}' is not available or already borrowed.")

    def return_book(self, book_name):
        self.available_books.append(book_name)
        print(f"✅ Thank you for returning '{book_name}'.")


class Student:
    def _init_(self, name):
        self.name = name
        self.borrowed_books = []

    def request_book(self):
        book = input("Enter the name of the book you want to borrow: ")
        return book

    def return_book(self):
        book = input("Enter the name of the book you want to return: ")
        return book


# --- Main Program ---
def main():
    library = Library(["Python Programming", "Data Structures", "Machine Learning", "OOP in Java", "Clean Code"])
    name = input("Enter student name: ")
    student = Student(name)

    while True:
        print("\n==== Library Menu ====")
        print("1. Display all available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            library.display_books()

        elif choice == '2':
            book_name = student.request_book()
            library.borrow_book(book_name)
            student.borrowed_books.append(book_name)

        elif choice == '3':
            book_name = student.return_book()
            library.return_book(book_name)
            if book_name in student.borrowed_books:
                student.borrowed_books.remove(book_name)

        elif choice == '4':
            print(f"\n👋 Goodbye, {student.name}!")
            break

        else:
            print("❗ Invalid choice. Please enter a number between 1 and 4.")

# Run the program
if _name_ == "_main_":
    main()
