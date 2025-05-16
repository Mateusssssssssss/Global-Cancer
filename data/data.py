import pandas as pd

dados = pd.read_csv('data/global_cancer_patients_2015_2024.csv')
print(dados.head())
print(dados.columns)
print(dados.describe())