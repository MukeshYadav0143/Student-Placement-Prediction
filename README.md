# CampusPulse AI - Student Placement Predictor & Career Intelligence

CampusPulse AI is an end-to-end machine learning platform that predicts student campus placement probability, calculates expected compensation packages (LPA), diagnoses profile strengths and red flags, and provides actionable career improvement roadmaps.

## Key Features
- **AI Placement Prediction**: Powered by a tuned Random Forest Classifier trained on 5,000+ benchmark profiles.
- **Estimated Compensation Package**: Accurately computes package tiers (Standard Core, Prime, Dream, Super Dream).
- **6-Factor Readiness Radar**: Academics, Consistency, Projects, Aptitude, Communication, and Experience.
- **Interactive 'What-If' Simulator**: Real-time slider feedback to test career decisions.
- **Cohort Historical Analytics**: Department statistics and backlog impact charts.
- **Batch Evaluation & CSV Export**: Bulk evaluate cohorts with 1-click CSV download.
- **Interactive Animated UI**: Particle constellation background, circular SVG gauge, and celebratory confetti.

## Quick Start
1. Run the Web App:
   `ash
   python run.py
   `
   Opens automatically at http://127.0.0.1:5000.

2. Command-Line (CLI) Mode:
   `ash
   python src/predict_placement.py
   `

3. Retrain Model:
   `ash
   python src/train_model.py
   `
