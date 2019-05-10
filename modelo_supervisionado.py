# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IMcaHawE48417ASt4bEIBVUYAurIFZ68
"""

import pandas as pd
df = pd.read_csv('diabetes.csv')
df.head()

from google.colab import files
uploaded = files.upload()

"""**MODELO SUPERVISIONADO**

**Acurácia** = *( Vardadeiro Positivo + Verdadeiro Negativo ) / Total de Registros*
"""

# Exemplo de Função de Avaliação
def accuracy(y_real, y_pred):
  return sum(y_real == y_pred) / len(y_real)

# REGRESSÃO LOGÍSTICA -> Algoritmo de classificação

#  Importa modelo linear de classificação
from sklearn.linear_model import LogisticRegression

# Extrai features e rótulos do dataframe
X = df.drop('label', axis=1).as_matrix()
y = df['label'].as_matrix()

#  Instancia e treina modelo de classificação
model = LogisticRegression().fit(X,y)

# Prediz valores
y_predito = model.predict(X)

# Avaliando modelo
print(accuracy(y, y_predito))