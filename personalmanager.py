def display_menu():
    print("Welcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    publication_year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == 'yes'
    
    # Check if the book already exists
    for book in library:
        if book['title'].lower() == title.lower():
            print("This book is already in your library.")
            return
    
    library.append({
        'title': title,
        'author': author,
        'publication_year': publication_year,
        'genre': genre,
        'read_status': read_status
    })
    print("Book added successfully!")

def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

def search_book(library):
    search_by = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
    if search_by == '1':
        title = input("Enter the title: ")
        matching_books = [book for book in library if book['title'].lower() == title.lower()]
    elif search_by == '2':
        author = input("Enter the author: ")
        matching_books = [book for book in library if book['author'].lower() == author.lower()]
    else:
        print("Invalid choice.")
        return

    if matching_books:
        print("Matching Books:")
        for i, book in enumerate(matching_books, start=1):
            read_status = "Read" if book['read_status'] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {read_status}")
    else:
        print("No matching books found.")

def display_all_books(library):
    if library:
        print("Your Library:")
        for i, book in enumerate(library, start=1):
            read_status = "Read" if book['read_status'] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {read_status}")
    else:
        print("Your library is empty.")

def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("No books in the library.")
        return
    read_books = sum(book['read_status'] for book in library)
    percentage_read = (read_books / total_books) * 100
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

def main():
    library = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_book(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
