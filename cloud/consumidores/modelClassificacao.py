from matplotlib import pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from csv import reader
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")

dataset_forestfire = pd.read_csv('../dados/dadosClassificacao/forest_fire_classificacao.csv')  

target = dataset_forestfire.pop('fire')

svc = SVC(gamma="auto")

#Testando o modelo 'svc' 
cv_result = cross_val_score(svc, dataset_forestfire, target , cv=10, scoring="accuracy")

#Retorna a acurácia em porcentagem do nosso modelo
print("Acurácia com cross validation:", cv_result.mean()*100)


svc.fit(dataset_forestfire, target)
#print('\n\n',svc.predict([[1,4,91.5,130.1,807.1,7.5,21.3,35,2.2,0.0,28.19]]))
                
def predict(row):
    predict = svc.predict([row])
    if predict == 1:
        print(row, ' ---> Chance de fogo alta 🌳🔥')
    else: 
        print(row, ' ---> Chance de fogo baixa 🌳✅')