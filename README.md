# Python Generators - SQL Streaming Project

## Project Overview

This project demonstrates how to use **Python generators** to stream rows from a **MySQL database** efficiently.  
It sets up a database, creates a table, inserts data from a CSV file, and allows you to fetch rows one by one using a generator.

---

## Project Structure

python-generators-0x00/
│
├── seed.py # Script to create database, table, and insert CSV data
├── 0-main.py # Script to test database setup and data insertion
├── 1-main.py # Script to test streaming rows with a generator
├── user_data.csv # Sample CSV file with user data
└── README.md # Project documentation

---

## Requirements

- Python 3.x  
- MySQL Server 8.x  
- Python package: `mysql-connector-python`

Install the MySQL connector with:

```bash
pip install mysql-connector-python
Usage
Step 1: Seed the database

Run the main script to create the database, table, and insert CSV data:

python 0-main.py


Expected output:

Connection to MySQL server successful
Database ALX_prodev created or already exists
connection successful
Connected to ALX_prodev database
Table user_data created successfully
Data inserted successfully
Database ALX_prodev is present
[('uuid1', 'Jane Smith', 'janesmith@gmail.com', 28), ...]

Step 2: Stream data with the generator

Run the generator script:

python 1-main.py


Expected output:

Connected successfully!
('uuid1', 'Jane Smith', 'janesmith@gmail.com', Decimal('28'))
('uuid2', 'Bob Williams', 'bob.williams@gmail.com', Decimal('51'))
...


Each row is fetched one by one, demonstrating memory-efficient streaming.

CSV Format

Your user_data.csv file should look like:

name,email,age
John Doe,johndoe@example.com,35
Jane Smith,janesmith@gmail.com,28
...


name → VARCHAR

email → VARCHAR

age → DECIMAL

Notes

The generator function stream_user_data(connection) fetches rows one at a time using yield.

UUIDs are generated for each user as the user_id primary key.

This setup ensures efficient memory usage even with large datasets.

Author

Your Meron Bihon/ ALX Backend Python Project