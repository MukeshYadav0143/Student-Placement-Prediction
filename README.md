# 🎓 Student Placement Prediction AI

### 🚀 Machine Learning Powered Student Placement Prediction & Analytics Platform

## 🌐 Live Demo

🚀 **Try CampusPulse AI:**  
https://student-placement-prediction-sigma.vercel.app/

An end-to-end **Machine Learning web application** that analyzes student academic and career-related data to predict placement outcomes using **Random Forest, Python, Flask, MySQL, Pandas, NumPy, HTML, CSS and JavaScript**.

---

## 👨‍💻 Developer Profile

### **Mukesh Yadav**

**Data Science & AI Enthusiast | Machine Learning Developer | Full-Stack Developer**

📍 Lucknow, Uttar Pradesh, India

| Attribute          | Details                                                                             |
| ------------------ | ----------------------------------------------------------------------------------- |
| **Developer**      | **Mukesh Yadav**                                                                    |
| **University**     | **Babu Banarasi Das University (BBDU)**                                             |
| **Degree**         | **Bachelor of Computer Applications (BCA)**                                         |
| **Specialization** | **Data Science & Artificial Intelligence**                                          |
| **Batch**          | **2024–2027**                                                                       |
| **Core Focus**     | Machine Learning, Data Analytics, Python & Full-Stack Development                   |
| **Project Role**   | Data Processing, ML Model Development, Flask Integration, Database Integration & UI |

🔗 **GitHub:** [MukeshYadav0143](https://github.com/MukeshYadav0143)

---

# 📌 About The Project

**Student Placement Prediction AI** is a Machine Learning based application developed to predict whether a student is likely to be **Placed** or **Not Placed** based on academic performance and career-related information.

The system combines a trained **Random Forest Classifier** with a **Flask web application**, allowing users to enter student information through a simple web interface and receive an ML-based prediction.

The project also includes **MySQL database integration** for storing and analyzing student data.

---

# 💡 Project Vision

Student placement depends on multiple academic and career-related factors.

This project aims to demonstrate how Machine Learning can be used to analyze these factors and build an intelligent prediction system.

### The system focuses on:

* 📊 Understanding student performance
* 🤖 Applying Machine Learning to placement prediction
* 🎓 Identifying patterns in student data
* 💼 Considering internship and project experience
* 📈 Supporting data-driven placement analysis
* 🌐 Integrating ML with a real web application
* 🗄️ Managing student data using MySQL

> **The prediction is an ML-based estimate and does not guarantee actual placement.**

---

# 🚀 Key Features

## 1. 🤖 Machine Learning Placement Prediction

The core of the project is a **Random Forest Classifier** trained on student placement data.

The model analyzes multiple student attributes and predicts:

```text
Placed
```

or

```text
Not Placed
```

---

## 2. 📊 Academic Performance Analysis

The system considers important academic indicators such as:

* CGPA
* 10th Percentage
* 12th Percentage
* Attendance
* Backlogs

These features help the model identify relationships between academic performance and placement outcomes.

---

## 3. 💼 Career Profile Analysis

The application also considers:

* Internship experience
* Number of projects
* Academic performance
* Backlogs

This provides the model with a broader representation of a student's profile.

---

## 4. 🌐 Interactive Web Application

Students can enter their information through a browser-based interface.

### Prediction Flow

```text
Student Information
        ↓
Web Interface
        ↓
Flask Backend
        ↓
Machine Learning Model
        ↓
Random Forest Prediction
        ↓
Placed / Not Placed
```

---

## 5. 🌲 Random Forest Classification

The project uses **Random Forest**, an ensemble learning algorithm that combines multiple decision trees to produce a classification result.

### Advantages

* Handles multiple input features
* Suitable for structured/tabular datasets
* Captures complex relationships
* Robust classification algorithm
* Easy to integrate with Python applications

---

## 6. 🗄️ MySQL Database Integration

The project includes MySQL integration for student data management.

MySQL can be used for:

* Student records
* Placement data
* SQL analysis
* Data management
* Dataset import
* Database connectivity testing

---

## 7. 💾 Trained Model Storage

The trained Machine Learning model is stored using **Joblib**.

```text
models/random_forest_placement_model.pkl
```

This allows the Flask application to load the already-trained model and perform predictions without retraining every time.

---

# 🧠 Machine Learning Workflow

```text
                 Student Dataset
                       │
                       ▼
              Data Preparation
                       │
                       ▼
                Feature Selection
                       │
                       ▼
                Train / Test Split
                       │
                       ▼
             Random Forest Training
                       │
                       ▼
                Model Evaluation
                       │
                       ▼
               Save Model - Joblib
                       │
                       ▼
                 Flask Application
                       │
                       ▼
              Student Input Form
                       │
                       ▼
              ML Model Prediction
                       │
                       ▼
             ┌───────────────────┐
             │  PLACED /         │
             │  NOT PLACED       │
             └───────────────────┘
```

---

# 📥 Machine Learning Input Features

| Feature             | Description                  |
| ------------------- | ---------------------------- |
| **Age**             | Student age                  |
| **CGPA**            | College academic performance |
| **Attendance**      | Attendance percentage        |
| **10th Percentage** | Class 10 academic score      |
| **12th Percentage** | Class 12 academic score      |
| **Backlogs**        | Number of academic backlogs  |
| **Internship**      | Internship experience        |
| **Projects**        | Number of completed projects |

---

# 📤 Prediction Output

The application generates a classification result:

### ✅ Placed

The trained model predicts that the student's input belongs to the **Placed** class.

### ❌ Not Placed

The trained model predicts that the student's input belongs to the **Not Placed** class.

> Predictions are based on patterns learned from the training dataset and should not be considered a guaranteed placement result.

---

# 🏗️ System Architecture

```text
┌─────────────────────────────────────────────┐
│                 USER LAYER                  │
│                                             │
│       Student enters profile details        │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│              PRESENTATION LAYER             │
│                                             │
│          HTML • CSS • JavaScript            │
│             Prediction Interface            │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│              APPLICATION LAYER              │
│                                             │
│             Flask • Python                 │
│       Request Handling & Prediction         │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│            MACHINE LEARNING LAYER           │
│                                             │
│       Random Forest Classifier              │
│       Joblib Trained Model                  │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│               OUTPUT LAYER                  │
│                                             │
│           PLACED / NOT PLACED              │
└─────────────────────────────────────────────┘

                       │
                       ▼

┌─────────────────────────────────────────────┐
│              DATABASE LAYER                 │
│                                             │
│                   MySQL                     │
│        Student Data & SQL Analysis         │
└─────────────────────────────────────────────┘
```

---

# 🛠️ Technology Stack

| Technology           | Purpose                        |
| -------------------- | ------------------------------ |
| 🐍 **Python**        | Programming & Machine Learning |
| 🌐 **Flask**         | Web Application Backend        |
| 🐼 **Pandas**        | Data Processing                |
| 🔢 **NumPy**         | Numerical Computing            |
| 🧠 **Scikit-learn**  | Machine Learning               |
| 🌲 **Random Forest** | Classification Algorithm       |
| 💾 **Joblib**        | Model Serialization            |
| 🗄️ **MySQL**        | Database                       |
| 🎨 **HTML**          | Web Structure                  |
| 🎨 **CSS**           | User Interface                 |
| ⚡ **JavaScript**     | Frontend Interaction           |
| 🔧 **Git**           | Version Control                |
| 🐙 **GitHub**        | Repository & Collaboration     |

---

# 📂 Project Directory Structure

```text
Student-Placement-Prediction/
│
├── app.py
├── start.bat
├── requirements.txt
├── .gitignore
├── README.md
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

---

# ⚡ Quick Start Guide

## 📋 Prerequisites

Before running the project, install:

* Python 3.x
* MySQL
* Git
* Modern Web Browser

---

## Step 1 — Clone Repository

```bash
git clone https://github.com/MukeshYadav0143/Student-Placement-Prediction.git
cd Student-Placement-Prediction
```

---

## Step 2 — Create Virtual Environment

```bash
python -m venv .venv
```

---

## Step 3 — Activate Virtual Environment

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

Then activate again:

```powershell
.venv\Scripts\Activate.ps1
```

---

## Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 5 — Run the Application

```bash
python app.py
```

The Flask server will start locally.

Open:

```text
http://127.0.0.1:5000
```

---

# 🗄️ MySQL Setup & Integration

The project contains Python scripts for MySQL integration.

### Test MySQL Connection

```bash
python src/test_mysql.py
```

### Import Student Dataset

```bash
python src/import_to_mysql.py
```

Make sure the MySQL server is running before executing database-related scripts.

---

# 📊 Data Analysis

The student dataset can be analyzed to understand patterns related to placement.

### Possible Analysis Areas

* 📈 Placement Rate
* 🎓 CGPA vs Placement
* 📅 Attendance vs Placement
* 💼 Internship vs Placement
* 🧑‍💻 Projects vs Placement
* 📚 Backlogs vs Placement
* 📊 Academic Performance vs Placement

These analyses can help understand which factors are associated with different placement outcomes in the dataset.

---

# 🧪 Example Prediction

## Example 1 — Strong Academic & Career Profile

```text
Age: 22
CGPA: 8.5
Attendance: 85%
10th Percentage: 80%
12th Percentage: 82%
Backlogs: 0
Internship: Yes
Projects: 4
```

### Model Output

```text
Placed
```

---

## Example 2 — Different Student Profile

```text
Age: 22
CGPA: 6.0
Attendance: 60%
10th Percentage: 55%
12th Percentage: 59%
Backlogs: 3
Internship: No
Projects: 0
```

### Model Output

```text
Not Placed
```

> Actual predictions depend on the trained model and the supplied input values.

---

# 🔬 Model Development

The project follows a complete Machine Learning development process.

### Training Pipeline

```text
Dataset
   ↓
Data Loading
   ↓
Data Preparation
   ↓
Feature Selection
   ↓
Train/Test Split
   ↓
Random Forest Training
   ↓
Model Evaluation
   ↓
Model Serialization
   ↓
Flask Integration
```

The trained model is saved as:

```text
random_forest_placement_model.pkl
```

using **Joblib**.

---

# 📈 Model Evaluation

The model is evaluated using a train/test split to measure how well it performs on unseen data.

Common evaluation metrics for this classification task include:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

These metrics help evaluate the effectiveness of the trained placement prediction model.

---

# 💡 Why This Project?

This project demonstrates a complete **end-to-end Machine Learning workflow** rather than only training a model.

### It combines:

```text
Data
 +
Machine Learning
 +
Web Development
 +
Database
 +
Deployment Concepts
```

The project provides practical experience in:

* Python programming
* Data preprocessing
* Machine Learning
* Classification
* Model serialization
* Flask development
* MySQL integration
* Frontend development
* Git & GitHub

---

# 🎯 Project Objectives

* 🤖 Build a Machine Learning based placement prediction system.
* 📊 Analyze student academic and career-related data.
* 🌲 Implement Random Forest classification.
* 🌐 Integrate the ML model with Flask.
* 🗄️ Connect the project with MySQL.
* 🎨 Build an interactive web interface.
* 🧠 Understand an end-to-end ML workflow.
* 💼 Develop a portfolio-ready Data Science project.

---

# 🗺️ Roadmap & Future Enhancements

## Phase 1 — Completed

* [x] Student dataset
* [x] Data processing
* [x] Random Forest model
* [x] Model evaluation
* [x] Joblib model saving
* [x] Flask web application
* [x] MySQL integration
* [x] GitHub repository
* [x] Professional README

## Phase 2 — Planned

* [ ] 📊 Interactive analytics dashboard
* [ ] 📈 Placement probability visualization
* [ ] 🧠 Feature importance visualization
* [ ] 🔬 Multiple ML algorithm comparison
* [ ] 📋 Prediction history
* [ ] 📊 Advanced data visualization

## Phase 3 — Advanced

* [ ] 🔐 User authentication
* [ ] ☁️ Cloud deployment
* [ ] 🔗 REST API
* [ ] 📱 Mobile-friendly interface
* [ ] 🔄 Automated model retraining
* [ ] 📈 Model monitoring

---

# 🌟 Project Highlights

```text
🎓 Student Placement Prediction
🤖 Machine Learning
🌲 Random Forest Classifier
🐍 Python
🌐 Flask
📊 Pandas & NumPy
🗄️ MySQL
💾 Joblib
🎨 HTML / CSS / JavaScript
🔧 Git & GitHub
```

---

# 🤝 Contributing

Contributions, suggestions and improvements are welcome.

```text
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Commit your changes
5. Push the branch
6. Open a Pull Request
```

---

# 📄 License

This project is created for **educational and portfolio purposes**.

---

# 👨‍💻 Author

## **Mukesh Yadav**

### Data Science & AI Enthusiast | Machine Learning Developer

**Babu Banarasi Das University (BBDU)**
**BCA — Data Science & Artificial Intelligence**

🔗 **GitHub:** [MukeshYadav0143](https://github.com/MukeshYadav0143)

---

<div align="center">

# 🎓 Student Placement Prediction AI

### Turning Student Data into Intelligent Placement Insights

**Built with Python • Machine Learning • Flask • MySQL**

### ❤️ Crafted by Mukesh Yadav

⭐ **If you find this project useful, please consider giving it a star!** ⭐

</div>
