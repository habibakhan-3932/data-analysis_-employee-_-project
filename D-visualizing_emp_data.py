#EMPLOYEE DATA VISUALIZATION PROJECT
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Task 1: Load the cleaned dataset
df = pd.read_csv("cleaned_employee_data.csv")
#Task 2: Basic info
print("Data loaded successfully!")
print(df.head())

#Visualization 1: Gender Distribution
if 'Gender' in df.columns:
    gender_count = df['Gender'].value_counts()
    plt.figure(figsize=(6, 5))
    plt.bar(gender_count.index, gender_count.values)
    plt.title("Gender Distribution of Employees")
    plt.xlabel("Gender")
    plt.ylabel("Number of Employees")
    plt.tight_layout()
    plt.show()

#Visualization 2: Average Salary by Department
if 'Department' in df.columns and 'Salary' in df.columns:
    avg_salary = df.groupby('Department')['Salary'].mean()
    plt.figure(figsize=(8, 5))
    plt.bar(avg_salary.index, avg_salary.values)
    plt.title("Average Salary by Department")
    plt.xlabel("Department")
    plt.ylabel("Average Salary")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#Visualization 3: Age Distribution
if 'Age' in df.columns:
    plt.figure(figsize=(7, 5))
    plt.hist(df['Age'], bins=10, edgecolor='black')
    plt.title("Employee Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Number of Employees")
    plt.tight_layout()
    plt.show()

#Visualization 4: Experience vs Salary
if 'Experience_Years' in df.columns and 'Salary' in df.columns:
    x = df['Experience_Years'].to_numpy()
    y = df['Salary'].to_numpy()
    plt.figure(figsize=(7, 5))
    plt.scatter(x, y)
    plt.title("Experience vs Salary")
    plt.xlabel("Experience (Years)")
    plt.ylabel("Salary")
    plt.tight_layout()
    plt.show()
#Visualization 5: Department Count Pie Chart
if 'Department' in df.columns:
    dept_count = df['Department'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(dept_count.values, labels=dept_count.index, autopct='%1.1f%%', startangle=90)
    plt.title("Employee Distribution by Department")
    plt.tight_layout()
    plt.show()
print("\n Visualization completed successfully!")
