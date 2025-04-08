# 🧩 Feature Plan – F1 Podium Predictor

This document outlines the proposed input features for the F1 Podium Prediction model, including their types, sources, whether they require engineering, and notes for preprocessing or transformation.

---

## 🔢 Numerical Features

| Feature                     | Type      | Source         | Engineering Required | Notes                             |
|----------------------------|-----------|----------------|----------------------|------------------------------------|
| Grid Position              | Numeric   | Race data      | No                   | Strong baseline predictor          |
| Driver Championship Points | Numeric   | Standing table | No                   | Reflects current form              |
| Constructor Points         | Numeric   | Standing table | No                   | Team strength indicator            |
| Driver Recent Form (5R Avg)| Numeric   | Historical     | Yes                  | Rolling avg. finish position       |
| Team Average Finish (5R)   | Numeric   | Historical     | Yes                  | Team trend analysis                |

---

## 🔠 Categorical Features

| Feature         | Type        | Source       | Engineering Required | Notes                          |
|----------------|-------------|--------------|----------------------|---------------------------------|
| Driver Name     | Categorical | Race Results | Yes                  | Encode or embed                |
| Team Name       | Categorical | Race Results | Yes                  | Combine with track or driver   |
| Track Name      | Categorical | Metadata     | Yes                  | Add track type or location     |
| Tyre Compound   | Categorical | Optional     | Optional             | May add in v2.0                |
| Weather (Dry/Wet)| Binary     | Weather API  | Optional             | Encode as 0/1 if included      |

---

## 🧠 Contextual & Engineered Features

| Feature                        | Type      | Source         | Engineering Required | Notes                                 |
|-------------------------------|-----------|----------------|----------------------|----------------------------------------|
| Track Overtaking Score        | Numeric   | Track metadata | Yes                  | Quantifies overtaking difficulty       |
| Team Reliability Index        | Numeric   | Historical     | Yes                  | Based on DNFs, penalized races         |
| Penalty Flag (Driver)         | Binary    | Race history   | Yes                  | True if prior race had time/grid penalty |
| Safety Car History (Track)    | Numeric   | Race metadata  | Yes                  | Avg. SC count per GP                   |

---

## ⏳ Temporal Features (Optional)

| Feature                  | Type      | Source         | Engineering Required | Notes                             |
|-------------------------|-----------|----------------|----------------------|------------------------------------|
| Race Number in Season   | Numeric   | Calendar       | No                   | Early/late season variation        |
| Previous Year Podium    | Categorical | History       | Yes                  | Team/driver-track affinity         |

---

## 💡 Notes

- Start with essential features and iteratively expand
- Encode categorical variables with one-hot or embeddings
- Normalize or scale numerical features (if needed)
- Use SHAP importance to rank feature value post-training

---

