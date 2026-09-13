import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql@7080",
    database="student_placement",
    port=3306
)

cursor = connection.cursor()

query = """
INSERT INTO students
(age, cgpa, attendance, tenth_percentage, twelfth_percentage, backlogs, internship, placement)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

values = (22, 8.5, 85, 55, 59, 2, "Yes", "Yes")

cursor.execute(query, values)
connection.commit()

print("Student data inserted successfully!")

cursor.close()
connection.close()