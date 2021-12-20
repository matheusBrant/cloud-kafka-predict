from confluent_kafka import Producer
from csv import reader
import certifi
 
if __name__ == '__main__':  
  
  topic = "fire-predict"  
  conf = {  
    'bootstrap.servers': 'cell-1.streaming.sa-saopaulo-1.oci.oraclecloud.com:9092', 
    'security.protocol': 'SASL_SSL',  
    'ssl.ca.location': certifi.where(),   
    'sasl.mechanism': 'PLAIN',  
    'sasl.username': 'matheusbrant/oracleidentitycloudservice/matheusbrantgo@gmail.com/ocid1.streampool.oc1.sa-saopaulo-1.amaaaaaaz2nkdgaatblh5dkumqibancjusgaghu24vhrec4yvhacwhrbixta',  # from step 2 of Prerequisites section
    'sasl.password': '2P0vj>Fxh4ghGe.KHD:p',  
   }  
  
producer = Producer(**conf)  
delivered_records = 0  

def acked(err, msg):  
    global delivered_records  
      
    if err is not None:  
        print("Falha ao entregar a mensagem: {}".format(err))  
    else:  
        delivered_records += 1  
        print("Produtor gravou no tópico '{}', partição [{}] e @ offset {}".format(msg.topic(), msg.partition(), msg.offset()))  

fator=1

for n in range(fator):
    with open('../dados/dadosBasicos/forest_fire.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            i=1
            for row in csv_reader:
                record_key = "producer2 -> key: " + str(i)
                i=i+1  
                record_value = str(row)
                print("Produtor gravando: {}\t{}".format(record_key, record_value))  
                producer.produce(topic, key=record_key, value=record_value, on_delivery=acked)  
                producer.poll(0) 
     
producer.flush()  
print("✅ {} mensagens foram produzidas no tópico '{}'!".format(delivered_records, topic))