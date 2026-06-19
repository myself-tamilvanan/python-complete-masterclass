# Chapter 44: Pandas Tutorial
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 10:26:21
# ============================================

try:
    import numpy as np
    import pandas as pd

    HAS_PANDAS = True
    print("pandas version:", pd.__version__)
except ImportError:
    HAS_PANDAS = False
    print("pandas not installed. Run: pip install pandas")

if HAS_PANDAS:

    # -----------------------------------------------
    # SECTION 1: Creating DataFrames
    # -----------------------------------------------

    print("\n--- Creating DataFrames ---")

    # From dict
    data = {
        "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
        "Age": [25, 30, 35, 28, 22],
        "Department": ["Engineering", "Marketing", "Engineering", "HR", "Marketing"],
        "Salary": [85000, 65000, 95000, 70000, 60000],
        "Performance": [4.5, 3.8, 4.9, 4.1, 3.5],
    }
    df = pd.DataFrame(data)
    print(df)
    print("\nShape:", df.shape)
    print("Columns:", list(df.columns))
    print("Dtypes:")
    print(df.dtypes)

    # -----------------------------------------------
    # SECTION 2: Selecting Data
    # -----------------------------------------------

    print("\n--- Selecting Data ---")

    # Single column (Series)
    print("Names:\n", df["Name"].values)

    # Multiple columns
    print("\nName & Salary:")
    print(df[["Name", "Salary"]])

    # Row by index
    print("\nRow 0:", df.iloc[0].to_dict())

    # Row by label
    print("Rows 1-3:")
    print(df.iloc[1:4])

    # -----------------------------------------------
    # SECTION 3: Filtering
    # -----------------------------------------------

    print("\n--- Filtering ---")

    # Single condition
    seniors = df[df["Age"] > 28]
    print("Age > 28:")
    print(seniors[["Name", "Age", "Salary"]])

    # Multiple conditions
    high_earners = df[(df["Salary"] > 70000) & (df["Performance"] >= 4.0)]
    print("\nHigh earners with good performance:")
    print(high_earners[["Name", "Salary", "Performance"]])

    # isin()
    eng_mkt = df[df["Department"].isin(["Engineering", "Marketing"])]
    print("\nEngineering or Marketing:")
    print(eng_mkt["Name"].values)

    # -----------------------------------------------
    # SECTION 4: GroupBy and Aggregation
    # -----------------------------------------------

    print("\n--- GroupBy ---")

    # Group by department
    dept_stats = (
        df.groupby("Department")
        .agg({"Salary": ["mean", "max", "min", "count"], "Performance": "mean"})
        .round(2)
    )
    print("Department statistics:")
    print(dept_stats)

    # -----------------------------------------------
    # SECTION 5: Adding and Modifying Columns
    # -----------------------------------------------

    print("\n--- Adding Columns ---")

    df2 = df.copy()

    # Add column
    df2["Annual_Bonus"] = df2["Salary"] * 0.10
    df2["Seniority"] = df2["Age"].apply(lambda x: "Senior" if x >= 30 else "Junior")

    print(df2[["Name", "Salary", "Annual_Bonus", "Seniority"]])

    # -----------------------------------------------
    # SECTION 6: Missing Values
    # -----------------------------------------------

    print("\n--- Missing Values ---")

    # Create dataframe with NaN values
    df_missing = pd.DataFrame(
        {"A": [1, 2, None, 4, 5], "B": [None, 2, 3, None, 5], "C": [1, 2, 3, 4, 5]}
    )
    print("Original with NaN:")
    print(df_missing)
    print("Missing counts:", df_missing.isnull().sum().to_dict())

    # Drop rows with any NaN
    clean = df_missing.dropna()
    print("\nAfter dropna():")
    print(clean)

    # Fill NaN with values
    filled = df_missing.fillna(df_missing.mean(numeric_only=True))
    print("\nAfter fillna(mean):")
    print(filled.round(2))

    # -----------------------------------------------
    # SECTION 7: Sorting and Ranking
    # -----------------------------------------------

    print("\n--- Sorting ---")

    top3 = df.sort_values("Salary", ascending=False).head(3)
    print("Top 3 earners:")
    print(top3[["Name", "Salary", "Performance"]])

    # -----------------------------------------------
    # SECTION 8: Merging DataFrames
    # -----------------------------------------------

    print("\n--- Merging ---")

    employees = pd.DataFrame({"emp_id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]})
    salaries = pd.DataFrame({"emp_id": [1, 2, 4], "salary": [85000, 65000, 90000]})

    # Inner join
    inner = pd.merge(employees, salaries, on="emp_id", how="inner")
    print("Inner join:")
    print(inner)

    # Left join
    left = pd.merge(employees, salaries, on="emp_id", how="left")
    print("\nLeft join:")
    print(left)

    # -----------------------------------------------
    # SECTION 9: Save and Load
    # -----------------------------------------------

    print("\n--- Save and Load ---")
    df.to_csv("employees.csv", index=False)
    loaded = pd.read_csv("employees.csv")
    print("Loaded from CSV:")
    print(loaded.head(3))

    import os

    os.remove("employees.csv")

print("\n" + "=" * 50)
print("Chapter 44 Complete!")
print("=" * 50)
