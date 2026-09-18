# Student-Lifestyle-EDA-Project
Exploratory Data Analysis (EDA) on Student Lifestyle Dataset using Pandas, NumPy, Matplotlib, and Seaborn.
# 📊 Student Lifestyle Dataset - Exploratory Data Analysis (EDA)

![Python](https://shields.io)
![Pandas](https://shields.io)
![Seaborn](https://shields.io)
![License](https://shields.io)

## 📌 Project Overview
This project delivers a comprehensive and detailed Exploratory Data Analysis (EDA) on the Student Lifestyle Dataset. The primary goal of this research is to investigate how a student's daily lifestyle choices—such as study hours, sleep duration, social hours, and physical activity—impact their academic performance (GPA) and psychological well-being (Stress Level). 

By analyzing records of 2,000 students, we uncover critical behavioral trends and core correlations driving student success.

---

## 🛠️ Tech Stack & Core Libraries
The following data science libraries were utilized to build this analytical pipeline:
*   **Pandas:** For data ingestion, programmatic inspection, descriptive statistics, and multi-variable grouping operations.
*   **NumPy:** For high-performance numerical calculations and array processing operations.
*   **Matplotlib:** For low-level plotting controls, figure layout management, and custom visual scaling.
*   **Seaborn:** For high-level statistical representations, default aesthetics, and advanced multi-axis plotting themes.

---

## 🚀 Key Implementation Steps
This project strictly adheres to the standard data science workflow:

1.  **Data Ingestion & Structural Check:** Loaded the dataset using `pd.read_csv()` and verified structural integrity via `.shape` and `.info()`.
2.  **Data Quality Assurance (Cleaning):** Run `.isnull().sum()` and `.duplicated().sum()` check vectors. The dataset was validated as 100% clean with zero missing values or duplicate records.
3.  **Descriptive Statistical Analysis:** Generated standard metrics using `.describe()` and applied targeted multi-variable grouping operations (`.groupby()`).
4.  **Statistical Visualizations (EDA):**
    *   **Univariate Analysis:** Evaluated the overall distribution of student GPAs using `sns.histplot` overlaid with a KDE curve.
    *   **Bivariate Analysis:** Plotted `Study_Hours_Per_Day` against `GPA` via `sns.scatterplot`, color-mapped (`hue`) by `Stress_Level`.
    *   **Categorical Spread:** Analyzed the specific relationship between sleep distribution and stress using `sns.boxplot`.
    *   **Multivariate Analysis:** Constructed a comprehensive Correlation Matrix using `sns.heatmap` to capture all linear relationships at a glance.

---

## 📈 Key Insights & Data Interpretations

*   **Academic Performance Driver (Study Hours vs. GPA):** The numerical correlation matrix and scatter plot clearly indicate that a higher number of daily study hours directly links to a better GPA. Academic performance is heavily driven by consistent study habits.
*   **The Stress Threshold (Sleep Hours vs. Stress Level):** The box plot highlights a critical insight: sleep-deprived students (averaging 4-5 hours of sleep) severely impact students, resulting in a 'High' stress level. Conversely, students getting optimal rest (7-8 hours) generally maintain a 'Low' or 'Moderate' stress profile.
*   **The Importance of a Balanced Routine:** The data shows that academic success isn't just about studying. Students who dedicate time to physical activity and extracurricular operations manage their stress levels much better while keeping their GPA stable.
*   **Data Quality Assurance:** The `student_lifestyle_dataset.csv` was found to be perfectly clean with 0 missing values and 0 duplicate entries, ensuring that all our derived analytical findings are 100% accurate and reliable.

---

## 💻 How to Clone and Run the Environment

### 1. Clone the Repository:
```bash
git clone https://github.com
cd Student-Lifestyle-EDA
```

### 2. Install Dependencies:
```bash
pip install pandas numpy matplotlib seaborn
```

### 3. Launch Notebook:
Open your preferred environment (Jupyter Notebook or VS Code) and run the `Student-Lifestyle-EDA.ipynb` cells sequentially. Ensure the `student_lifestyle_dataset.csv` file remains in your root project directory.

---

## 👤 Author
*   **Name:** Kamran Ali Jarwar
*   **Role:** Machine Learning Engineer / Data Analyst
*   **LinkedIn:** [in/kamran-ali-jarwar-1860a1391](https://linkedin.com)
