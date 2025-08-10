# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor: Initializes the book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Prints message when object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation: Human-readable format."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation: Code to recreate the instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

