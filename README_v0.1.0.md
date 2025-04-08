# 🏁 F1 Podium Predictor

A production-grade machine learning project designed to predict whether a Formula 1 driver will finish on the podium (Top 3). This project combines data collection, feature engineering, model training, explainability, simulation, and deployment to create an interactive and API-enabled prediction engine.

---

## 🎯 Objective

Predict whether an F1 driver will finish on the podium (Top 3) using pre-race features such as grid position, team strength, and driver form.

---

## 💼 Use Cases

- 🕹️ iGaming (e.g., Altenar): Smarter odds generation
- 🧮 Fantasy F1: Optimize driver selections
- 📺 Broadcast/Media: Predictive insights for commentary
- 📊 Fan Dashboards: Data-driven race previews

---

## 📈 Evaluation Metrics

- Precision@3
- ROC-AUC
- Log-loss
- F1-score

---

## 📁 Project Structure

```bash
f1-podium-predictor/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_Problem_Definition.ipynb
│   └── 01b_Baseline_Model.ipynb
├── scripts/
├── app/
├── dashboard/
├── models/
├── tests/
├── docs/
│   └── feature_plan.md
├── config.yaml
├── .gitignore
├── requirements.txt
├── CHANGELOG.md
└── README.md
```

---

## 📦 Current Features (v0.1.0)

- ✅ Folder and repo structure created
- ✅ Problem framed clearly
- ✅ Feature planning completed
- ✅ Baseline rule-based model implemented (`GridPosition ≤ 3`)
- ✅ Version control and changelog setup
- ✅ GitHub repo initialized with branches and roadmap

---

## 🚀 Next Steps (Planned v0.2.0)

- Collect and clean historical F1 race data
- Perform EDA and preprocessing
- Engineer competitive features (driver/team form, reliability)

---

## 🧠 Baseline Model Strategy

Implemented a dummy model that predicts podium = `True` if the grid position ≤ 3.  
Serves as a performance reference for upcoming machine learning models.

---

## 🛠️ Installation

```bash
pip install -r requirements.txt
```

Use Jupyter Notebook or VS Code to run notebooks.

---

## 🔁 Versioning Strategy

- `main`: Stable releases
- `dev`: Active development
- `feat/...`: Feature branches per phase

Tags follow semantic versioning: `vMAJOR.MINOR.PATCH`

---

## 👤 Author

Created by [Mantas](https://github.com/mantas123456)  
🔬 Passionate about motorsport analytics & real-world ML deployment.

---

