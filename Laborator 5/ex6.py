class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.checked_out = False

    def display_info(self):
        return f"{self.title} (ID: {self.item_id})"

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} checked out successfully."
        else:
            return f"{self.title} is already checked out."

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} returned successfully."
        else:
            return f"{self.title} is not checked out."


class Book(LibraryItem):
    def __init__(self, title, item_id, author, num_pages):
        super().__init__(title, item_id)
        self.author = author
        self.num_pages = num_pages

    def display_info(self):
        return f"{super().display_info()}, Author: {self.author}, Pages: {self.num_pages}"


class DVD(LibraryItem):
    def __init__(self, title, item_id, director, duration):
        super().__init__(title, item_id)
        self.director = director
        self.duration = duration

    def display_info(self):
        return f"{super().display_info()}, Director: {self.director}, Duration: {self.duration} minutes"


class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def display_info(self):
        return f"{super().display_info()}, Issue Number: {self.issue_number}"


book = Book(title="Jane Eyre", item_id="B001", author="Charlotte Bronte", num_pages=400)
print(book.display_info())
print(book.check_out())
print(book.return_item())

dvd = DVD(title="Inception", item_id="D001", director="Christopher Nolan", duration=148)
print(dvd.display_info())
print(dvd.check_out())
print(dvd.check_out())

magazine = Magazine(title="National Geographic", item_id="M001", issue_number=255)
print(magazine.display_info())
print(magazine.return_item())
