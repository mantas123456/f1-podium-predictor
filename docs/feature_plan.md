# 🧠 Feature Plan – F1 Podium Predictor

This document outlines the full list of features to be used in the machine learning pipeline. Features will evolve through different phases of the project, starting from basic grid-based predictors to engineered and enriched metadata, simulation-based, and NLP-driven inputs.

---

## ✅ Phase 1: Baseline Features (Implemented)

| Feature Name     | Type       | Description                                |
|------------------|------------|--------------------------------------------|
| `GridPosition`   | Numerical  | Starting position on the grid              |
| `Podium`         | Binary     | Target variable (1 if finished Top 3, else 0) |

---

## 🚧 Phase 2 & 3: Raw + Engineered Features (Planned)

### 🔢 Numerical Features

| Feature                     | Description |
|-----------------------------|-------------|
| `QualifyingPosition`        | Starting grid position from Q session |
| `RaceWinsSeason`            | Total wins by the driver in current season |
| `PodiumsSeason`             | Total podiums in current season |
| `ConstructorPoints`         | Current constructor points |
| `TrackLength`               | Circuit length (in km) |
| `AveragePitTime`            | Track-specific average pit stop duration |

### 🔠 Categorical Features

| Feature                     | Description |
|-----------------------------|-------------|
| `DriverName`                | Driver ID or name |
| `ConstructorName`           | Team (e.g. Red Bull, Ferrari) |
| `TrackName`                 | Race location (e.g. Monza) |
| `WeatherCondition`          | Dry / Wet / Mixed |

> ⚙️ These will be encoded using one-hot or target encoding depending on model type.

---

## 🧪 Phase 4: Engineered Features

| Feature                             | Description |
|-------------------------------------|-------------|
| `FormRolling3`                      | Driver average finish over past 3 races |
| `TrackExperienceYears`              | Number of times driver raced this track |
| `TeamReliabilityRate`               | % of races completed by team |
| `DriverPenaltyPoints`               | Accumulated season penalty points |
| `QualifyingVsRaceDiff`             | Difference between qualifying and actual finish |
| `ConstructorTrackWinRatio`         | Team’s historical success at current track |

---

## 🧠 Phase 5+: Enriched & Simulated Features (Optional / Advanced)

| Feature                             | Description |
|-------------------------------------|-------------|
| `SimulationProbWin`                 | Probability of win from Monte Carlo simulation |
| `SimulationProbPodium`             | Probability of Top 3 from simulation |
| `NLP_Sentiment`                     | Driver/Team pre-race sentiment from press data |
| `TyreStrategyCode`                  | Encoded strategy pattern (e.g. Soft → Medium → Hard) |

---

## 📌 Notes

- **Missing Values**: Will be imputed based on season averages or domain logic.
- **Normalization**: Scaling only where needed (tree models are insensitive).
- **Feature Importance**: SHAP/LIME will be used to evaluate top contributing features.
- **Versioning**: Features will be tracked by model version (e.g. `features_v0_2_0.csv`)

---

## 🔄 Feature Version Plan

| Phase       | Version     | Feature Count | Notes |
|-------------|-------------|----------------|-------|
| Phase 1     | `v0_1_0`     | 1 basic feature | Baseline rule |
| Phase 2–3   | `v0_2_0`     | 10–15 features | Raw and preprocessed |
| Phase 4–5   | `v0_3_0+`    | 25+ features | Engineered + simulations |

---

_Last updated: April 2025_  
_Author: [Mantas](https://github.com/mantas123456)_
