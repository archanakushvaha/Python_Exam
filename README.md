# Bookstore Inventory Management and Sales Analysis

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

```text
Bookstore_Project/
│
├── main.py
├── inventory.csv
├── sales.csv
└── README.md
```

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

```csv
title,author,genre,price,quantity
Atomic Habits,James Clear,Self-Help,499,40
Ikigai,Hector Garcia,Self-Help,299,35
The Alchemist,Paulo Coelho,Fiction,250,30
```

### sales.csv

This file stores book sales transactions.

| Column        | Description                 |
| ------------- | --------------------------- |
| date          | Date of the sale            |
| title         | Name of the book sold       |
| quantity_sold | Number of copies sold       |
| total_revenue | Total revenue from the sale |

Example:

```csv
date,title,quantity_sold,total_revenue
2026-01-05,Atomic Habits,5,2495
2026-01-12,The Alchemist,4,1000
```

## Installation

### Step 1: Install Python

Install Python on your computer if it is not already installed.

### Step 2: Install Required Libraries

Open the terminal or command prompt and run:

```bash
pip install numpy pandas matplotlib seaborn
```

### Step 3: Prepare Project Files

Keep `main.py`, `inventory.csv`, and `sales.csv` in the same project folder.

### Step 4: Run the Project

Open the terminal in the project directory and execute:

```bash
python main.py
```

## Main Menu

When the program runs, the following menu is displayed:

```text
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
```

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

```text
Inventory Value = Price × Available Quantity
```

### Sales Revenue

Sales revenue is calculated as:

```text
Sales Revenue = Price × Quantity Sold
```

### Monthly Revenue Growth

```text
Growth Rate = ((Current Month Revenue - Previous Month Revenue)
               / Previous Month Revenue) × 100
```

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
