# 🏁 F1 Podium Predictor

A production-quality machine learning project designed to predict whether a Formula 1 driver will finish on the podium (Top 3). This project combines data collection, advanced feature engineering, model training, explainability, simulation, and deployment to create a fully interactive and API-enabled prediction engine.

---

## 🎯 Objective

To build a reliable podium prediction model using pre-race information such as qualifying positions, team performance, driver history, and track characteristics.

---

## 💼 Use Cases

- 🕹️ **iGaming & Betting Platforms**: Enhance odds with ML-based probability estimates.
- 🧮 **Fantasy F1 Tools**: Help users choose drivers with highest podium potential.
- 📺 **Media & Broadcast**: Power real-time prediction visualizations.
- 🧠 **Race Strategy & Scenario Modeling**: Simulate likely outcomes based on grid positions and track conditions.

---

## 📈 Evaluation Metrics

- **Precision@3** – Accuracy of predicting correct podium drivers
- **ROC-AUC** – Classifier discrimination ability
- **Log-loss** – Calibration of predicted probabilities
- **F1-score** – Overall performance for Top 3 classification

---

## 📁 Project Structure

```bash
f1-podium-predictor/
├── data/               # Raw and processed datasets
│   ├── raw/
│   └── processed/
├── notebooks/          # Jupyter notebooks for exploration and modeling
├── scripts/            # Modular scripts for each pipeline stage
├── app/                # FastAPI backend or Streamlit app
├── dashboard/          # Dashboard code and configs
├── models/             # Saved models and checkpoints
├── tests/              # Unit tests
├── requirements.txt    # Python dependencies
├── .gitignore
└── README.md
```

---

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
