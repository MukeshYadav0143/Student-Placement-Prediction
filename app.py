import os
import sys
import io
import json
import joblib
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, jsonify, Response, send_from_directory

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load Machine Learning Model
MODEL_PATH = os.path.join(BASE_DIR, "random_forest_placement_model.pkl")
DATA_PATH = os.path.join(BASE_DIR, "data", "student_placement.csv")

print("[INFO] Loading Random Forest Model...")
try:
    model = joblib.load(MODEL_PATH)
    print("[SUCCESS] Model loaded successfully.")
except Exception as e:
    model = None
    print(f"[WARNING] Could not load model: {e}")

# Load Dataset for Analytics
df_analytics = None
if os.path.exists(DATA_PATH):
    try:
        df_analytics = pd.read_csv(DATA_PATH)
        print(f"[SUCCESS] Dataset loaded: {len(df_analytics)} records.")
    except Exception as e:
        print(f"[WARNING] Failed to load dataset: {e}")

FEATURE_COLS = [
    "Age", "CGPA", "Attendance", "10th_Percentage", "12th_Percentage",
    "Backlogs", "Internship", "Projects", "Communication_Score",
    "Aptitude_Score", "Gender_Female", "Gender_Male",
    "Department_CE", "Department_CSE", "Department_ECE",
    "Department_EEE", "Department_IT", "Department_ME"
]

def format_student_input(data):
    gender = str(data.get("gender", "male")).strip().lower()
    department = str(data.get("department", "CSE")).strip().upper()
    internship_val = data.get("internship", 0)
    internship = 1 if str(internship_val).lower() in ["1", "yes", "true"] else 0

    return pd.DataFrame([{
        "Age": int(data.get("age", 22)),
        "CGPA": float(data.get("cgpa", 7.5)),
        "Attendance": float(data.get("attendance", 80.0)),
        "10th_Percentage": float(data.get("tenth", 75.0)),
        "12th_Percentage": float(data.get("twelfth", 75.0)),
        "Backlogs": int(data.get("backlogs", 0)),
        "Internship": internship,
        "Projects": int(data.get("projects", 2)),
        "Communication_Score": float(data.get("communication", 70.0)),
        "Aptitude_Score": float(data.get("aptitude", 70.0)),
        "Gender_Female": 1 if gender == "female" else 0,
        "Gender_Male": 1 if gender == "male" else 0,
        "Department_CE": 1 if department == "CE" else 0,
        "Department_CSE": 1 if department == "CSE" else 0,
        "Department_ECE": 1 if department == "ECE" else 0,
        "Department_EEE": 1 if department == "EEE" else 0,
        "Department_IT": 1 if department == "IT" else 0,
        "Department_ME": 1 if department == "ME" else 0
    }])[FEATURE_COLS]

def calculate_insights(data, prob, pred):
    cgpa = float(data.get("cgpa", 7.5))
    backlogs = int(data.get("backlogs", 0))
    projects = int(data.get("projects", 0))
    internship = 1 if str(data.get("internship", "0")).lower() in ["1", "yes", "true"] else 0
    aptitude = float(data.get("aptitude", 70))
    communication = float(data.get("communication", 70))
    attendance = float(data.get("attendance", 80))

    strengths = []
    weaknesses = []
    recommendations = []

    # Strengths
    if cgpa >= 8.5:
        strengths.append(f"Outstanding academic standing ({cgpa} CGPA) puts you in the top candidate pool.")
    elif cgpa >= 7.5:
        strengths.append(f"Strong academic record ({cgpa} CGPA) satisfies major corporate cut-offs.")

    if backlogs == 0:
        strengths.append("Zero active backlogs ensures 100% company drive eligibility.")
    if projects >= 3:
        strengths.append(f"Robust project portfolio ({projects} projects) showcases practical execution skill.")
    if internship == 1:
        strengths.append("Valuable industrial internship experience gives you a competitive hiring advantage.")
    if aptitude >= 80:
        strengths.append(f"High aptitude score ({aptitude}/100) will help ace initial screening rounds.")
    if communication >= 80:
        strengths.append(f"Excellent communication skills ({communication}/100) will shine in HR and technical interviews.")

    # Weaknesses
    if backlogs > 0:
        weaknesses.append(f"{backlogs} active backlog(s) may disqualify you from 75%+ tier-1 recruitment rounds.")
    if cgpa < 7.0:
        weaknesses.append(f"CGPA of {cgpa} is below preferred thresholds for premier technology companies.")
    if internship == 0:
        weaknesses.append("Lack of real-world internship experience makes practical readiness harder to prove.")
    if projects < 2:
        weaknesses.append(f"Only {projects} project(s) listed; recruiters heavily favor 3+ demonstrable projects.")
    if communication < 65:
        weaknesses.append(f"Communication score ({communication}/100) needs strengthening for interview clearance.")
    if aptitude < 65:
        weaknesses.append(f"Aptitude score ({aptitude}/100) is at risk for online assessment filtration.")
    if attendance < 75:
        weaknesses.append(f"Attendance ({attendance}%) indicates low campus participation consistency.")

    # Recommendations
    if backlogs > 0:
        recommendations.append("Priority 1: Clear all active backlogs immediately before final placement season begins.")
    if internship == 0:
        recommendations.append("Secure a 4-8 week virtual or on-site industry internship or open-source contribution.")
    if projects < 3:
        recommendations.append("Build and deploy 1-2 end-to-end full-stack or AI/ML projects on GitHub with live demos.")
    if aptitude < 75:
        recommendations.append("Practice 15 quantitative & logical aptitude questions daily on platforms like IndiaBIX or LeetCode.")
    if communication < 75:
        recommendations.append("Participate in mock interviews and GD sessions to boost confidence and articulation.")

    if not recommendations:
        recommendations.append("Maintain your exceptional profile! Practice advanced problem-solving for Dream/Super Dream companies.")

    # Calculate estimated package
    if pred == 1:
        base = 4.0
        cgpa_bonus = max(0.0, (cgpa - 6.0) * 1.5)
        proj_bonus = min(3.5, projects * 0.9)
        apt_bonus = min(2.5, (aptitude / 100) * 2.5)
        comm_bonus = min(2.0, (communication / 100) * 2.0)
        intern_bonus = 2.0 if internship == 1 else 0.0
        backlog_penalty = backlogs * 1.0
        package = round(max(3.5, min(22.0, base + cgpa_bonus + proj_bonus + apt_bonus + comm_bonus + intern_bonus - backlog_penalty)), 2)
    else:
        package = 0.0

    # Determine Tier
    if package >= 12.0:
        tier = "Super Dream Tier (12+ LPA)"
        tier_badge = "badge-super-dream"
    elif package >= 8.0:
        tier = "Dream Tier (8 - 12 LPA)"
        tier_badge = "badge-dream"
    elif package >= 4.5:
        tier = "Prime Tier (4.5 - 8 LPA)"
        tier_badge = "badge-prime"
    elif package > 0:
        tier = "Standard Core (3.5 - 4.5 LPA)"
        tier_badge = "badge-standard"
    else:
        tier = "Not Applicable"
        tier_badge = "badge-none"

    # Radar scores (0 to 100)
    radar = {
        "Academics": round(min(100.0, (cgpa / 10.0) * 100), 1),
        "Consistency": round(min(100.0, attendance), 1),
        "Projects": round(min(100.0, (projects / 5.0) * 100), 1),
        "Aptitude": round(min(100.0, aptitude), 1),
        "Communication": round(min(100.0, communication), 1),
        "Experience": 100.0 if internship == 1 else 30.0
    }

    return {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "recommendations": recommendations,
        "package_lpa": package,
        "tier": tier,
        "tier_badge": tier_badge,
        "radar": radar
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static"), "favicon.ico", mimetype="image/vnd.microsoft.icon")

@app.route("/api/predict", methods=["POST"])
def api_predict():
    if model is None:
        return jsonify({"error": "Model not loaded on server."}), 500

    try:
        data = request.get_json(force=True)
        student_df = format_student_input(data)

        pred = int(model.predict(student_df)[0])
        prob = float(model.predict_proba(student_df)[0][1])
        prob_pct = round(prob * 100, 2)

        insights = calculate_insights(data, prob, pred)

        return jsonify({
            "status": "success",
            "prediction": pred,
            "placement_status": "Placed" if pred == 1 else "Not Placed",
            "probability": prob_pct,
            "insights": insights
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/what-if", methods=["POST"])
def api_what_if():
    if model is None:
        return jsonify({"error": "Model not loaded on server."}), 500

    try:
        data = request.get_json(force=True)
        student_df = format_student_input(data)
        prob = float(model.predict_proba(student_df)[0][1])
        pred = int(model.predict(student_df)[0])

        return jsonify({
            "probability": round(prob * 100, 2),
            "prediction": pred,
            "placement_status": "Placed" if pred == 1 else "Not Placed"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/analytics", methods=["GET"])
def api_analytics():
    if df_analytics is None:
        return jsonify({"error": "Analytics dataset not available."}), 500

    total_students = int(len(df_analytics))
    placed_count = int((df_analytics["Placement_Status"] == "Placed").sum())
    placement_rate = round((placed_count / total_students) * 100, 1)

    # Department placement rates
    dept_group = df_analytics.groupby("Department")["Placement_Status"].apply(
        lambda s: round((s == "Placed").mean() * 100, 1)
    ).to_dict()

    # Backlog vs Placement rate
    backlog_group = df_analytics.groupby("Backlogs")["Placement_Status"].apply(
        lambda s: round((s == "Placed").mean() * 100, 1)
    ).to_dict()

    # Average package of placed students
    placed_df = df_analytics[df_analytics["Placement_Status"] == "Placed"]
    avg_package = round(float(placed_df["Package_LPA"].mean()), 2) if len(placed_df) > 0 else 0.0

    return jsonify({
        "total_students": total_students,
        "placed_students": placed_count,
        "placement_rate": placement_rate,
        "avg_package_lpa": avg_package,
        "department_rates": dept_group,
        "backlog_rates": backlog_group
    })

@app.route("/api/sample/<profile_type>", methods=["GET"])
def api_sample(profile_type):
    samples = {
        "high_achiever": {
            "age": 22,
            "gender": "Female",
            "department": "CSE",
            "cgpa": 9.2,
            "attendance": 94.0,
            "tenth": 91.5,
            "twelfth": 89.0,
            "backlogs": 0,
            "internship": 1,
            "projects": 4,
            "communication": 90,
            "aptitude": 92
        },
        "average_student": {
            "age": 22,
            "gender": "Male",
            "department": "IT",
            "cgpa": 7.4,
            "attendance": 78.0,
            "tenth": 76.0,
            "twelfth": 74.5,
            "backlogs": 1,
            "internship": 0,
            "projects": 2,
            "communication": 68,
            "aptitude": 70
        },
        "at_risk": {
            "age": 23,
            "gender": "Male",
            "department": "ME",
            "cgpa": 5.9,
            "attendance": 58.0,
            "tenth": 60.0,
            "twelfth": 58.0,
            "backlogs": 3,
            "internship": 0,
            "projects": 1,
            "communication": 50,
            "aptitude": 48
        },
        "comeback_aspirant": {
            "age": 22,
            "gender": "Female",
            "department": "ECE",
            "cgpa": 8.0,
            "attendance": 84.0,
            "tenth": 82.0,
            "twelfth": 80.0,
            "backlogs": 0,
            "internship": 1,
            "projects": 3,
            "communication": 78,
            "aptitude": 82
        }
    }

    if profile_type in samples:
        return jsonify(samples[profile_type])
    return jsonify({"error": "Unknown sample profile."}), 404

@app.route("/api/batch-predict", methods=["POST"])
def api_batch_predict():
    if model is None:
        return jsonify({"error": "Model not loaded on server."}), 500

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded."}), 400

    file = request.files["file"]
    if not file.filename.endswith(".csv"):
        return jsonify({"error": "Only CSV files are supported."}), 400

    try:
        df_uploaded = pd.read_csv(file)
        results = []

        for _, row in df_uploaded.iterrows():
            row_dict = row.to_dict()
            student_df = format_student_input(row_dict)
            pred = int(model.predict(student_df)[0])
            prob = float(model.predict_proba(student_df)[0][1])

            res = {
                "Student_ID": row_dict.get("Student_ID", _ + 1),
                "CGPA": row_dict.get("CGPA", row_dict.get("cgpa", 0)),
                "Department": row_dict.get("Department", row_dict.get("department", "Unknown")),
                "Prediction": "Placed" if pred == 1 else "Not Placed",
                "Probability_Pct": round(prob * 100, 2)
            }
            results.append(res)

        return jsonify({
            "total_records": len(results),
            "placed_count": sum(1 for r in results if r["Prediction"] == "Placed"),
            "data": results
        })
    except Exception as e:
        return jsonify({"error": f"Failed to process CSV: {str(e)}"}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting server on http://127.0.0.1:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
