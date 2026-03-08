import pandas as pd

file1 = "../archive/AHS_Woman_23_Madhya_Pradesh/AHS_Woman_23_Madhya_Pradesh_Part_1.csv"
file2 = "../archive/AHS_Woman_23_Madhya_Pradesh/AHS_Woman_23_Madhya_Pradesh_Part_2.csv"

print("Loading data...")

df1 = pd.read_csv(file1, sep="|", nrows=50000)
df2 = pd.read_csv(file2, sep="|", nrows=50000)
print("чето там: ")
print(df1.head())
print("чето там: ")
print(df2.head())

print("Files loaded")

df = pd.concat([df2, df1], ignore_index=True)

print("Data merged")

print("Dataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst rows:")
print(df.head())

print(df["outcome_pregnancy"].value_counts())

print(df.isnull().sum())