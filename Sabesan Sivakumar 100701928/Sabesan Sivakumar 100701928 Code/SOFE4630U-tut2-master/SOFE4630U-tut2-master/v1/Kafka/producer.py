from kafka import KafkaProducer
from kafka.errors import KafkaError
print("start")
producer = KafkaProducer(bootstrap_servers = ["localhost:9093" ,"localhost:9094" ,"localhost:9095"],api_version=(0,10,1))
print("Currently Working")
producer.send('sample', 'Hello')
print("sent")
producer.flush()
print("flushed")