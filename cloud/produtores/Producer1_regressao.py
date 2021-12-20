from confluent_kafka import Producer, KafkaError  
import certifi
from csv import reader
 
if __name__ == '__main__':  
  
  topic = "fire-predict"  
  conf = {  
    'bootstrap.servers': 'cell-1.streaming.sa-saopaulo-1.oci.oraclecloud.com:9092', #usually of the form cell-1.streaming.<region>.oci.oraclecloud.com:9092  
    'security.protocol': 'SASL_SSL',  

    'ssl.ca.location': certifi.where(),  # from step 6 of Prerequisites section
        # optionally instead of giving path as shown above, you can do 1. pip install certifi 2. import certifi and
        # 3. 'ssl.ca.location': certifi.where()
    
    'sasl.mechanism': 'PLAIN',  
    'sasl.username': 'matheusbrant/oracleidentitycloudservice/matheusbrantgo@gmail.com/ocid1.streampool.oc1.sa-saopaulo-1.amaaaaaaz2nkdgaatblh5dkumqibancjusgaghu24vhrec4yvhacwhrbixta',  # from step 2 of Prerequisites section
    'sasl.password': '2P0vj>Fxh4ghGe.KHD:p',  # from step 7 of Prerequisites section
   }  
  
# Create Producer instance  
producer = Producer(**conf)  
delivered_records = 0  

# Optional per-message on_delivery handler (triggered by poll() or flush())  
# when a message has been successfully delivered or permanently failed delivery after retries.  
def acked(err, msg):  
    global delivered_records  
    """Delivery report handler called on  
        successful or failed delivery of message """  
    if err is not None:  
        print("Failed to deliver message: {}".format(err))  
    else:  
        delivered_records += 1  
        print("Produced record to topic {} partition [{}] @ offset {}".format(msg.topic(), msg.partition(), msg.offset()))  

fator=1

for n in range(fator):
    # skip first line i.e. read header first and then iterate over each row od csv as a list
    with open('../dados/dadosBasicos/forest_fire.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        # Check file as empty
        if header != None:
            # Iterate over each row after the header in the csv
            i=1
            for row in csv_reader:
                # row variable is a list that represents a row in csv
                record_key = "Vindo do original " + str(i)
                i=i+1  
                record_value = str(row)
                print("Producing record: {}\t{}".format(record_key, record_value))  
                producer.produce(topic, key=record_key, value=record_value, on_delivery=acked)  
                # p.poll() serves delivery reports (on_delivery) from previous produce() calls.  
                producer.poll(0) 
     
producer.flush()  
print("{} messages were produced to topic {}!".format(delivered_records, topic))
