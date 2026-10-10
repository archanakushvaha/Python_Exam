📚 Bookstore Management System
A Python-based Bookstore Management System that helps manage book inventory, update book details, analyze sales, generate CSV reports, and visualize bookstore performance. The project uses Object-Oriented Programming (OOP), abstract classes, NumPy, Pandas, Matplotlib, and Seaborn.
📌 Table of Contents
- Introduction
- Project Objectives
- Features
- Technologies Used
- Project Structure
- CSV File Requirements
- Installation and Setup
- How to Run
- Main Menu
- Reports and Analysis
- Data Visualizations
- OOP Concepts Used
- Validation and Error Handling
- Future Improvements
- Learning Outcomes
- Contact Me
📖 Introduction
The Bookstore Management System is a menu-driven Python project designed to make common bookstore operations easier. It allows users to load book and sales data from CSV files, add new books, view available inventory, update prices and quantities, and delete book records.
The project also provides inventory and sales summaries, exports reports to CSV files, and creates charts to help users understand sales trends. It demonstrates how Python programming and data analysis libraries can be combined in a practical application.
🎯 Project Objectives
- Manage book inventory in a structured way.
- Add, display, update, and delete book records.
- Read and validate data stored in CSV files.
- Calculate inventory totals and sales performance.
- Identify the best-selling book.
- Save inventory and sales reports as CSV files.
- Visualize sales information using different charts.
- Practice OOP concepts, including abstraction and encapsulation.
- Use NumPy and Pandas for calculations and data manipulation.
✨ Features
1. Load Data
- Loads book details from inventory.csv.
- Loads sales information from sales.csv when available.
- Checks for required columns and invalid values.
- Allows inventory data to be loaded even if the sales file is missing.
2. Add a Book
- Accepts a book title, author, genre, price, and quantity.
- Checks that required text fields are not empty.
- Prevents adding a title that already exists, ignoring letter case.
- Validates numeric values before saving.
- Updates the inventory CSV file after a successful addition.
3. Display Books
- Displays all loaded book records in a readable table.
- Shows a message if the data has not been loaded or no books are available.
4. Update a Book
- Finds a book by its title.
- Allows the user to change the price, quantity, or both.
- Pressing Enter for a field keeps its current value.
- Saves successful changes to the inventory file.
5. Delete a Book
- Searches for a book by title.
- Removes the matching record from the inventory.
- Saves the updated inventory to the CSV file.
6. Analysis and Reports
- Calculates the total number of book titles.
- Calculates the total number of copies in stock.
- Calculates the average book price and total inventory value.
- Calculates the total number of books sold and total revenue.
- Finds the best-selling book by quantity sold.
7. Generate CSV Reports
- Saves inventory data to inventory_report.csv.
- Summarizes sales by book title and saves it to sales_report.csv when sales data is available.
8. Visualization
The visualization menu offers four chart options:
- Bar chart: Total books sold by genre.
- Line chart: Monthly sales revenue.
- Pie chart: Revenue distribution by genre.
- Heatmap: Correlation between book price and total quantity sold.
🛠️ Technologies Used
Technology	Purpose
Python	Main programming language
NumPy	Numerical calculations and array operations
Pandas	Loading, validating, grouping, and saving tabular data
Matplotlib	Creating charts and visualizations
Seaborn	Creating the correlation heatmap
CSV	Storing inventory, sales, and exported reports
OOP	Organizing the application using classes and methods


📂 Project Structure
Bookstore-Management-System/
├── main.py                  # Main application code (use your actual Python filename)
├── inventory.csv            # Book inventory data
├── sales.csv                # Sales transaction data
├── inventory_report.csv     # Generated inventory report
├── sales_report.csv         # Generated sales summary
└── README.md                # Project documentation
The report CSV files are created when the corresponding report option is used. If your Python file has a different name, replace main.py in this structure with that filename.
🗃️ CSV File Requirements
inventory.csv
The inventory file must contain these columns:
Column	Description
title	Book title
author	Author's name
genre	Book category or genre
price	Price of one book
quantity	Number of copies in stock


Example format:
title,author,genre,price,quantity
The Silent Patient,Alex Michaelides,Thriller,350,12
Wings of Fire,A. P. J. Abdul Kalam,Autobiography,250,20
The Alchemist,Paulo Coelho,Fiction,300,15
sales.csv
The sales file must contain these columns:
Column	Description
date	Date of the sale
title	Title of the book sold; should match an inventory title for charting
quantity_sold	Number of copies sold
total_revenue	Total revenue for that sales record


Example format:
date,title,quantity_sold,total_revenue
2026-01-05,The Silent Patient,2,700
2026-01-12,Wings of Fire,3,750
2026-02-02,The Alchemist,1,300
Use valid dates and non-negative numeric values. The program validates the required columns and several data-quality conditions when loading these files.
⚙️ Installation and Setup
Step 1: Install Python
Install a recent version of Python from the official website: https://www.python.org/downloads/
Step 2: Open the Project Folder
Open the folder containing your Python script and CSV files in VS Code or another Python editor.
Step 3: Install Required Libraries
Open the terminal and run:
pip install numpy pandas matplotlib seaborn
Step 4: Prepare the CSV Files
Place inventory.csv and sales.csv in the same working directory as the program. Make sure the column names match the requirements above.
▶️ How to Run
1. Open the project folder in VS Code.
2. Open the Python file containing the Bookstore Management System code.
3. Open the terminal in that folder.
4. Run the script, for example:
python main.py
5. Select an option from the menu by entering its number.
6. Choose Load Data first before performing inventory operations or reports.
7. Follow the prompts shown in the terminal.
8. Choose Exit when you finish.
If your script has a different filename, use that filename in the run command.
📋 Main Menu
Option	Operation
1	Load Data
2	Add Book
3	Display Books
4	Update Book
5	Delete Book
6	Analysis and Report
7	Generate CSV Report
8	Visualization
9	Exit


📊 Reports and Analysis
Inventory Report
The inventory report displays:
- Total Book Titles: Number of book records in the inventory.
- Total Copies: Sum of the quantities available.
- Average Price: Average price of the books in the inventory.
- Inventory Value: Sum of each book's price multiplied by its quantity.
Sales Report
The sales report displays:
- Total Books Sold: Sum of quantity_sold.
- Total Revenue: Sum of total_revenue.
- Best-Selling Book: Book title with the highest total quantity sold.
Exported Reports
- inventory_report.csv contains the inventory records.
- sales_report.csv contains sales totals grouped by book title, including quantity sold and revenue.
📈 Data Visualizations
Bar Chart — Books Sold by Genre
Groups sales by genre and compares the number of books sold in each genre.
Line Chart — Monthly Sales Revenue
Groups sales by month to display how revenue changes over time.
Pie Chart — Revenue by Genre
Shows each genre's share of the total revenue in the loaded sales data.
Heatmap — Book Price and Sales Correlation
Displays the correlation between book price and total quantity sold for titles that match between inventory and sales. A correlation shows an association in the data; it does not prove that one variable causes the other.
🧠 OOP Concepts Used
1. Abstraction
The abstract Report class defines the generate() method using @abstractmethod. Report classes implement this method with their own behavior.
2. Inheritance
InventoryReport and SalesReport inherit from the Report abstract class.
3. Encapsulation
The Bookstore class uses __books and __sales as private attributes to keep its data managed inside the class.
4. Polymorphism
Both report classes provide their own implementation of generate(). The program can call this method on different report objects through a common interface.
5. Classes and Objects
Bookstore, InventoryReport, and SalesReport organize related data and functionality into reusable classes. Objects of these classes are used to perform the application's operations.
🛡️ Validation and Error Handling
The program includes checks for several common issues:
- Missing CSV files.
- Missing required columns.
- CSV parsing or text-encoding errors for the inventory file.
- Empty required book fields.
- Duplicate book titles when adding a book.
- Invalid numeric input.
- Negative inventory or sales values when loading data.
- Missing or unavailable sales data for reports and charts.
- Book titles in sales data that do not match inventory titles for visualization.
For reliable results, use the required column names and keep the CSV data consistent. Always keep a backup of important CSV files before making changes.
🚀 Future Improvements
- Add a graphical user interface (GUI).
- Add customer details and billing functionality.
- Add book search by title, author, or genre.
- Track stock changes and low-inventory alerts.
- Add login and user-role management.
- Create more detailed monthly and yearly reports.
- Add automated tests for important operations.
- Improve report formatting and provide export options beyond CSV.
These are possible future enhancements and are not features currently implemented in the project.
🎓 Learning Outcomes
Through this project, I practiced:
- Building a menu-driven Python application.
- Using classes, objects, abstraction, inheritance, encapsulation, and polymorphism.
- Reading and writing CSV files with Pandas.
- Validating and cleaning tabular data.
- Performing numerical calculations with NumPy.
- Grouping and summarizing data with Pandas.
- Creating bar, line, pie, and heatmap visualizations.
- Handling common file and input errors.

Feel free to explore the project and share suggestions for improvement.# Bookstore Inventory Management and Sales Analysis

## Project Overview
The Bookstore Inventory Management and Sales Analysis project is a Python-based application designed to manage bookstore inventory and analyze sales data. It allows users to add, display, search, update, and remove books. It also records sales, calculates revenue, generates reports, and visualizes sales trends using charts.

This project uses Object-Oriented Programming (OOP), NumPy, Pandas, Matplotlib, and Seaborn to manage data and perform analysis.

## Features

### 1. Inventory Management
* Load inventory data from a CSV file.
* Add new books to the inventory.
* Display all available books.
* Search books by title.
* Update book title, price, and quantity.
* Remove books from the inventory.
* Save inventory changes automatically to the CSV file.

### 2. Input Validation
* Validate book titles and author names.
* Prevent empty book details.
* Ensure book prices are positive.
* Validate book quantities.
* Prevent selling more books than available in stock.
* Handle invalid inputs and missing files.

### 3. Sales Management
* Record book sales.
* Calculate total revenue for each sale.
* Automatically update available inventory.
* Save sales records to a CSV file.

### 4. Data Analysis Using NumPy
* Calculate total book copies.
* Calculate average book price.
* Calculate total inventory value.
* Calculate total copies sold.
* Calculate total sales revenue.
* Calculate monthly revenue growth rate.

### 5. Data Management Using Pandas
* Load and manage CSV files.
* Update inventory records.
* Analyze sales by book title.
* Identify the best-selling book.
* Identify the highest-revenue book.
* Analyze monthly sales trends.

### 6. Data Visualization
* **Bar Chart:** Total books sold by genre.
* **Line Chart:** Monthly sales revenue trends.
* **Pie Chart:** Revenue share by book genre.
* **Heatmap:** Correlation between book price and sales quantity.

## Technologies Used
* Python
* Object-Oriented Programming (OOP)
* NumPy
* Pandas
* Matplotlib
* Seaborn
* CSV File Handling
* Exception Handling
* Control Structures

## Project Structure
Bookstore_Project/
│
├── main.py
├── inventory.csv
├── sales.csv
└── README.md

## CSV File Structure

### inventory.csv
This file stores the book inventory details.

| Column   | Description          |
| -------- | -------------------- |
| title    | Name of the book     |
| author   | Name of the author   |
| genre    | Category of the book |
| price    | Price of the book    |
| quantity | Available copies     |

Example:
title,author,genre,price,quantity
Atomic Habits,James Clear,Self-Help,499,40
Ikigai,Hector Garcia,Self-Help,299,35
The Alchemist,Paulo Coelho,Fiction,250,30

### sales.csv
This file stores book sales transactions.

| Column        | Description                 |
| ------------- | --------------------------- |
| date          | Date of the sale            |
| title         | Name of the book sold       |
| quantity_sold | Number of copies sold       |
| total_revenue | Total revenue from the sale |

Example:
date,title,quantity_sold,total_revenue
2026-01-05,Atomic Habits,5,2495
2026-01-12,The Alchemist,4,1000


## Installation

### Step 1: Install Python
Install Python on your computer if it is not already installed.

### Step 2: Install Required Libraries
Open the terminal or command prompt and run:
pip install numpy pandas matplotlib seaborn


### Step 3: Prepare Project Files
Keep `main.py`, `inventory.csv`, and `sales.csv` in the same project folder.

### Step 4: Run the Project
Open the terminal in the project directory and execute
python main.py


## Main Menu
When the program runs, the following menu is displayed:
========== BOOKSTORE MANAGEMENT ==========

1. Load Data
2. Add Book
3. Display Books
4. Search Book
5. Update Book
6. Remove Book
7. Record Sales
8. Analysis and Report
9. Visualization
10. Exit

Enter the corresponding option number to perform an operation.

## Analysis and Reports
The application provides the following metrics:
* Total number of book titles.
* Total available book copies.
* Average book price.
* Total inventory value.
* Total copies sold.
* Total sales revenue.
* Best-selling book.
* Highest-revenue book.
* Monthly revenue growth percentage.

### Inventory Value
Inventory value is calculated as:
Inventory Value = Price × Available Quantity

### Sales Revenue
Sales revenue is calculated as:
Sales Revenue = Price × Quantity Sold


### Monthly Revenue Growth
Growth Rate = ((Current Month Revenue - Previous Month Revenue)/ Previous Month Revenue) × 100

## Learning Outcomes
Through this project, users can learn:
* Python classes, objects, and methods.
* Constructors and instance variables.
* Conditional statements and loops.
* Input validation and exception handling.
* CSV file handling with Pandas.
* Numerical calculations using NumPy.
* Data aggregation and analysis.
* Data visualization using Matplotlib and Seaborn.
* Inventory and sales management concepts.

## Conclusion
The Bookstore Inventory Management and Sales Analysis project provides a practical way to manage bookstore inventory, record sales transactions, calculate important business metrics, and visualize sales performance. It demonstrates how Python and data analysis libraries can be combined to build a useful data-driven application.
