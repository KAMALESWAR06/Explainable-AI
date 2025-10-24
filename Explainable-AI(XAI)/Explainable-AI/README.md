# Explainable AI for BMI-Based Diabetes Risk Prediction
**Author:** Kamaleswar Urranki · Blekinge Institute of Technology, Sweden  
**Course:** RMA 2515 Research Methodology (5.5 hp)  
**Date:** March 2025  

## Overview
This repository hosts the research artefacts for the paper **“Comparative Analysis of SHAP and LIME Methods in Explainable AI for BMI-Based Diabetes Risk Prediction.”**  
It reproduces and extends the Explainable AI pipeline comparing SHAP and LIME methods applied to the PIMA Indian Diabetes dataset.

## Aim
Evaluate how SHAP and LIME differentiate BMI’s impact on diabetes risk prediction and assess their relative stability, accuracy, and interpretability.

## Methodology
- **Data Preprocessing:** imputation, Z-score normalization, duplicate removal.
- **Modeling:** Logistic Regression & XGBoost.
- **Explainability:** SHAP (TreeExplainer) for global + local interpretation, LIME (LimeTabularExplainer) for local surrogate models.
- **Visualization:** Plotly + Dash dashboard.

## Key Findings
| Metric | SHAP | LIME |
|:--|:--:|:--:|
| Explanation Type | Global + Local | Local |
| Stability | High | Medium |
| Speed | Moderate | High |
| BMI Importance Score | 0.45 | 0.40 |

## Societal Impact
Transparent AI explanations enable clinicians to interpret model predictions confidently and identify at-risk individuals early.

## Citation
> Urranki K. (2025). *Explainable AI for BMI-Based Diabetes Risk Prediction: Comparative Analysis of SHAP and LIME.* Blekinge Institute of Technology.
