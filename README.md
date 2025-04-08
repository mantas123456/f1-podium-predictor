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

```bash
f1-podium-predictor/
├── data/
│   ├── raw/
│   └── processed/v0_1_0/
├── notebooks/
│   └── v0_1_0/
├── scripts/
├── models/
│   └── v0_1_0/
├── reports/
│   └── v0_1_0/
├── app/
├── dashboard/
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
```

---

## 🔁 Version Control Strategy

- `main` → ✅ Clean, production-ready code only (e.g. `v0.1.0`)
- `dev` → 🧪 Active development & feature integration
- `feat/*` → Feature-specific work (e.g. `feat/data-collection`)

Use PRs to merge `feat/` → `dev`, then `dev` → `main`  
Each version (`v0_1_0`, `v0_2_0`, ...) has its own notebooks, models, and outputs.

---

## 🧪 Phase Roadmap

### ✅ Phase 1: Problem Framing & Baseline (Complete)
- Rule: Podium = Grid Position ≤ 3
- Metric output stored in `reports/v0_1_0/`
- Notebook: `notebooks/v0_1_0/01b_Baseline_Model_v0.1.0.ipynb`

### 🚧 Phase 2: Data Collection & Cleaning (Next)
- Scrape or import ≥5 seasons of race data
- Include grid, results, weather, track, reliability

### 🔜 Future Phases
- Feature Engineering
- ML Model Training
- SHAP/LIME Explainability
- Monte Carlo Simulation
- API Inference (FastAPI)
- Dashboard Visualization (Streamlit)
- CI/CD and Testing

---

## 🧠 Setup Instructions

```bash
git clone https://github.com/mantas123456/f1-podium-predictor.git
cd f1-podium-predictor
pip install -r requirements.txt
```

To run the baseline model:
```bash
jupyter notebook notebooks/v0_1_0/01b_Baseline_Model_v0.1.0.ipynb
```

---

## 📜 License

This project is licensed under the MIT License — see the `LICENSE` file.

---

## 👤 Author

Created by [Mantas](https://github.com/mantas123456)  
🔬 Data Scientist | 🏎 Motorsport Fan | 💡 ML for Real-World Insight
