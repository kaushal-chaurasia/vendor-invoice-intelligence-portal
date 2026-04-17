# Vendor Invoice Intelligence System  
**Freight Cost Prediction & Invoice Risk Flagging**

---

## 📚 Table of Contents

- [Project Overview](#project-overview)
- [Business Objectives](#business-objectives)
- [Data Sources](#data-sources)
- [Exploratory Data Analysis](#eda)
- [Models Used](#models-used)
- [Evaluation Metrics](#metrics)
- [Applications](#application)
- [Project Structure](#project-structure)
- [How to Run this Project](#how-to-run-this-project)
- [Author & Contact](#author--contact)

---

## 🚀 Project Overview

This project implements an **end-to-end machine learning system** designed to support finance teams by:

1. **Predicting expected freight cost** for vendor invoices  
2. **Flagging high-risk invoices** that require manual review due to abnormal cost, freight, or operational patterns

---

## 🎯 Business Objectives

- Reduce unexpected freight cost variations  
- Identify high-risk invoices automatically  
- Minimize manual review workload for finance teams  
- Improve operational efficiency and cost control  

---

## 📂 Data Sources

- Invoice data from vendor systems  
- Purchase order data  
- Freight and cost-related attributes  
- SQLite database (`inventory.db`)

---

## 📊 Exploratory Data Analysis (EDA)

- Checked missing values and data consistency  
- Analyzed distribution of invoice amounts and freight costs  
- Identified outliers and abnormal patterns  
- Correlation analysis between cost-related features  

---

## 🤖 Models Used

### 🔹 Freight Cost Prediction
- Linear Regression ✅ (Best Model)
- Decision Tree Regressor  
- Random Forest Regressor  

### 🔹 Invoice Risk Flagging
- Logistic Regression  
- Decision Tree Classifier  
- Random Forest Classifier ✅ (Best Model)

---

## 📈 Evaluation Metrics

### Regression (Freight Prediction)
- MAE (Mean Absolute Error)  
- RMSE (Root Mean Squared Error)  
- R² Score  

### Classification (Invoice Flagging)
- Accuracy  
- Precision  
- Recall  
- F1-score  

---

## 💡 Applications

- 📦 Freight cost estimation before invoice approval  
- 🚨 Automatic detection of risky invoices  
- 💰 Cost optimization and fraud detection  
- 📊 Data-driven decision making for finance teams  

---

## 🗂️ Project Structure
Machine Learning Projects/
│
├── freight_cost_prediction/
│ ├── train.py
│ └── models/
│ └── predict_freight_model.pkl
│
├── invoice_flagging/
│ ├── data/
│ │ └── inventory.db
│ ├── models/
│ │ └── predict_flag_invoice.pkl
│ ├── data_preprocessing.py
│ ├── modeling_evaluation.py
│ └── train.py
│
├── inference/
│ ├── predict_freight.py
│ └── predict_invoice_flag.py
│
├── app.py (Streamlit UI)
└── README.md


---

## ▶️ How to Run this Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/kaushal-chaurasia/your-repo-name.git
cd your-repo-name
---
2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣ Train models

python freight_cost_prediction/train.py
python invoice_flagging/train.py

4️⃣ Run Streamlit App

streamlit run app.py

5️⃣ Run Inference (Optional)

python inference/predict_freight.py
python inference/predict_invoice_flag.py


🧑‍💻 Author & Contact

Kaushal Chaurasia
📍 India

💼 LinkedIn: (https://www.linkedin.com/in/kaushal-chaurasia-b6a609233/)
📧 Email: (kaushalchaurasia1625@gmail.com)
🐙 GitHub: (https://github.com/kaushal-chaurasia)


