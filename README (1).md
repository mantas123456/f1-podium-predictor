# 🏁 F1 Podium Predictor

A production-grade machine learning project designed to predict whether a Formula 1 driver will finish on the podium (Top 3).  
Built to demonstrate full-cycle ML project structure, documentation, versioning, and deployment-readiness.

---

## 🎯 Objective

Predict podium finishes (Top 3) in F1 races using grid position and future engineered features.  
Phase 1 uses a baseline rule model for performance benchmarking.

---

## 📦 Project Features (v0.1.0)

- ✅ Rule-based baseline model (Grid Position ≤ 3 → Podium)
- ✅ Full versioned folder structure (`v0_1_0`)
- ✅ Output metrics saved to `reports/v0_1_0/`
- ✅ Project structure suitable for scalable ML dev
- ✅ Git branching strategy with `feat/`, `dev`, and `main`

---

## 🧠 Use Cases

- 🎲 iGaming: Smarter race odds & insights
- 📊 Fantasy F1: Optimize team picks
- 🧮 Data Science Portfolio: Showcase clean ML pipeline
- 🎓 Learning: Project design & MLOps readiness

---

## 🗂 Folder Structure

```
f1-podium-predictor/
├── notebooks/v0_1_0/              # Phase 1 notebooks
├── reports/v0_1_0/                # Baseline metrics JSON
├── models/v0_1_0/                 # Model artifacts (if applicable)
├── data/processed/v0_1_0/        # Cleaned data snapshots
├── docs/feature_plan.md          # Input features and design
├── README.md                     # Project overview
├── CHANGELOG.md                  # Version log
├── requirements.txt              # (To be added)
```

---

## 📈 Baseline Model Logic

Simple rule-based model for benchmarking:
```python
if GridPosition <= 3:
    Podium = True
else:
    Podium = False
```

Results stored in `reports/v0_1_0/baseline_metrics.json`

---

## 🔁 Versioning Strategy

- `main` → Clean, stable releases only
- `dev` → Integration & testing
- `feat/*` → Feature-specific branches

Tags use semantic versioning (`v0.1.0`, `v0.2.0`, etc.)  
Outputs, notebooks, and models are stored in versioned folders.

---

## 📄 Current Version

**Version:** `v0.1.0`  
**Release Date:** April 2025  
**Status:** ✅ Baseline complete, starting Phase 2

---

## 👤 Author

**Mantas**  
Passionate about F1, data science, and high-performance clean ML pipelines.  
GitHub: [@mantas123456](https://github.com/mantas123456)

---

## 🛣️ Roadmap

- 📥 Phase 2 – Data Collection & EDA
- 🤖 Phase 3 – ML Training & Feature Engineering
- 📊 Phase 4 – Dashboard & Visual Insights
- 🔌 Phase 5 – API Deployment
