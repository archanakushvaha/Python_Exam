import os 
import numpy as np
import pandas as np
import matplotlib.pyplot as plt
import seaborn as sns

class Inventory():
    
    def __init__(self):
            self.books = None
            
    def load_data(self,file_path):
            
        try:
            self.books = pd.read_csv(file_path)
            print("load data sucssesfully!")
            return
        except FileNotFoundError:
            print("File not found...")
   
    def __init__(self,title,author,price,quantity):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity
        
    def add_book(self):
        book = {
            "ID" = int(input("Enter Book Id:")),
            "author" = int(input("Enter Book Author:")),
            "price" = int(input("Enter Book Price:")),
            "quantity" = int(input("Enter Book Quantity:"))
        }   
        
        self.books.append(book)
        print("Book add successfully..")
        
    def display_books(self):
        if not self.books:
            print("No Books Availabel..")
            
        else:
            for book in self.books:
                print(book)
                
    def search_book(self):
        book_id =  int(input("Enter book id:"))
        for book in self.books:
            if book["ID"] == book_id:
                print(book)
                return
            
        print("Book not found")
        
    def Update_book(self):
        book_id = int(input("Enter Book id:"))
        for book in self.books:
            if book["ID"] == book_id:
                book["rice"] = int(input("Enter Price:"))
                book["quantity"] = int(input("Enter Quantity:"))
                print("Book Updated Successfully!")
                return
    
    def remove_book(self):
        book_id = int(input("Enter Book ID:"))
        for book in self.books:
            if book["ID"] == book_id:
                self.books.remove(book)
                print("Book deleted!")
                return
            
        print("Book not Found!")
        
    def analysis(self):
        if self.books is None:
            print("Please Load data first..")
            return
        
        price = self.books["Price"].to_numpy(dtype=float)
        quantity= self.books["Quantity"].to_numpy(dtype=int) 
        
        print("Total Book Titles:", len(self.books))
        print("Total Book Copies:", np.sum(quantity))
        print("Average Price:", np.mean(price))
        print("Total Inventory Value:", np.sum(price*quantity))
        
    def visualization(self):
        if self.books is None:
            print("Please Load data first..")
            return
        
        while True:
            
            print("1. Bar Chart")
            print("2. Line Chart")
            print("3. Pie Chart")
            print("4. Heatap")
            print("5. Exit")
            
            choice = int(input("Enter Your Choice:"))
            
            if choice == 1:
                
                plt.figure(figsize=(8,5))
                plt.bar(self.books[
                    "Total sales",
                    "author"
                ])
                plt.title("Total Sales by genre or author")
                plt.xlabel("Total sales")
                plt.ylabel("Author")
                plt.show
                
            elif choice == 2:
                plt.figure(figsize=(8,5))
                plt.plot(self.books[
                    "Total Sales",
                    "monthly"
                    maker="o"
                ])
                plt.title("Monthy Trade sales")
                plt.xlabel("Total sales")
                plt.ylabel("monthy")
                plt.show
                
            elif choice == 3:
                plt.figure(figsize=(8,5))
                plt.pie(self.books[
                    revenue.index
                    autopct="%1.1f%%"
                ])
                plt.title("Revenue share by book")
                plt.show
                
            elif choice == 4:
                plt.figure(figsize=(8,5))
                plt.heatmap(self.books[
                    "Total sales",
                    "author"
                ])
                plt.titel("Correlation beetween Book price and sales volums")
                plt.xlabel("Total sales")
                plt.ylabel("Author")
                plt.show
                
            elif choice == 5:
                print("Thank You")
                break
            else:
                print("Invaild Choice.")
                 
book = Inventory()

while True:
    print("1. load_data")
    print("2. add_book")
    print("3. display_books")
    print("4. search_book")
    print("5. Update_book")
    print("6. remove_book")
    print("7. analysis")
    print("8. visualization")
    print("9. Exit")
    
    choice = int(input("Enter Your Choice:"))
    
    if choice == 1:
        book.load_data(input("Enter CSV file_path:"))
        
    elif choice == 2:
        book.add_book()
        
    elif choice == 3:
        book.display_books()
        
    elif choice == 4:
        book.search_book()
        
    elif choice == 5:
        book.Update_book()
        
    elif choice == 6:
        book.remove_book()
        
    elif choice == 7:
        book.analysis()
        
    elif choice == 8:
        book.visualization()
        
    elif choice == 9:
        print("Thank You!")
        break
    
    else:
        ("Invaild Choice. Please Enter Correct Choice...")
        
    
        
                   
            
            
    
        
        
        
        
        
    