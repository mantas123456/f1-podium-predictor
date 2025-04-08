# 📊 Baseline Results – F1 Podium Predictor (v0_1_0)

This document outlines the logic, assumptions, and performance metrics of the **baseline rule-based model** developed in Phase 1.

---

## 🧠 Rule-Based Model Logic

A simple heuristic based on **starting grid position**:

```python
if GridPosition <= 3:
    Podium = True
else:
    Podium = False
```

This assumes that top-3 qualifiers have the highest chance to finish on the podium — reflecting a historical bias in F1 race outcomes.

---

## 📦 Input Data

- Dataset: Synthetic or reference race grid positions
- Format: One row per driver per race
- Size: ~20 drivers per race × N races

---

## ✅ Evaluation Metrics

| Metric         | Value (example) | Description |
|----------------|------------------|-------------|
| Precision@3    | 0.72             | Accuracy of selecting podium drivers correctly |
| F1 Score       | 0.61             | Trade-off between precision and recall |
| Accuracy       | 0.84             | Overall prediction accuracy |
| Recall         | 0.54             | Correctly predicted podiums among actual ones |

> 🔍 *These numbers will be updated once real race data is ingested in Phase 2.*

---

## 📈 Observations

- ✅ Surprisingly strong performance using just grid position
- ❌ Fails to account for DNF, strategy, driver skill, or weather
- 🔄 No adaptation or learning — purely position-based

---

## 🗂 Output

Stored in:

```
reports/v0_1_0/baseline_metrics.json
```

Structure:

```json
{
  "precision@3": 0.72,
  "f1_score": 0.61,
  "accuracy": 0.84,
  "recall": 0.54
}
```

---

## 🧪 Limitations

- No context awareness (e.g., driver history, weather)
- No team/constructor performance data
- No feature interactions

---

## 🔭 Next Steps

| Task                        | Target Phase |
|-----------------------------|---------------|
| Ingest real historical data | Phase 2 |
| Engineer predictive features| Phase 3 |
| Train and compare ML models | Phase 3 |
| Run SHAP-based explanation  | Phase 4 |

---

_Last updated: April 2025_  
_Author: [Mantas](https://github.com/mantas123456)_
