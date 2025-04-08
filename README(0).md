# 🏁 F1 Podium Predictor

A **production-quality machine learning project** designed to predict whether a Formula 1 driver will finish on the podium (Top 3).  
Combines rule-based and advanced ML approaches — integrating data collection, feature engineering, simulation, explainability, and real-time deployment.

---

> 🧠 *Can a machine predict podium finishes in Formula 1 with the strategic intuition of a race engineer? This project simulates that challenge using real-world data and machine learning.*

---

## 🎯 Objective

To build a reliable podium prediction engine using pre-race data like qualifying results, team/driver performance, and track characteristics — evolving from simple baselines to full ML inference.

---

## 💼 Use Cases

- 🕹️ **iGaming & Betting**: Improve odds-making with data-driven probabilities.
- 🧮 **Fantasy F1 Tools**: Optimize team picks based on predicted podium potential.
- 📺 **Media & Broadcast**: Power race-day visuals with explainable ML.
- 🧠 **Race Strategy Simulation**: Support outcome modeling before the lights go out.

---

## 📈 Evaluation Metrics

| Metric        | Purpose |
|---------------|---------|
| **Precision@3** | Accuracy of predicting podium finishes |
| **F1 Score**    | Classification balance (precision & recall) |
| **ROC-AUC**     | Discrimination ability of the model |
| **Log-loss**    | Calibration of predicted probabilities |

---

## 🧱 Project Structure


f1-podium-predictor/
├── data/
│   ├── raw/
│   └── processed/v0_1_0/
├── notebooks/
│   └── v0_1_0/
├── scripts/                 # Modular pipeline scripts
├── models/
│   └── v0_1_0/
├── reports/
│   └── v0_1_0/
├── app/                     # FastAPI app (planned)
├── dashboard/               # Streamlit dashboard (planned)
├── docs/
│   ├── feature_plan.md
│   ├── model_design.md
│   └── baseline_results.md
├── tests/
├── README.md
├── CHANGELOG.md
├── requirements.txt
├── .gitignore
└── LICENSE


## 🗂️ Detailed Development Plan

### Phase 1: Problem Framing
- Define prediction target: binary podium classification
- Identify use cases and stakeholders
- Establish success criteria (Precision@3 > 70%)

### Phase 2: Data Collection
- Collect race results, team/driver stats (≥5 seasons)
- Add track metadata, qualifying positions, weather
- Optional: Add pre-race NLP sentiment data

### Phase 3: Preprocessing & EDA
- Handle nulls/outliers, format consistency
- EDA with correlations, distributions, trends

### Phase 4: Feature Engineering
- Rolling averages (form), penalty flags, reliability
- Team/driver-track interactions
- SHAP-based importance analysis

### Phase 5: Model Training
- Try Logistic Regression, XGBoost, CatBoost
- Use k-fold CV stratified by race
- Evaluate all defined metrics

### Phase 6: Explainability & Error Analysis
- SHAP/LIME for top 10 features
- Analyze 3+ misclassification cases
- Calibration curve + confusion matrix

### Phase 7: Monte Carlo Simulation
- Run 10,000+ race simulations per GP
- Output podium probability distributions
- Compare vs real outcomes

### Phase 8: Real-Time Prediction API
- FastAPI endpoint: receive grid data, return podium prediction
- Test with JSON inputs
- Response time < 500ms

### Phase 9: Dashboard Development
- Streamlit app with driver/track/weather selectors
- Visualize probabilities, SHAP values, scenario simulations

### Phase 10: CI/CD & Testing
- Write unit tests for logic and pipeline
- Set up GitHub Actions for auto-testing and linting
- Achieve ≥80% code coverage

### Phase 11: Documentation & Delivery
- Complete README and setup instructions
- Demo video (2–4 min walkthrough)
- Publish blog post on LinkedIn or Medium
- Add project to GitHub portfolio and CV

---

## 📌 Version Control Strategy

- `main` – Production-ready code only
- `dev` – Active development (feature branches merged here)
- Feature branches:
  - `feat/data-collection`
  - `feat/feature-engineering`
  - `feat/model-training`
  - `feat/api`
  - `feat/dashboard`

✅ Use pull requests to merge `dev` into `main` after each completed phase.

---

## 🛠️ Requirements

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 📊 Status

🚧 Phase 1: Problem Framing – Complete  
🚧 Phase 2: Data Collection – In Progress  
🔜 Phase 3: EDA and Preprocessing – Next

---

## 👤 Author

Created by [Mantas](https://github.com/mantas123456) – Data Scientist with a passion for motorsport analytics and real-world machine learning deployment.
