# DataFrame Basics in Python
This module provides a foundational understanding of DataFrames, a core data structure in the pandas library, essential for data manipulation and analysis in Python.

# What is a DataFrame?
A DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns). Think of it as:
1. A spreadsheet (like Excel)
1. A SQL table
1. A dictionary of Series objects

It's the most commonly used pandas object, and it allows you to store and manipulate data in a structured way.

# Key Characteristics of DataFrames
1. Labeled Axes: Both rows and columns have labels (indices for rows, column names for columns). This makes data access intuitive.
1.Heterogeneous Data: Columns can have different data types (e.g., one column can be integers, another strings, and another booleans).
1. Size Mutable: You can add or remove columns and rows.
1. Value Mutable: Data within the DataFrame can be changed.

# Creating DataFrames
DataFrames can be created in various ways, most commonly from:
1. Dictionaries of lists or Series
1. Lists of dictionaries
1. NumPy arrays
1. CSV or other external files

Let's look at some examples of how to create DataFrames.
