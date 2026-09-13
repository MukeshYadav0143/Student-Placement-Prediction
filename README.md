# 🎓 Student Placement Prediction

An end-to-end **Machine Learning web application** that predicts student placement outcomes based on academic performance, attendance, internships, projects, backlogs, and other relevant factors.

## 🚀 Project Overview

**Student Placement Prediction** is a Machine Learning project designed to predict whether a student is likely to be placed based on important academic and career-related features.

The project combines:

* 🤖 Machine Learning
* 🌐 Flask Web Application
* 📊 Data Analysis
* 🗄️ MySQL Database
* 🎯 Random Forest Classification

## ✨ Features

* 🎓 Student placement prediction
* 🤖 Random Forest Machine Learning model
* 📊 Academic performance analysis
* 📈 Attendance-based prediction
* 💼 Internship experience analysis
* 🧑‍💻 Project and backlog consideration
* 🌐 Interactive web interface
* 🗄️ MySQL database integration
* 💾 Trained model using Joblib
* ⚡ Fast prediction

## 🛠️ Technologies Used

| Technology    | Purpose              |
| ------------- | -------------------- |
| Python        | Programming & ML     |
| Flask         | Web Application      |
| Pandas        | Data Processing      |
| NumPy         | Numerical Computing  |
| Scikit-learn  | Machine Learning     |
| Random Forest | Classification       |
| Joblib        | Model Saving         |
| MySQL         | Database             |
| HTML          | Frontend             |
| CSS           | Styling              |
| JavaScript    | Frontend Interaction |
| Git & GitHub  | Version Control      |

## 🧠 Machine Learning Model

The project uses a **Random Forest Classifier** to predict student placement outcomes.

### Input Features

The model considers features such as:

* Age
* CGPA
* Attendance
* 10th Percentage
* 12th Percentage
* Backlogs
* Internship
* Number of Projects

### Prediction Output

The model predicts:

```text
Placed
```

or

```text
Not Placed
```

## 📂 Project Structure

```text
Student-Placement-Prediction/
│
├── app.py
├── start.bat
├── .gitignore
│
├── data/
│   ├── student_placement.csv
│   └── student_placement.xlsx
│
├── models/
│   └── random_forest_placement_model.pkl
│
├── src/
│   ├── generate_dataset.py
│   ├── train_model.py
│   ├── predict_placement.py
│   ├── import_to_mysql.py
│   └── test_mysql.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── app.js
│   └── favicon.ico
│
└── templates/
    └── index.html
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/MukeshYadav0143/Student-Placement-Prediction.git
```

### 2. Open the project

```bash
cd Student-Placement-Prediction
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

## 🧪 Example Prediction

### Student with strong academic profile

```text
CGPA: 8.5
Attendance: 85%
Internship: Yes
Projects: 4
Backlogs: 0
```

**Expected Prediction: Placed**

### Student with weaker profile

```text
CGPA: 6.0
Attendance: 60%
Internship: No
Projects: 0
Backlogs: 3
```

**Expected Prediction: Not Placed**

> Actual predictions depend on the trained Machine Learning model and input data.

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Data Preprocessing
   ↓
Feature Selection
   ↓
Train/Test Split
   ↓
Random Forest Training
   ↓
Model Evaluation
   ↓
Save Trained Model
   ↓
Flask Application
   ↓
Student Prediction
```

## 🗄️ MySQL Integration

The project includes MySQL integration for storing and working with student data.

Test the database connection:

```bash
python src/test_mysql.py
```

Import student data into MySQL:

```bash
python src/import_to_mysql.py
```

Make sure MySQL is installed and running before using these scripts.

## 🎯 Project Objectives

* Build a practical Machine Learning application.
* Predict student placement outcomes.
* Analyze factors related to placement.
* Integrate Machine Learning with Flask.
* Connect the application with MySQL.
* Develop a portfolio-ready Data Science project.

## 🚧 Future Improvements

* 📊 Interactive analytics dashboard
* 📈 Placement probability visualization
* 👨‍🎓 Prediction history
* 🔐 User authentication
* ☁️ Cloud deployment
* 📱 Improved responsive design
* 📉 Feature importance visualization
* 🧠 Multiple ML algorithm comparison

## 👨‍💻 Author

**Mukesh Yadav**

GitHub: [MukeshYadav0143](https://github.com/MukeshYadav0143)

## ⭐ Support

If you find this project useful, please consider giving the repository a ⭐.

## 📜 License

This project is created for educational and portfolio purposes.
