def reverse_integer(number):
    reversed_num = 0
    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10
    return reversed_num

num = int(input("Enter an integer: "))

reversed_num = reverse_integer(num)
print(f"The reversed integer is: {reversed_num}")

######

import mysql.connector

db_config = {
    "host": "localhost",
    "user": "your_username",
    "password": "your_password",
    "database": "your_database"
}

connection = mysql.connector.connect(**db_config)

cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    department VARCHAR(255)
)
"""
cursor.execute(create_table_query)

insert_query = """
INSERT INTO people (name, gender) VALUES (%s, %s)
"""
data_to_insert = [
    ("John Doe", "Male"),
    ("Jane Smith", "Female"),
    ("Alice Johnson", "Female")
]
cursor.executemany(insert_query, data_to_insert)
connection.commit()

# Fetching and displaying data from the table
select_query = "SELECT * FROM people"
cursor.execute(select_query)
result = cursor.fetchall()

print("Fetched data:")
for row in result:
    print(f"ID: {row[0]}, Name: {row[1]}, Department: {row[2]}")

# Closing the cursor and connection
cursor.close()
connection.close()