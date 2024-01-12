class LibraryItem:
    def __init__(self, title, item_id, num_copies):
        self.title = title
        self.item_id = item_id
        self.num_copies = num_copies
        self.checked_out = 0  # Number of copies checked out

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Item ID: {self.item_id}")
        print(f"Total Copies: {self.num_copies}")
        print(f"Copies Checked Out: {self.checked_out}")

    def check_out(self, num_copies):
        if self.checked_out + num_copies <= self.num_copies:
            self.checked_out += num_copies
            print(f"{num_copies} copies of {self.title} checked out successfully.")
        else:
            print(f"Sorry, not enough copies available for {self.title}.")

    def check_in(self, num_copies):
        if self.checked_out >= num_copies:
            self.checked_out -= num_copies
            print(f"{num_copies} copies of {self.title} checked in successfully.")
        else:
            print(f"Invalid check-in. {num_copies} copies not checked out for {self.title}.")


class Book(LibraryItem):
    def __init__(self, title, item_id, num_copies, author):
        super().__init__(title, item_id, num_copies)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")


class DVD(LibraryItem):
    def __init__(self, title, item_id, num_copies, director):
        super().__init__(title, item_id, num_copies)
        self.director = director

    def display_info(self):
        super().display_info()
        print(f"Director: {self.director}")


class Journal(LibraryItem):
    def __init__(self, title, item_id, num_copies, publisher):
        super().__init__(title, item_id, num_copies)
        self.publisher = publisher

    def display_info(self):
        super().display_info()
        print(f"Publisher: {self.publisher}")


# Example usage:
book_item = Book(title="The Catcher in the Rye", item_id="B001", num_copies=5, author="J.D. Salinger")
dvd_item = DVD(title="Inception", item_id="D001", num_copies=3, director="Christopher Nolan")
journal_item = Journal(title="Scientific American", item_id="J001", num_copies=10, publisher="Nature Publishing Group")

# Display information for each library item
print("Book Information:")
book_item.display_info()

print("\nDVD Information:")
dvd_item.display_info()

print("\nJournal Information:")
journal_item.display_info()

# Check out and check in operations
book_item.check_out(2)
dvd_item.check_out(1)
journal_item.check_in(3)

# Display updated information after operations
print("\nUpdated Information:")
book_item.display_info()
dvd_item.display_info()
journal_item.display_info()
