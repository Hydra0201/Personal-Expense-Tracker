# Personal Expense Tracker with Data Visualization
What You’ll Build:
A simple app to record daily expenses, categorize them, and visualize your spending habits with charts.

Core Features:
Add expenses with details: amount, category (food, transport, entertainment, etc.), and date

View a list of all expenses

Summarize expenses by category and over time

Display charts showing spending trends (bar charts, pie charts)

Technologies & Libraries:
Python standard libraries (file handling)  

pandas for data handling

matplotlib or seaborn for charts

Data stored in CSV or SQLite database (start with CSV for simplicity)

Step-by-Step Plan:
Step	What to Do	Notes
1	Set up a way to input expense data (amount, category, date)	Use console input to start
2	Store data in a CSV file	Append new entries to file
3	Load data from CSV and display expenses	Show all expenses with filters
4	Summarize expenses by category and date range	Use pandas grouping
5	Plot bar chart for monthly spending per category	Use matplotlib or seaborn
6	Plot pie chart for category-wise spending	Visualize proportion of spend
7	Add extra features (optional)	E.g., edit/delete expenses, GUI interface

What You’ll Learn:
Handling user input and data storage

Reading and writing CSV files

Data manipulation with pandas

Creating basic visualizations

Structuring a simple app with multiple functionalities

## Project structure
expense-tracker/
│
├── main.py                #  Entry point of the app
├── expenses.py            #  Handles adding, reading, and saving expenses
├── analyzer.py            #  Summarizes and analyzes expense data
├── visualizer.py          #  Creates charts (bar, pie)
├── utils.py               #  Helper functions (e.g., input validation)
│
├── data/
│   └── expenses.csv       #  Stores all recorded expense entries
│
├── README.md              #  Project description and usage instructions
└── requirements.txt       #  Python dependencies



