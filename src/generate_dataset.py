import pandas as pd
import numpy as np

# Reproducible results
np.random.seed(42)

# Number of students
n = 5000

# Generate student data
data = {
    "Student_ID": range(1001, 1001 + n),

    "Age": np.random.randint(20, 25, n),

    "Gender": np.random.choice(
        ["Male", "Female"],
        n,
        p=[0.55, 0.45]
    ),

    "Department": np.random.choice(
        ["CSE", "IT", "ECE", "EEE", "ME", "CE"],
        n
    ),

    "CGPA": np.round(
        np.random.uniform(5.0, 10.0, n), 2
    ),

    "Attendance": np.round(
        np.random.uniform(50, 100, n), 2
    ),

    "10th_Percentage": np.round(
        np.random.uniform(50, 100, n), 2
    ),

    "12th_Percentage": np.round(
        np.random.uniform(50, 100, n), 2
    ),

    "Backlogs": np.random.randint(0, 5, n),

    "Internship": np.random.choice(
        ["Yes", "No"],
        n,
        p=[0.45, 0.55]
    ),

    "Projects": np.random.randint(0, 6, n),

    "Communication_Score": np.random.randint(40, 101, n),

    "Aptitude_Score": np.random.randint(40, 101, n)
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate placement probability
score = (
    df["CGPA"] * 8
    + df["Attendance"] * 0.20
    + df["10th_Percentage"] * 0.15
    + df["12th_Percentage"] * 0.15
    + df["Projects"] * 4
    + df["Communication_Score"] * 0.10
    + df["Aptitude_Score"] * 0.15
    + (df["Internship"] == "Yes") * 8
    - df["Backlogs"] * 5
)

# Convert score into placement status
threshold = score.median()

df["Placement_Status"] = np.where(
    score >= threshold,
    "Placed",
    "Not Placed"
)

# Generate package only for placed students
df["Package_LPA"] = np.where(
    df["Placement_Status"] == "Placed",
    np.round(np.random.uniform(3, 15, n), 2),
    0
)

# Create data folder
import os
os.makedirs("data", exist_ok=True)

# Save CSV
df.to_csv("data/student_placement.csv", index=False)

# Save Excel
df.to_excel("data/student_placement.xlsx", index=False)
print("Dataset created successfully!")
print("Total Students:", len(df))
print("\nFirst 5 rows:")
print(df.head())

print("\nPlacement Summary:")
print(df["Placement_Status"].value_counts())