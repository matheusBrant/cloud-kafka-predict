from kafka import KafkaProducer, KafkaConsumer, KafkaClient
import json
import random
from time import sleep
from datetime import datetime
import pandas as pd
import numpy as np
import time
import random
from random import randint

a='data/forest_fire.json'
b='data/forest_fire2x.json'
c='data/forest_fire4x.json'
d='data/forest_fire8x.json'
e='data/forest_fire32x.csv'
f='../cloud/dados/dado_recebido.csv'

#se for e troca pra csv
df = pd.read_csv(f)
print(df)
js = df.to_json()
obj = json.loads(js)

'''with open('obj.json', 'w', encoding='utf-8') as outfile:
    json.dump(obj, outfile, ensure_ascii=False, indent=2)'''

from csv import reader
# skip first line i.e. read header first and then iterate over each row od csv as a list
with open(f, 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Check file as empty
    if header != None:
        # Iterate over each row after the header in the csv
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            print(row)

# Create an instance of the Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                            value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Call the producer.send method with a producer-record
print("Ctrl+c to Stop")
i=1
while True:
    producer.send('python-topic-2', js)
    i+=1
    time.sleep(10)
    print("Valores enviados")
    
# sudo docker-compose up -d
# sudo docker-compose ps
# -- create topic --
# sudo docker-compose exec kafka \
# kafka-topics --create --topic python-topic-1 --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092
"""virtualenv -p python3 .env3
source .env3/bin/activate"""
#cd Área\ de\ Trabalho/vsFiles/estudoKafka/cofluent-kafka-oracle/local/