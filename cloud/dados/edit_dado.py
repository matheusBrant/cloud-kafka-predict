import pandas as pd

csv_input = pd.read_csv('dados/dado_recebido.csv')
for i in range(len(csv_input)): 
    if csv_input['area'][i] == 0.0:
        csv_input['month'][i] = int(0)
    else:
        csv_input['month'][i] = int(1)

csv_input = csv_input.rename(columns={'month': 'fire'})
csv_input= csv_input.drop(['day'],axis=1)
#csv_input= csv_input.drop(['fire'],axis=1) #ativar para tirar o fire para test
csv_input = csv_input[['X','Y','FFMC','DMC','DC','ISI','temp','RH','wind','rain','area']] 
csv_input.to_csv('dados/forest_fire_classificacao_test.csv',  index=False)

