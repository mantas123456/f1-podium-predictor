# 🏎️ F1 Podium Predictor

The **F1 Podium Predictor** is a full-cycle machine learning project built to predict whether a Formula 1 driver will finish in the top 3 (podium position). Designed as a professional-grade portfolio project, it demonstrates clean structuring, documentation, versioning, and deployment readiness.

---

## 🎯 Project Goals

- Predict podium finishes using grid position, team/driver data, and historical performance.
- Establish and compare rule-based vs. ML-driven predictions.
- Develop a reproducible and extensible MLOps-ready pipeline.
- Showcase production-grade version control and project hygiene.

---

## 🧩 Use Cases

| Use Case       | Description |
|----------------|-------------|
| 🎲 iGaming      | Enhance pre-race odds and live betting intelligence. |
| 📊 Fantasy F1   | Optimize team composition based on expected performance. |
| 🧪 Data Science | Portfolio demonstration of structured end-to-end ML. |
| 📺 Media        | Generate insights for commentary and visualizations. |

---

## 🔧 Project Features

| Phase          | Status  | Summary |
|----------------|---------|---------|
| Phase 1: Problem Definition & Baseline | ✅ Complete | Rule-based model using Grid Position ≤ 3 |
| Phase 2: Data Collection & EDA         | 🔜 Upcoming | Ingest historical race data, clean and structure |
| Phase 3: Feature Engineering & ML      | 🔜 Upcoming | Train classifiers, tune models, evaluate |
| Phase 4: Visualization & Dashboard     | 🔜 Upcoming | Present insights via dashboard (e.g. Streamlit) |
| Phase 5: API & Deployment              | 🔜 Upcoming | Serve predictions via REST API |

---

## 🧱 Folder Structure

```
f1-podium-predictor/
├── notebooks/
│   └── v0_1_0/                     ← Phase 1 notebooks
├── reports/
│   └── v0_1_0/                     ← Baseline metrics (JSON)
├── models/
│   └── v0_1_0/                     ← Saved model artifacts
├── data/
│   └── processed/v0_1_0/          ← Cleaned data snapshots
├── docs/
│   ├── feature_plan.md            ← Feature design planning
│   ├── baseline_results.md        ← Explanation of rule model results
│   └── model_design.md            ← Future ML architecture strategy
├── README.md                      ← Project overview
├── CHANGELOG.md                   ← Version log
├── requirements.txt               ← Python dependencies
├── .gitignore                     ← Ignored files
```

---

## 📊 Baseline Model (Phase 1)

**Logic:**  
> If `GridPosition <= 3`, predict `Podium = True`; otherwise `False`.

**Metrics (stored in `reports/v0_1_0/`)**
- Precision
- F1 Score
- Accuracy

---

## 🧠 Versioning Strategy

- Branches:
  - `main`: Stable releases only
  - `dev`: Pre-release integration and testing
  - `feat/...`: Feature-specific branches (e.g., `feat/baseline-model`)
- Folders:
  - Models, notebooks, data, and reports are organized by version (`v0_1_0`)
- Tags:
  - Git tags created for all public versions (`v0.1.0`, `v0.2.0`, etc.)

---

## 🚀 Setup & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/mantas123456/f1-podium-predictor.git
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Run the Baseline Notebook
```bash
jupyter notebook notebooks/v0_1_0/01b_Baseline_Model_v0.1.0.ipynb
```

---

## 📇 Author

**Mantas**  
Data Scientist | Sustainability & Innovation | Motorsport Analytics  
GitHub: [@mantas123456](https://github.com/mantas123456)

---

## 🛣️ Roadmap

- [x] Phase 1 – Problem framing, baseline model, metrics
- [ ] Phase 2 – Real F1 data ingestion and preprocessing
- [ ] Phase 3 – Model development & feature engineering
- [ ] Phase 4 – Dashboard & data visualization
- [ ] Phase 5 – API deployment and CI/CD integration

---

## 📜 License

This project is licensed under the MIT License — see the `LICENSE` file for details.
