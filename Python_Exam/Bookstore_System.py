# Project : Bookstore Management System

from abc import ABC, abstractmethod
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Report(ABC):
    @abstractmethod
    def generate(self, books, sales):
        pass

class InventoryReport(Report):
    def generate(self, books, sales):

        if books is None or books.empty:
            print("No book data available.")
            return

        prices = books["price"].to_numpy()
        quantities = books["quantity"].to_numpy()
        print("Total Book Titles:", len(books))
        print("Total Copies:", np.sum(quantities))
        print("Average Price:", round(np.mean(prices), 2))
        print("Inventory Value:", round(np.sum(prices * quantities), 2))


class SalesReport(Report):

    def generate(self, books, sales):
        if sales is None or sales.empty:
            print("\nNo sales data available.")
            return

        print("Total Books Sold:",int(sales["quantity_sold"].sum()))
        print("Total Revenue:",round(float(sales["total_revenue"].sum()), 2))
        best = sales.groupby("title")["quantity_sold"].sum()
        if not best.empty:
            print("Best-Selling Book:", best.idxmax())

class Bookstore:

    def __init__(self):
        self.__books = None
        self.__sales = None

        self.inventory_file = "inventory.csv"
        self.sales_file = "sales.csv"

    def load_data(self):

        try:
            books = pd.read_csv(self.inventory_file)
            required = ["title", "author", "genre", "price", "quantity"]

            if not all(col in books.columns for col in required):
                print("Invalid inventory CSV columns!")
                return

            books["price"] = pd.to_numeric(books["price"], errors="coerce")
            books["quantity"] = pd.to_numeric(books["quantity"], errors="coerce")

            if (
                books[required].isna().any().any()
                or (books[["price", "quantity"]] < 0).any().any()
                or (books["quantity"] % 1 != 0).any()
            ):
                print("Invalid data in inventory.csv!")
                return

            books["quantity"] = books["quantity"].astype(int)
            self.__books = books

        except FileNotFoundError:
            print("inventory.csv not found!")
            return

        except (pd.errors.ParserError, UnicodeDecodeError):
            print("Unable to read inventory.csv!")
            return

        try:
            sales = pd.read_csv(self.sales_file)
            required_sales = ["date", "title", "quantity_sold", "total_revenue"]

            if not all(col in sales.columns for col in required_sales):
                print("Invalid sales CSV columns. Sales report unavailable.")

                self.__sales = pd.DataFrame(columns=required_sales)
                self.__sales["date"] = pd.to_datetime(self.__sales["date"])

            else:
                sales["date"] = pd.to_datetime(sales["date"], errors="coerce")
                for col in ["quantity_sold", "total_revenue"]:
                    sales[col] = pd.to_numeric(
                        sales[col], errors="coerce"
                    )

                if (
                    sales[required_sales].isna().any().any()or (sales[["quantity_sold", "total_revenue"]] < 0).any().any()
                    or (sales["quantity_sold"] % 1 != 0).any()
                ):
                    print("Invalid sales data. Sales report unavailable.")
                    self.__sales = pd.DataFrame(columns=required_sales)
                    self.__sales["date"] = pd.to_datetime(self.__sales["date"])

                else:
                    self.__sales = sales

        except FileNotFoundError:
            self.__sales = pd.DataFrame(columns=["date", "title","quantity_sold", "total_revenue"])
            self.__sales["date"] = pd.to_datetime(self.__sales["date"])
            print("sales.csv not found. Inventory loaded only.")
        print("Bookstore data loaded successfully!")

    def save_inventory(self):
        self.__books.to_csv(self.inventory_file)

    def add_book(self):

        if self.__books is None:
            print("Please load data first!")
            return

        try:
            title = input("Enter book title: ").strip()
            author = input("Enter author: ").strip()
            genre = input("Enter genre: ").strip()

            if not title or not author or not genre:
                print("Title, author and genre cannot be empty!")
                return

            if self.__books["title"].str.casefold().eq(title.casefold()).any():
                print("Book already exists!")
                return

            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))

            if not np.isfinite(price) or price <= 0 or quantity < 0:
                print("Price must be positive and quantity cannot be negative!")
                return

            new_book = pd.DataFrame([{"title": title,"author": author,"genre": genre,"price": price,"quantity": quantity}])
            self.__books = pd.concat([self.__books, new_book],ignore_index=True)
            self.save_inventory()
            print("Book added successfully!")

        except ValueError:
            print("Enter valid numeric values!")

    def display_books(self):

        if self.__books is None:
            print("Please load data first!")
        elif self.__books.empty:
            print("No books found.")
        else:
            print(self.__books.to_string(index=False))

    def update_book(self):

        if self.__books is None:
            print("Please load data first!")
            return

        title = input("Enter book title to update: ").strip()
        rows = self.__books.index[self.__books["title"].str.casefold()== title.casefold()]
        if len(rows) == 0:
            print("Book not found.")
            return
        try:
            i = rows[0]
            price_text = input("New price (Enter to keep current): ").strip()
            qty_text = input("New quantity (Enter to keep current): ").strip()
            if price_text:
                price = float(price_text)
                if not np.isfinite(price) or price <= 0:
                    print("Price must be positive!")
                    return

                self.__books.at[i, "price"] = price

            if qty_text:
                qty = int(qty_text)
                if qty < 0:
                    print("Quantity cannot be negative!")
                    return
                self.__books.at[i, "quantity"] = qty

            self.save_inventory()
            print("Book updated successfully!")
        except ValueError:
            print("Enter valid numeric values!")

    def delete_book(self):

        if self.__books is None:
            print("Please load data first!")
            return

        title = input("Enter book title to delete: ").strip()
        rows = self.__books.index[self.__books["title"].str.casefold()== title.casefold()]
        if len(rows) == 0:
            print("Book not found.")
            return

        self.__books = self.__books.drop(index=rows[0]).reset_index(drop=True)
        self.save_inventory()
        print("Book deleted successfully!")

    def analysis(self):

        if self.__books is None:
            print("Please load data first!")
            return

        reports = [InventoryReport(),SalesReport()]
        for report in reports:
            report.generate(self.__books,self.__sales)

    def generate_report(self):

        if self.__books is None:
            print("Please load data first!")
            return

        print("\n1. Save Inventory Report")
        print("2. Save Sales Report")

        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                self.__books.to_csv("inventory_report.csv",)
                print("Inventory report saved to inventory_report.csv")

            elif choice == 2:
                if self.__sales is None or self.__sales.empty:
                    print("No sales data available!")
                    return

                report = self.__sales.groupby("title").agg(quantity_sold=("quantity_sold", "sum"),total_revenue=("total_revenue", "sum"))
                report.to_csv("sales_report.csv",index=False)
                print("Sales report saved to sales_report.csv")

            else:
                print("Invalid choice!")

        except ValueError:
            print("Enter a valid menu number!")

    def visualization(self):

        if self.__books is None:
            print("Please load data first!")
            return

        if self.__sales is None or self.__sales.empty:
            print("No sales data available for charts!")
            return

        data = self.__sales.merge(self.__books[["title", "genre", "price"]],on="title",how="inner")
        if data.empty:
            print("Sales titles do not match inventory titles!")
            return

        while True:
            print("1. Bar Chart")
            print("2. Line Chart")
            print("3. Pie Chart")
            print("4. Heatmap")
            print("5. Back")

            try:
                choice = int(input("Enter choice: "))
            except ValueError:
                print("Enter a valid number!")
                continue

            if choice == 1:
                chart = data.groupby("genre")["quantity_sold"].sum()
                chart.plot(
                    kind="bar",
                    figsize=(8, 5)
                )
                plt.title("Books Sold by Genre")
                plt.xlabel("Genre")
                plt.ylabel("Books Sold")

            elif choice == 2:
                monthly = data.assign(month=data["date"].dt.to_period("M").astype(str)).groupby("month")["total_revenue"].sum()
                plt.figure(figsize=(8, 5))
                plt.plot(
                    monthly.index,
                    monthly.values,
                    marker="o"
                )
                plt.title("Monthly Sales Revenue")
                plt.xlabel("Month")
                plt.ylabel("Revenue")
                plt.xticks(rotation=30)

            elif choice == 3:
                chart = data.groupby("genre")["total_revenue"].sum()
                if chart.sum() <= 0:
                    print("No revenue available for pie chart.")
                    continue
                plt.figure(figsize=(7, 7))
                plt.pie(
                    chart,
                    labels=chart.index,
                    autopct="%1.1f%%"
                )
                plt.title("Revenue by Genre")

            elif choice == 4:
                sold = self.__sales.groupby("title")["quantity_sold"].sum().rename("total_sold")
                corr_data = self.__books[
                    ["title", "price"]
                ].merge(
                    sold,
                    left_on="title",
                    right_index=True,
                    how="inner"
                )
                if (len(corr_data) < 2 or corr_data[["price", "total_sold"]].nunique().min() < 2):
                    print("Not enough varied data for heatmap.")
                    continue

                plt.figure(figsize=(6, 4))
                sns.heatmap(
                    corr_data[
                        ["price", "total_sold"]
                    ].corr(),
                    annot=True,
                    cmap="coolwarm",
                    vmin=-1,
                    vmax=1
                )
                plt.title("Book Price and Sales Correlation")

            elif choice == 5:
                break
            else:
                print("Invalid choice!")
                continue
            plt.tight_layout()
            plt.show()

bookstore = Bookstore()
while True:
    print("1. Load Data")
    print("2. Add Book")
    print("3. Display Books")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Analysis and Report")
    print("7. Generate CSV Report")
    print("8. Visualization")
    print("9. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number from 1 to 11.")
        continue

    if choice == 1:
        bookstore.load_data()

    elif choice == 2:
        bookstore.add_book()

    elif choice == 3:
        bookstore.display_books()

    elif choice == 4:
        bookstore.update_book()

    elif choice == 5:
        bookstore.delete_book()

    elif choice == 6:
        bookstore.analysis()

    elif choice == 7:
        bookstore.generate_report()

    elif choice == 8:
        bookstore.visualization()

    elif choice == 9:
        print("Thank you for using Bookstore Management System!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 9.")
