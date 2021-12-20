import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from csv import reader
import warnings

warnings.filterwarnings("ignore")

dataset_forestfire = pd.read_csv('dados/dadosClassificacao/forest_fire_classificacao.csv')  
#dataset_forestfire=dataset_forestfire.drop(['area'],axis=1) 

target = dataset_forestfire.pop('fire')

svc = SVC(gamma="auto")

#Testando o modelo 'svc' na nossa base 'iris'
cv_result = cross_val_score(svc, dataset_forestfire, target , cv=10, scoring="accuracy")

#Retorna a acurácia em porcentagem do nosso modelo
print("Acurácia com cross validation:", cv_result.mean()*100)


svc.fit(dataset_forestfire, target)
#print('\n\n',svc.predict([[6,5,63.5,70.8,665.3,0.8,17.0,72,6.7,0.0]]))
                
def predict(row):
    predict = svc.predict([row])
    if predict == 1:
        print(row, ' ---> Chance de fogo alta 🌳🔥')
    else: 
        print(row, ' ---> Chance de fogo baixa 🌳✅')