class LibraryItem:
    def __init__(self,title: str, author_or_artist:str, publication_year: int, item_identifier:int):
        self.title = title
        self.author_or_artist = author_or_artist
        self.publication_year = publication_year
        self.item_identifier = item_identifier
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"'{self.title}' checked out")
        else:
            print(f"'{self.title}' is already checked out")

    def return_item(self):
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"'{self.title}' returned")
        else:
            print(f"'{self.title}' is already available")
            
            
class Book(LibraryItem):
    def __init__(self, title: str, author_or_artist:str, publication_year: int, item_identifier:int, isbn: str, number_of_pages:int):
        super().__init__(title, author_or_artist, publication_year, item_identifier)
        self.isbn = isbn
        self.number_of_pages = number_of_pages
        
class DVD(LibraryItem):
    def __init__(self, title: str, artist:str, publication_year: int, item_identifier:int, runtime_in_minutes: int, region_code:str):
        super().__init__(title, artist, publication_year, item_identifier)
        self.runtime_in_minutes = runtime_in_minutes
        self.region_code = region_code
        
book1 = Book("The hobbit", "J.R.R. Tolkien", 1930,"B0001","932-345677", 350)
dvd1= DVD("Inception","Christopher Nolan", 2012, "D0001",345,"1")

print(book1)
print(dvd1)

book1.check_out()
dvd1.check_out()

book1.check_out()

book1.return_item()