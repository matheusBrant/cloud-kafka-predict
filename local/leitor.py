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

my_dict = {
    "id": {
    },
    "X": {
    },
    "Y": {
    },
    "month": {
    },
    "day": {
    },
    "FFMC": {
    },
    "DMC": {
    },
    "DC": {
    },
    "ISI": {
    },
    "temp": {
    },
    "RH": {
    },
    "wind": {
    },
    "rain": {
    },
    "area": {
    },
  }

print(my_dict)

for x in range(5000):
    my_dict['id'][x] = randint(1,9)
    my_dict['X'][x] = randint(2,9)
    my_dict['Y'][x] = randint(1,9)
    my_dict['month'][x] = randint(1,9)
    my_dict['day'][x] = randint(1,9)
    my_dict['FFMC'][x] = round(random.uniform(18.7,96.2),1)
    my_dict['DMC'][x] = round(random.uniform(1.1,291.3),1)
    my_dict['DC'][x] = round(random.uniform(7.9,860.6),1)
    my_dict['ISI'][x] = round(random.uniform(0,56.10),1)
    my_dict['temp'][x] = round(random.uniform(2.2,33.30),1)
    my_dict['RH'][x] = round(random.uniform(15,100),1)
    my_dict['wind'][x] = round(random.uniform(0.4,9.4),1)
    my_dict['rain'][x] = round(random.uniform(0,6.4),1)
    my_dict['area'][x] = round(random.uniform(0,1090.84),1)

with open('data.json', 'w', encoding='utf-8') as outfile:
    json.dump(my_dict, outfile, ensure_ascii=False, indent=2)