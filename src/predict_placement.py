import pandas as pd
import joblib
import os
import sys

def get_model():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(base_dir, "random_forest_placement_model.pkl")
    if not os.path.exists(model_path):
        print(f"[ERROR] Model file not found at: {model_path}")
        sys.exit(1)
    return joblib.load(model_path)

def predict_single(data_dict, model=None):
    if model is None:
        model = get_model()

    gender = data_dict.get("Gender", "male").lower()
    department = data_dict.get("Department", "CSE").upper()
    internship = 1 if str(data_dict.get("Internship", "0")).lower() in ["1", "yes", "true"] else 0

    student = pd.DataFrame([{
        "Age": int(data_dict.get("Age", 22)),
        "CGPA": float(data_dict.get("CGPA", 7.5)),
        "Attendance": float(data_dict.get("Attendance", 80.0)),
        "10th_Percentage": float(data_dict.get("10th_Percentage", 75.0)),
        "12th_Percentage": float(data_dict.get("12th_Percentage", 75.0)),
        "Backlogs": int(data_dict.get("Backlogs", 0)),
        "Internship": internship,
        "Projects": int(data_dict.get("Projects", 2)),
        "Communication_Score": float(data_dict.get("Communication_Score", 70)),
        "Aptitude_Score": float(data_dict.get("Aptitude_Score", 70)),
        "Gender_Female": 1 if gender == "female" else 0,
        "Gender_Male": 1 if gender == "male" else 0,
        "Department_CE": 1 if department == "CE" else 0,
        "Department_CSE": 1 if department == "CSE" else 0,
        "Department_ECE": 1 if department == "ECE" else 0,
        "Department_EEE": 1 if department == "EEE" else 0,
        "Department_IT": 1 if department == "IT" else 0,
        "Department_ME": 1 if department == "ME" else 0
    }])

    pred = int(model.predict(student)[0])
    prob = float(model.predict_proba(student)[0][1])

    # Estimate package based on CGPA, projects, aptitude, communication
    if pred == 1:
        base = 3.5
        cgpa_bonus = max(0.0, (student["CGPA"].iloc[0] - 6.0) * 1.6)
        proj_bonus = min(3.0, student["Projects"].iloc[0] * 0.8)
        apt_bonus = min(2.5, (student["Aptitude_Score"].iloc[0] / 100) * 2.5)
        comm_bonus = min(2.0, (student["Communication_Score"].iloc[0] / 100) * 2.0)
        intern_bonus = 1.5 if internship == 1 else 0.0
        backlog_penalty = student["Backlogs"].iloc[0] * 0.8
        est_package = round(max(3.0, min(18.0, base + cgpa_bonus + proj_bonus + apt_bonus + comm_bonus + intern_bonus - backlog_penalty)), 2)
    else:
        est_package = 0.0

    return {
        "prediction": pred,
        "status": "Placed" if pred == 1 else "Not Placed",
        "probability": round(prob * 100, 2),
        "estimated_package_lpa": est_package
    }

def main():
    print("==================================================")
    print("      STUDENT PLACEMENT PREDICTOR (CLI)          ")
    print("==================================================")
    try:
        age = int(input("Enter Age (e.g. 22): ") or 22)
        cgpa = float(input("Enter CGPA (e.g. 8.2): ") or 8.2)
        attendance = float(input("Enter Attendance % (e.g. 85): ") or 85)
        tenth = float(input("Enter 10th % (e.g. 82): ") or 82)
        twelfth = float(input("Enter 12th % (e.g. 78): ") or 78)
        backlogs = int(input("Enter Active Backlogs (e.g. 0): ") or 0)
        internship = input("Internship Completed? (Yes/No): ") or "Yes"
        projects = int(input("Number of Projects (e.g. 3): ") or 3)
        communication = float(input("Communication Score 0-100 (e.g. 80): ") or 80)
        aptitude = float(input("Aptitude Score 0-100 (e.g. 85): ") or 85)
        gender = input("Gender (Male/Female): ") or "Male"
        department = input("Department (CE/CSE/ECE/EEE/IT/ME): ") or "CSE"

        inputs = {
            "Age": age, "CGPA": cgpa, "Attendance": attendance,
            "10th_Percentage": tenth, "12th_Percentage": twelfth,
            "Backlogs": backlogs, "Internship": internship,
            "Projects": projects, "Communication_Score": communication,
            "Aptitude_Score": aptitude, "Gender": gender, "Department": department
        }

        result = predict_single(inputs)

        print("\n==================================================")
        print("                 PREDICTION RESULT                ")
        print("==================================================")
        print(f" Status               : {result['status'].upper()}")
        print(f" Placement Probability: {result['probability']}%")
        if result['prediction'] == 1:
            print(f" Estimated Package    : {result['estimated_package_lpa']} LPA")
        print("==================================================\n")

    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"[Error]: {e}")

if __name__ == "__main__":
    main()
