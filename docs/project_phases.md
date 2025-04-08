# 🗂️ Project Phases – F1 Podium Predictor

This document outlines the full end-to-end project lifecycle for the F1 Podium Predictor. Each phase includes its purpose, key tasks, status, and the relevant output or file paths.

---

## ✅ Phase 1: Problem Framing & Baseline

**Goal:** Define the ML objective and implement a simple rule-based baseline.

| Task                          | Status | Output |
|-------------------------------|--------|--------|
| Define prediction target      | ✅     | `docs/feature_plan.md` |
| Build rule-based model        | ✅     | `notebooks/v0_1_0/01b_Baseline_Model_v0.1.0.ipynb` |
| Save evaluation metrics       | ✅     | `reports/v0_1_0/baseline_metrics.json` |
| Document results              | ✅     | `docs/baseline_results.md` |

**Version:** `v0_1_0`

---

## 🚧 Phase 2: Data Collection & Preprocessing

**Goal:** Collect real F1 data and prepare it for modeling.

| Task                              | Status | Planned Output |
|-----------------------------------|--------|----------------|
| Gather race results & stats       | ⏳     | `data/raw/` |
| Parse and clean features          | ⏳     | `data/processed/v0_2_0/` |
| Handle nulls/outliers             | ⏳     | `notebooks/v0_2_0/data_cleaning.ipynb` |

**Branch:** `feat/data-collection`  
**Version:** `v0_2_0`

---

## 🧪 Phase 3: EDA & Feature Engineering

**Goal:** Discover patterns, trends, and enhance predictive signal.

| Task                        | Status | Planned Output |
|-----------------------------|--------|----------------|
| Analyze driver/grid correlations | 🔜 | `notebooks/v0_2_0/eda.ipynb` |
| Engineer new features       | 🔜     | `docs/feature_plan.md` |
| Visualize trends            | 🔜     | `reports/v0_2_0/eda_charts/` |

---

## 🤖 Phase 4: Model Training & Selection

**Goal:** Train and validate predictive ML models.

| Task                      | Status | Output |
|---------------------------|--------|--------|
| Train ML classifiers      | 🔜     | `models/v0_3_0/` |
| Run cross-validation      | 🔜     | `reports/v0_3_0/metrics.json` |
| Compare models            | 🔜     | `docs/model_design.md` |

---

## 🔍 Phase 5: Explainability

**Goal:** Use SHAP/LIME to interpret model predictions.

| Task                      | Status | Output |
|---------------------------|--------|--------|
| Apply SHAP values         | 🔜     | `reports/v0_3_0/explainability/` |
| Create feature impact plots| 🔜    | `notebooks/v0_3_0/interpretation.ipynb` |

---

## 🎲 Phase 6: Monte Carlo Simulation

**Goal:** Simulate 10,000+ race outcomes for robust podium probability.

| Task                         | Status | Output |
|------------------------------|--------|--------|
| Build simulation logic       | 🔜     | `scripts/simulate_gp.py` |
| Generate probabilistic results | 🔜   | `reports/v0_4_0/simulation/` |

---

## 🌐 Phase 7: Real-Time API

**Goal:** Deploy a FastAPI model prediction endpoint.

| Task                      | Status | Output |
|---------------------------|--------|--------|
| Create REST API in FastAPI| 🔜     | `app/api.py` |
| Deploy locally or via Docker | 🔜 | `/predict-podium` endpoint |

---

## 📊 Phase 8: Dashboard

**Goal:** Build a Streamlit dashboard for live predictions and simulation results.

| Task                     | Status | Output |
|--------------------------|--------|--------|
| UI for driver/track input| 🔜     | `dashboard/app.py` |
| Display charts + SHAP    | 🔜     | `dashboard/components/` |

---

## 🔄 Phase 9: CI/CD & Testing

**Goal:** Automate testing, linting, and deployment pipelines.

| Task                      | Status | Output |
|---------------------------|--------|--------|
| Unit tests for pipeline   | 🔜     | `tests/test_pipeline.py` |
| GitHub Actions integration| 🔜     | `.github/workflows/` |

---

## 📦 Phase 10: Packaging & Delivery

**Goal:** Bundle the model, data, and docs for release or reuse.

| Task                      | Status | Output |
|---------------------------|--------|--------|
| Export training pipeline  | 🔜     | `scripts/train_pipeline.py` |
| Package as pip module     | 🔜     | `setup.py`, `src/` structure |

---

## 📣 Phase 11: Documentation & Showcase

**Goal:** Finalize docs, record demo, publish to portfolio.

| Task                       | Status | Output |
|----------------------------|--------|--------|
| Complete README, feature docs | ✅  | `README.md`, `docs/` |
| Record demo video          | 🔜     | `assets/demo.mp4` |
| Publish to LinkedIn/Medium | 🔜     | Blog post |

---

_Last updated: April 2025_  
_Author: [Mantas](https://github.com/mantas123456)_
