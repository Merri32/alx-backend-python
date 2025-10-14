#!/usr/bin/python3
import seed

# Connect to the ALX_prodev database
connection = seed.connect_to_prodev()

if connection:
    print("Connected successfully!")
    for row in seed.stream_user_data(connection):
        print(row)
    connection.close()
