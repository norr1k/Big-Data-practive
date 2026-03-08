import pandas as pd
# Подключаем библиотеку pandas для работы с таблицами (DataFrame)
file3 = "archive/AHS_Woman_08_Rajasthan/AHS_Woman_08_Rajasthan.csv"

file4 = "archive/AHS_Woman_10_Bihar/AHS_Woman_10_Bihar_Part_1.csv"
file5 = "archive/AHS_Woman_10_Bihar/AHS_Woman_10_Bihar_Part_2.csv"

file6 = "archive/AHS_Woman_18_Assam/AHS_Woman_18_Assam.csv"

file7 = "archive/AHS_Woman_20_Jharkhand/AHS_Woman_20_Jharkhand.csv"

file8 = "archive/AHS_Woman_21_Odisha/AHS_Woman_21_Odisha.csv"

file9 = "archive/AHS_Woman_22_Chhattisgarh/AHS_Woman_22_Chhattisgarh.csv"

file1 = "archive/AHS_Woman_23_Madhya_Pradesh/AHS_Woman_23_Madhya_Pradesh_Part_1.csv"
file2 = "archive/AHS_Woman_23_Madhya_Pradesh/AHS_Woman_23_Madhya_Pradesh_Part_2.csv"

# Пути к двум CSV файлам с данными.
# Каждый файл содержит часть данных по одному штату (Madhya Pradesh).

print("Loading data...! ! ! ")
print("Говно ")
print("Залупа ")
# Сообщение в консоль, чтобы понимать на каком этапе программа

df1 = pd.read_csv(file1, sep="|", nrows=10000)
df2 = pd.read_csv(file2, sep="|", nrows=10000)
df3 = pd.read_csv(file3, sep="|", nrows=10000)
df4 = pd.read_csv(file4, sep="|", nrows=10000)
df5 = pd.read_csv(file5, sep="|", nrows=10000)
df6 = pd.read_csv(file6, sep="|", nrows=10000)
df7 = pd.read_csv(file7, sep="|", nrows=10000)
df8 = pd.read_csv(file8, sep="|", nrows=10000)
df9 = pd.read_csv(file9, sep="|", nrows=10000)

# Читаем CSV файлы в DataFrame
# sep="|" означает, что в файле используется разделитель |
# nrows=50000 — читаем только первые 50 000 строк (для тестирования,
# чтобы не загружать сразу весь огромный датасет)

print("Files loaded")
# Сообщение о том, что файлы успешно прочитаны

df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9], ignore_index=True)
# Объединяем два DataFrame в один
# ignore_index=True — создаёт новый общий индекс
# (иначе индексы из двух таблиц могли бы повторяться)

print("Data merged")
# Сообщение о завершении объединения

print("Dataset shape:")
print(df.shape)
# Показывает размер таблицы:
# (количество строк, количество столбцов)
# например: (100000, 201)

print("\nColumns:")
print(df.columns)
# Выводит список всех названий столбцов
# Это помогает понять, какие признаки есть в датасете

print("\nFirst rows:")
print(df.head())
# Показывает первые 5 строк таблицы
# Нужно для визуальной проверки данных

print(df["outcome_pregnancy"].value_counts())
# Считает количество значений в целевой переменной
# outcome_pregnancy — результат беременности
# Это позволяет увидеть распределение классов

print(df.isnull().sum())
# Считает количество пропущенных значений (NaN)
# для каждого столбца
# Это нужно для понимания качества данных