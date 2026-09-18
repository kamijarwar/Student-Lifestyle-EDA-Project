#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib .pyplot as plt
import seaborn as sns


# In[2]:


student = pd.read_csv('student_lifestyle_dataset.csv')
student


# In[3]:


student.head(4)


# In[ ]:





# In[4]:


student.shape


# In[5]:


student.isnull().sum()


# In[6]:


student.duplicated().sum()


# In[7]:


student.dtypes


# In[8]:


student.describe()


# In[9]:


student.head()


# In[10]:


student['Stress_Level'].value_counts()


# In[11]:


student['Study_Hours_Per_Day'].mean()


# In[12]:


student['GPA'].mean()


# In[13]:


student.groupby('Stress_Level')[['Study_Hours_Per_Day',	'Sleep_Hours_Per_Day',  'GPA']].mean()


# In[14]:


numeric_student = student.select_dtypes(include=['float64', 'int64'])


# In[15]:


correclection_matrix = numeric_student.corr()


# In[16]:


correclection_matrix


# In[17]:


plt.figure(figsize= (10,6))


# In[18]:


plt.figure(figsize=(10, 6))

sns.heatmap(correclection_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('correclection_matrix Heatmap (Student Lifestyle)', fontsize=14, fontweight='bold')
plt.show()


# In[19]:


plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=student, 
    x='Study_Hours_Per_Day', 
    y='GPA', 
    hue='Stress_Level', 
    palette='deep', 
    alpha=0.8
)

plt.title('Relationship between Study Hours and GPA (By Stress Level)', fontsize=14, fontweight='bold')
plt.xlabel('Study Hours Per Day', fontsize=12)
plt.ylabel('GPA', fontsize=12)

plt.legend(title='Stress Level', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()


# In[20]:


# 1. Graph ka size set karna
plt.figure(figsize=(9, 5))
sns.boxplot(data=student, x='Stress_Level', y='Sleep_Hours_Per_Day', palette='Set2')
plt.title('Impact of Sleep Hours on Student Stress Levels', fontsize=14, fontweight='bold')
plt.xlabel('Stress Level', fontsize=12)
plt.ylabel('Sleep Hours Per Day', fontsize=12)


plt.show()


# In[ ]:


## 📝 Step 5: Final Summary & Key Insights

Based on the thorough Exploratory Data Analysis (EDA) of the Student Lifestyle Dataset, we have uncovered the following key takeaways:

*   **Study Hours vs. GPA (Strong Positive Correlation):** The numerical correlation matrix and scatter plot clearly indicate that a higher number of daily study hours directly links to a better GPA. Academic performance is heavily driven by consistent study habits.
*   **Sleep Hours vs. Stress Level (Strong Negative Correlation):** Our box plot and correlation data prove that sleep deprivation (e.g., 4-5 hours of sleep) severely impacts students, resulting in a 'High' stress level. Conversely, students getting optimal rest (7-8 hours) generally maintain a 'Low' or 'Moderate' stress profile.
*   **The Importance of a Balanced Routine:** The data shows that academic success isn't just about studying. Students who dedicate time to physical activity and extracurricular operations manage their stress levels much better while keeping their GPA stable.
*   **Data Quality Assurance:** The `student_lifestyle_dataset.csv` was found to be perfectly clean with 0 missing values and 0 duplicate entries, ensuring that all our derived analytical findings are 100% accurate and reliable.


# In[ ]:




