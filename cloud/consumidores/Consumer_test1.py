from modelRegressao import modelo
from confluent_kafka import Consumer, KafkaException
import certifi
import sys, csv, os

if __name__ == '__main__':

  topic = "fire-predict"  
  conf = {  
    'group.id': "fire-predict", 
    'session.timeout.ms': 6000,
    'auto.offset.reset': 'latest',
    'bootstrap.servers': 'cell-1.streaming.sa-saopaulo-1.oci.oraclecloud.com:9092', #usually of the form cell-1.streaming.<region>.oci.oraclecloud.com:9092  
    'security.protocol': 'SASL_SSL',  
  
    'ssl.ca.location': certifi.where(),  # from step 6 of Prerequisites section
     # optionally instead of giving path as shown above, you can do 1. pip install certifi 2. import certifi and
     # 3. 'ssl.ca.location': certifi.where()
  
    'sasl.mechanism': 'PLAIN',  
    'sasl.username': 'matheusbrant/oracleidentitycloudservice/matheusbrantgo@gmail.com/ocid1.streampool.oc1.sa-saopaulo-1.amaaaaaaz2nkdgaatblh5dkumqibancjusgaghu24vhrec4yvhacwhrbixta',  # from step 2 of Prerequisites section
    'sasl.password': '2P0vj>Fxh4ghGe.KHD:p',  # from step 7 of Prerequisites section
   }  

# Create Consumer instance
consumer = Consumer(conf)

# Subscribe to topic
consumer.subscribe([topic])

fileName = r"'../dados/dadosRegressao/dado_recebido_predict.csv'"
if os.path.isfile(fileName) == True:
    os.remove('../dados/dadosRegressao/dado_recebido_predict.csv')
else:
    print('Colhendo dados...')

# Process messages
try:
    with open('../dados/dadosRegressao/dado_recebido_predict.csv', 'w', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(["X","Y","month","day","FFMC","DMC","DC","ISI","temp","RH","wind","rain","area"])

    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())
        else:
            # Proper message
            sys.stderr.write('%% %s [%d] at offset %d with key %s:\n' %
                                (msg.topic(), msg.partition(), msg.offset(),
                                str(msg.key())))

            with open('../dados/dadosRegressao/dado_recebido_predict.csv', 'a', newline='\n') as file:

                writer = csv.writer(file)
                output=msg.value().decode('utf-8')
                strin=eval(output)
                print(strin)
                writer.writerows([strin])

                bt=1000000
                mega=1
                if mega > 5:
                    print('-> Limite de arquivo excedido <-')
                    os.remove('../dados/dadosRegressao/dado_recebido_predict.csv.csv')
                    break
                tam_mb = bt*mega
                if os.stat('../dados/dadosRegressao/dado_recebido_predict.csv').st_size >= tam_mb:
                    print('------------------------------------------- \n -> Arquivo chegou no limite especificado <-')
                    break

except KeyboardInterrupt:
    sys.stderr.write('%% Aborted by user\n')

finally:
    # Close down consumer to commit final offsets.
    consumer.close()

#aplicando os dados ao modelo
modelo(0.99, 'svr','predict')