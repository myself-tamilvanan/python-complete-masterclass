# Chapter 44: Pandas Tutorial

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 10:26:21

## Overview
Pandas is the most important Python library for data analysis and manipulation. It provides DataFrame (2D table) and Series (1D array) structures with SQL-like operations.

## Installation
```bash
pip install pandas
```

## Core Data Structures
| Structure  | Description                           |
|------------|---------------------------------------|
| Series     | 1D labeled array                      |
| DataFrame  | 2D labeled table (rows and columns)   |
| Index      | Label for rows/columns                |

## Key Operations
| Operation      | Method                            |
|----------------|-----------------------------------|
| Read CSV       | pd.read_csv("file.csv")           |
| View data      | df.head(), df.tail(), df.info()   |
| Select cols    | df["col"], df[["c1","c2"]]        |
| Filter rows    | df[df["age"] > 25]                |
| Group by       | df.groupby("col").sum()           |
| Sort           | df.sort_values("col")             |
| Missing values | df.dropna(), df.fillna(0)         |
| Apply function | df["col"].apply(func)             |
| Merge          | pd.merge(df1, df2, on="key")      |

## Learning Outcomes
- Create and manipulate DataFrames
- Filter, sort, and group data
- Handle missing values
- Merge and join DataFrames
- Read and write CSV files