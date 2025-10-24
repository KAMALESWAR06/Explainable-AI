# 🧠 Explainable AI for BMI-Based Diabetes Risk Prediction
**Author:** Kamaleswar Urranki  
**Affiliation:** Blekinge Institute of Technology · Karlskrona, Sweden  
**Course Context:** RMA 2515 — Research Methodology (5.5 hp)  
**Timeline:** January – March 2025  

---

## 🌍 Project Overview
This research repository documents the complete experimental pipeline and analysis behind my study  
**“Comparative Analysis of SHAP and LIME Methods in Explainable AI for BMI-Based Diabetes Risk Prediction.”**

In an age where *trustworthy AI* defines the next frontier of healthcare analytics, this project bridges the gap between *black-box prediction* and *clinical transparency*.  
The work explores **how Body Mass Index (BMI)** — a key physiological indicator — influences diabetes risk, and how **Explainable AI (XAI)** frameworks like **SHAP** and **LIME** can transform opaque predictions into interpretable medical insights.

> 🔍 In simple terms: the system doesn’t just predict whether a person might have diabetes — it also tells *why*.

---

## 🎯 Research Vision
> To build an interpretable, deployable, and reproducible **AI-driven decision support system** that empowers clinicians with transparent risk explanations — bridging data science with human-centric healthcare.

**Core Question:**  
*How do SHAP and LIME differ in explaining BMI’s influence on diabetes prediction models, and what implications does that have for clinical trust and real-time deployment?*

---

## ⚙️ Methodology Pipeline

### 🩺 1. Data Foundation  
Dataset: **PIMA Indian Diabetes Dataset** (Kaggle)  
Structured health records containing 8 biomedical features, including BMI, glucose, insulin, and blood pressure.

**Key Preprocessing Steps**
- Imputation for missing BMI and glucose values.  
- Outlier removal via **Z-score normalization**.  
- Duplicate pruning and consistent label encoding.  
- Feature correlation using **Pearson’s r** for interpretability focus.

---

### 🤖 2. Model Engineering
**Baseline Learners**
- Logistic Regression – transparent and linearly interpretable.
- XGBoost – nonlinear gradient-boosted ensemble for higher accuracy.

**Performance Metrics**
- Accuracy, Precision, Recall, F1, and AUC.
- Validation split (70 / 15 / 15) ensures reproducibility.

---

### 🧩 3. Explainability Layer
#### 🟩 SHAP (Shapley Additive Explanations)
- Theoretical backbone: cooperative game theory.  
- Computes *global + local* attributions.  
- Provides consistent fairness-based credit assignment for each feature.  
- Visualization: summary plots, dependence plots, and force plots.

#### 🟨 LIME (Local Interpretable Model-agnostic Explanations)
- Builds local surrogate models to mimic the black-box behavior around individual samples.  
- Provides *case-by-case* reasoning for clinicians reviewing patient-specific predictions.  
- Visualization: local bar-chart attribution maps.

---

### 📊 4. Visualization & Interaction
A lightweight **Plotly + Dash web dashboard** provides:
- Real-time feature importance comparisons between SHAP and LIME.  
- Interactive sliders for exploring BMI thresholds and their influence on risk probability.  
- Exportable charts for academic presentation or clinical evaluation.

*(Live demo hosted on localhost:8050 when run via `python dashboard/app.py`)*

---

## 🔬 Experimental Highlights

| Metric | SHAP | LIME |
|:--|:--:|:--:|
| Explanation Type | Global + Local | Local-only |
| Stability | ✅ High (consistent across runs) | ⚠️ Medium (perturbation-sensitive) |
| Speed | ⚙️ Moderate | ⚡ High |
| Clinical Interpretability | Robust & Quantitative | Intuitive but case-specific |
| BMI Importance Score | **0.45** | **0.40** |

🧩 **Outcome:**  
BMI consistently emerges as the most decisive feature influencing diabetes risk, with SHAP providing the mathematically rigorous justification, while LIME highlights individual nuances — together forming a holistic interpretability framework.

---

## 🌐 System Architecture Snapshot


