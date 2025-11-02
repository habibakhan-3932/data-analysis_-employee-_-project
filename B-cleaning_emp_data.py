# FINAL EMPLOYEE DATA CLEANING 
import pandas as pd
import numpy as np

#Task 1: Load dataset
df = pd.read_csv("messy_employee_data.csv")
#Task 2: Print original columns (to inspect)
print("Original Columns:\n", df.columns.tolist(), "\n")
#Task 3: Normalize column names (remove $, spaces, brackets)
df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_")
    .str.replace(r"[\(\)\$]", "", regex=True)
)

print("Renamed Columns:\n", df.columns.tolist(), "\n")

#Now columns like 'Salary($)' become 'Salary' and 'Experience(Years)' become 'Experience_Years'
# Task 4: Drop duplicate rows
df.drop_duplicates(inplace=True)
#Task 5: Clean Age column
if 'Age' in df.columns:
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    df['Age'].fillna(round(df['Age'].mean()), inplace=True)
#Task 6: Clean Salary column (with safe check)
if 'Salary' in df.columns:
    df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
    if df['Salary'].notna().any():
        df['Salary'].fillna(df['Salary'].median(), inplace=True)
    else:
        print("Warning: Salary column has no numeric values!")
#Task 7: Standardize Gender
if 'Gender' in df.columns:
    df['Gender'] = df['Gender'].replace({
        'Male': 'M', 'Female': 'F', 'MALE': 'M', 'FEMALE': 'F'
    })
#Task 8: Clean City
if 'City' in df.columns:
    df['City'] = df['City'].astype(str).str.strip().str.title()
#Task 9: Fix Email column
if 'Email' in df.columns:
    df['Email'] = df['Email'].astype(str)
    df['Email'] = df['Email'].str.replace('mail,com', 'mail.com', regex=False)
    df['Email'] = df['Email'].str.replace('gmail,com', 'gmail.com', regex=False)
    df['Email'] = df['Email'].replace(['', 'nan', 'n/a'], np.nan)
#Task 10: Fix Joining_Date
if 'Joining_Date' in df.columns:
    df['Joining_Date'] = pd.to_datetime(df['Joining_Date'], errors='coerce')
#Task 11: Clean Department
if 'Department' in df.columns:
    df['Department'] = df['Department'].replace({
        'It': 'IT', 'Hr': 'HR', 'Fin': 'Finance', 'finance': 'Finance'
    }).fillna('Unknown')
#Task 12: Clean Experience_Years
if 'Experience_Years' in df.columns:
    df['Experience_Years'] = pd.to_numeric(df['Experience_Years'], errors='coerce')
    if df['Experience_Years'].notna().any():
        df['Experience_Years'].fillna(round(df['Experience_Years'].mean()), inplace=True)
    else:
        print("⚠️ Warning: Experience_Years column has no numeric values!")
#Task 13: Print cleaning summary
print("\n Shape After Cleaning:", df.shape)
print("\n Missing Values After Cleaning:\n", df.isnull().sum())
#Task 14: Save cleaned CSV
df.to_csv("cleaned_employee_data.csv", index=False)
print("\nCleaned data saved successfully as 'cleaned_employee_data.csv'")
