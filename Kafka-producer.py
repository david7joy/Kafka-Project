from kafka import KafkaProducer
import time
from json import dumps

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))

for i in range(0,50):
    data = {'number':i}
    producer.send('numtest',value=data)
    time.sleep(5)

