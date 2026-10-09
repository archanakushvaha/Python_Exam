import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Inventory:

    def __init__(self):
        self.books = None
        self.sales = None
        self.file_path = "inventory.csv"
        self.sales_path = "sales.csv"

    def load_data(self, file_path="inventory.csv"):

        try:
            self.books = pd.read_csv(file_path)
            self.file_path = file_path
            required_columns = ["title", "author", "genre", "price", "quantity"]

            if not all(col in self.books.columns for col in required_columns):
                print("Invalid inventory CSV columns!")
                self.books = None
                return

            self.books["price"] = pd.to_numeric(self.books["price"], errors="coerce")
            self.books["quantity"] = pd.to_numeric(self.books["quantity"], errors="coerce")

            if (
                self.books["title"].isna().any()
                or self.books["author"].isna().any()
                or self.books["genre"].isna().any()
                or self.books["price"].isna().any()
                or self.books["quantity"].isna().any()
                or (self.books["price"] < 0).any()
                or (self.books["quantity"] < 0).any()
                or (self.books["quantity"] % 1 != 0).any()
            ):
                print("Invalid data in inventory CSV!")
                self.books = None
                return

            self.books["quantity"] = self.books["quantity"].astype(int)

            try:
                self.sales = pd.read_csv(self.sales_path)

                self.sales["date"] = pd.to_datetime(self.sales["date"], errors="coerce")
                self.sales["quantity_sold"] = pd.to_numeric(self.sales["quantity_sold"], errors="coerce")
                self.sales["total_revenue"] = pd.to_numeric(self.sales["total_revenue"], errors="coerce")

                if (
                    self.sales["date"].isna().any()
                    or self.sales["quantity_sold"].isna().any()
                    or self.sales["total_revenue"].isna().any()
                    or (self.sales["quantity_sold"] < 0).any()
                    or (self.sales["total_revenue"] < 0).any()
                ):
                    self.sales = None
                    print("Warning: Invalid sales data.")

            except FileNotFoundError:
                self.sales = None
                print("Sales CSV not found. Inventory loaded only.")

            print("Inventory loaded successfully!")

        except FileNotFoundError:
            print("File not found!")

        except (pd.errors.ParserError, UnicodeDecodeError):
            print("Unable to read CSV file!")


    def save_inventory(self):
        self.books.to_csv(self.file_path, index=False)

    def add_book(self):

        if self.books is None:
            print("Please load inventory first!")
            return

        try:
            title = input("Enter book title: ").strip()
            author = input("Enter author: ").strip()
            genre = input("Enter genre: ").strip()

            if not title or not author or not genre:
                print("Title, author and genre cannot be empty!")
                return

            if self.books["title"].str.casefold().eq(title.casefold()).any():
                print("Book already exists!")
                return

            price = float(input("Enter book price: "))
            quantity = int(input("Enter book quantity: "))

            if not np.isfinite(price) or price <= 0:
                print("Price must be positive!")
                return

            if quantity <= 0:
                print("Quantity must be positive!")
                return

            new_book = pd.DataFrame([{
                "title": title,
                "author": author,
                "genre": genre,
                "price": price,
                "quantity": quantity
            }])

            self.books = pd.concat([self.books, new_book], ignore_index=True)
            self.save_inventory()
            print("Book added successfully!")

        except ValueError:
            print("Enter valid numeric values!")



    def display_books(self):

        if self.books is None:
            print("Please load inventory first!")
            return

        if self.books.empty:
            print("No books available!")
        else:
            print(self.books.to_string(index=False))


    def update_book(self):

        if self.books is None:
            print("Please load inventory first!")
            return

        title = input("Enter current book title: ").strip()
        matches = self.books.index[self.books["title"].str.casefold() == title.casefold()].tolist()

        if not matches:
            print("Book not found!")
            return

        try:
            index = matches[0]
            new_title = input("Enter new title: ").strip()
            quantity_input = input("Enter new quantity: ").strip()
            price_input = input("Enter new price: ").strip()

            if new_title:
                duplicate = self.books[self.books["title"].str.casefold()== new_title.casefold()]
                if not duplicate.empty and duplicate.index[0] != index:
                    print("Another book already has this title!")
                    return

            if quantity_input:
                quantity = int(quantity_input)

                if quantity < 0:
                    print("Quantity cannot be negative!")
                    return
            else:
                quantity = int(self.books.at[index, "quantity"])

            if price_input:
                price = float(price_input)

                if not np.isfinite(price) or price <= 0:
                    print("Price must be positive!")
                    return
            else:
                price = float(self.books.at[index, "price"])

            if new_title:
                self.books.at[index, "title"] = new_title

            self.books.at[index, "quantity"] = quantity
            self.books.at[index, "price"] = price
            self.save_inventory()
            print("Book updated successfully!")

        except ValueError:
            print("Enter valid numeric values!")

    def remove_book(self):

        if self.books is None:
            print("Please load inventory first!")
            return

        title = input("Enter book title to remove: ").strip()
        matches = self.books.index[self.books["title"].str.casefold() == title.casefold()].tolist()

        if not matches:
            print("Book not found!")
            return

        self.books = self.books.drop(index=matches[0]).reset_index(drop=True)
        self.save_inventory()
        print("Book removed successfully!")

    def analysis(self):
        if self.books is None:
            print("Please load data first!")
            return
        
        price = self.books["price"].to_numpy()
        qty = self.books["quantity"].to_numpy()

        print("\n--- Inventory Analysis ---")
        print("Total Books:", len(self.books))
        print("Total Copies:", np.sum(qty))
        print("Average Price:", np.mean(price))
        print("Inventory Value:", np.sum(price * qty))

        if self.sales is None or self.sales.empty:
            print("No sales data available!")
            return

        print("Total Sold:", self.sales["quantity_sold"].sum())
        print("Total Revenue:", self.sales["total_revenue"].sum())
        best = self.sales.groupby("title")["quantity_sold"].sum()
        print("Best Selling Book:", best.idxmax())

    def visualization(self):

        if self.books is None:
            print("Please load inventory first!")
            return

        if self.sales is None or self.sales.empty:
            print("Please load valid sales data first!")
            return

        while True:
            print("1. Bar Chart")
            print("2. Line Chart")
            print("3. Pie Chart")
            print("4. Heatmap")
            print("5. Exit")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Enter a valid menu number!")
                continue

            data = self.sales.merge(self.books[["title", "author", "genre", "price"]],on="title",how="inner")

            if choice == 1:
                genre_sales = data.groupby("genre")["quantity_sold"].sum().sort_values(ascending=False)

                genre_sales.plot(kind="bar", figsize=(9, 5))

                plt.title("Total Books Sold by Genre")
                plt.xlabel("Genre")
                plt.ylabel("Quantity Sold")
                plt.xticks(rotation=45, ha="right")
                plt.tight_layout()
                plt.show()

            elif choice == 2:
                data["month"] = data["date"].dt.to_period("M")

                monthly = data.groupby("month")["total_revenue"].sum()
                monthly.index = monthly.index.astype(str)

                plt.figure(figsize=(9, 5))
                plt.plot(
                    monthly.index,
                    monthly.values,
                    marker="o"
                )

                plt.title("Monthly Sales Revenue Trend")
                plt.xlabel("Month")
                plt.ylabel("Total Revenue")
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

            elif choice == 3:
                genre_revenue = data.groupby("genre")["total_revenue"].sum()
                plt.figure(figsize=(8, 8))
                plt.pie(
                    genre_revenue,
                    labels=genre_revenue.index,
                    autopct="%1.1f%%",
                    startangle=90
                )

                plt.title("Revenue Share by Genre")
                plt.tight_layout()
                plt.show()

            elif choice == 4:
                book_sales = self.sales.groupby("title")["quantity_sold"].sum().rename("total_sold")
                correlation_data = self.books[
                    ["title", "price"]
                ].merge(
                    book_sales,
                    left_on="title",
                    right_index=True,
                    how="inner"
                )

                if len(correlation_data) < 2:
                    print("Not enough book data for a heatmap!")
                    continue

                corr = correlation_data[
                    ["price", "total_sold"]
                ].corr()

                plt.figure(figsize=(7, 5))
                sns.heatmap(
                    corr,
                    annot=True,
                    cmap="coolwarm",
                    vmin=-1,
                    vmax=1
                )

                plt.title("Correlation: Book Price vs Sales")
                plt.tight_layout()
                plt.show()

            elif choice == 5:
                print("Exiting visualization menu...")
                break

            else:
                print("Invalid choice!")

book = Inventory()

while True:
    print("1. Load Data")
    print("2. Add Book")
    print("3. Display Books")
    print("4. Update Book")
    print("5. Remove Book")
    print("6. Analysis and Report")
    print("7. Visualization")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        path = input("Enter CSV file: ")
        book.load_data(path)

    elif choice == 2:
        book.add_book()

    elif choice == 3:
        book.display_books()

    elif choice == 4:
        book.update_book()

    elif choice == 5:
        book.remove_book()

    elif choice == 6:
        book.analysis()

    elif choice == 7:
        book.visualization()

    elif choice == 9:
        print("Thank you for using Bookstore Management!")
        break

    else:
        print("Invalid choice. Please try again.")
