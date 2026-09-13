import pandas as pd
import mysql.connector

# CSV file load
df = pd.read_csv("data/student_placement.csv")

# MySQL connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql@7080",
    database="student_placement",
    port=3306
)

cursor = connection.cursor()

query = """
INSERT INTO students (
    Student_ID,
    Age,
    Gender,
    Department,
    CGPA,
    Attendance,
    `10th_Percentage`,
    `12th_Percentage`,
    Backlogs,
    Internship,
    Projects,
    Communication_Score,
    Aptitude_Score,
    Placement_Status,
    Package_LPA
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# CSV rows ko MySQL me insert karo
for _, row in df.iterrows():
    values = (
        row["Student_ID"],
        row["Age"],
        row["Gender"],
        row["Department"],
        row["CGPA"],
        row["Attendance"],
        row["10th_Percentage"],
        row["12th_Percentage"],
        row["Backlogs"],
        row["Internship"],
        row["Projects"],
        row["Communication_Score"],
        row["Aptitude_Score"],
        row["Placement_Status"],
        row["Package_LPA"]
    )

    cursor.execute(query, values)

connection.commit()

print(f"✅ {len(df)} students imported successfully!")

cursor.close()
connection.close()