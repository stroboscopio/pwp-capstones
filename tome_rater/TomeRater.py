# 1 - Create a User
class User(object):
# 1.1 - User constructor
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
# 1.2 - get_email method   
    def get_email(self):
        return self.email
# 1.3 - change_email method 
    def change_email(self, address):
        self.email = address
        print("This user's email address has been changed to {}".format(address))
# 1.4 - __repr__ method
    def __repr__(self):
        return "User {}, email: {}, books read: {}".format(self.name, self.email, self.books)
# 1.5 - __eq__ method
    def __eq__(self, other):
         return self.name == other.name and self.email == other.email
# 5.1 - give User the read_book method       
    def read_book(self, book, rating=None):
        self.books.update({book:rating})
# 5.2 - give User the get_average_rating method        
    def get_average_rating(self):
        val = []
        for v in self.books.values():
            if isinstance(v, int):
                val.append(v)
            else:
                continue
        return sum(val)/len(val)
# 2 - Create Book object        
class Book:
# 2.1 - create constructor
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
# 2.2 - create get_title method       
    def get_title(self):
        if isinstance(self.title, str):
            return self.title
# 2.3 - create get_isbn method    
    def get_isbn(self):
        if isinstance(self.isbn, int):
            return self.isbn
# 2.4 - create set_isbn method
    def set_isbn(self, number):
        self.isbn = number
        print("This book's ISBN code has been changed to {}".format(number))
# 2.5 - create add_rating method        
    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating. Please enter a rating between 0 and 4.")
# 2.6 - create __eq__ method           
    def __eq__(self, other):
         return self.title == other.title and self.isbn == other.isbn
    
    def __repr__(self):
        return "{}, isbn: {}".format(self.title, self.isbn)
# 5.3 - give Book the get_average_rating method        
    def get_average_rating(self):
        return sum(self.ratings)/len(self.ratings)
# 5.4 - give Book the __hash__ method    
    def __hash__(self):
        return hash((self.title, self.isbn))
# 3 - Create Fiction subClass                    
class Fiction(Book):
# 3.1 - create constructor
    def __init__(self,title,author,isbn):
        super().__init__(title,isbn)
        self.author = author
# 3.2 - create get_author       
    def get_author(self):
        return self.author
# 3.3 - create __repr__    
    def __repr__(self):
        return "{} by {}".format(self.title, self.author)
# 4 - Create Non_Fiction subClass         
class Non_Fiction(Book):
# 4.1 - create constructor    
    def __init__(self,title,subject, level, isbn):
        super().__init__(title,isbn)
        self.subject = subject
        self.level = level
# 4.2 - create get_subject        
    def get_subject(self):
        return self.subject
# 4.3 - create get_level    
    def get_level(self):
        return self.level
# 4.4 - create __repr__    
    def __repr__(self):
       return "{}, a {} manual on {}".format(self.title, self.level, self.subject)
# 6 - create TomeRater    
class TomeRater(object):
# 6.1 - create constructor
    def __init__(self):
        self.users = {}
        self.books = {}
    
# 6.2 - create create_book        
    def create_book(self, title, isbn):
        return Book(title, isbn)
# 6.3 - create create_novel            
    def create_novel(self, title, subject, isbn):
        return Fiction(title, subject, isbn)
# 6.4 - create create_non_fiction    
    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book,rating)
            if rating is not None:
                book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("User {email} not found".format(email=email))

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for k in self.books.keys():
            print(k)
            
    def print_users(self):
        for v in self.users.values():
            print(v)
    
    def most_read_book(self):
        most_read = ""
        n_read = 0
        for k,v in self.books.items():
            if v > n_read:
                n_read = v
                most_read = k
        return most_read
    
    def highest_rated_book(self):
        highest_rated = ""
        highest_avg = 0
        for v in self.books:
            val = v.get_average_rating()
            if val > highest_avg:
                highest_avg = val
                highest_rated = v.title
        return highest_rated
        
    def most_positive_user(self):
        most_positive = ""
        highest_avg = 0
        for v in self.users.values():
            avg_rating = v.get_average_rating()
            if avg_rating > highest_avg:
                highest_avg = avg_rating
                most_positive = [k for k, val in self.users.items() if val == v]
        return most_positive
    
    def get_n_most_read_books(self, n):
        return sorted(self.books, key=self.books.get, reverse=True)[0:n]
    
    def get_n_most_prolific_readers(self, n):
        s = {}
        for k,v in self.users.items():
            s.update({k:len(v.books)})
        print(s)
        return sorted(s, key=s.get, reverse=True)[0:n]