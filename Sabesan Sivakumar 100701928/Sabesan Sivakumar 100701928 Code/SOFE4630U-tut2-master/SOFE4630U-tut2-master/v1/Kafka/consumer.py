from ensurepip import bootstrap
from sys import api_version
from kafka import KafkaConsumer
consumer = KafkaConsumer('sample', api_version=(0,10,1), bootstrap_servers= ["localhost:9093" ,"localhost:9094" ,"localhost:9095"], auto_offset_reset='earliest')
print("Waiting...")
for message in consumer:
    print(message)