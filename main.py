import pandas as pd

files = [
    "archive/AHS_Woman_08_Rajasthan/AHS_Woman_08_Rajasthan.csv",
    "archive/AHS_Woman_10_Bihar/AHS_Woman_10_Bihar_Part_1.csv",
    "archive/AHS_Woman_10_Bihar/AHS_Woman_10_Bihar_Part_2.csv",
    "archive/AHS_Woman_18_Assam/AHS_Woman_18_Assam.csv",
    "archive/AHS_Woman_20_Jharkhand/AHS_Woman_20_Jharkhand.csv",
    "archive/AHS_Woman_21_Odisha/AHS_Woman_21_Odisha.csv",
    "archive/AHS_Woman_22_Chhgitattisgarh/AHS_Woman_22_Chhattisgarh.csv",
    "archive/AHS_Woman_23_Madhya_Pradesh/AHS_Woman_23_Madhya_Pradesh_Part_1.csv",
    "archive/AHS_Woman_23_Madhya_Pradesh/AHS_Woman_23_Madhya_Pradesh_Part_2.csv"
]

print("Loading data...") 

# Считываем все файлы и объединяем их
dfs = [pd.read_csv(f, sep="|") for f in files]
df = pd.concat(dfs, ignore_index=True)

print("Data merged")

# Размер датасета
print("Dataset shape:", df.shape)

# Список всех колонок
print("\nColumns: ")
print(df.columns)

# Первые строки
print("\nFirst rows:")
print(df.head())

# Распределение целевой переменной
if "outcome_pregnancy" in df.columns:
    print("\nOutcome distribution:")
    print(df["outcome_pregnancy"].value_counts())

# Количество пропущенных значений
print("\nMissing values per column:")
print(df.isnull().sum())

# Типы колонок
print("\nColumn names with data types:")
print(df.dtypes)