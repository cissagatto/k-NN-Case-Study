# ELAINE CECÍLIA GATTO
# APRENDIZAGEM BASEADA EM INSTÃNCIA
# k-NN

import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

nome_do_arquivo = "/home/biomal/Documentos/MACHINE LEARNING COM PYTHON/Bases de dados/credit_data.csv"
dados = pd.read_csv(nome_do_arquivo)

dados.shape

X_credit =  dados.iloc[:,0:3]
Y_credit = dados.iloc[:,4]

X_train, X_test, y_train, y_test = train_test_split(X_credit, Y_credit, train_size=0.7, test_size=0.3, random_state=0)

print(len(X_train), len(y_train))
print(len(X_test), len(y_test))




