from ensurepip import bootstrap
from kafka import KafkaProducer
#import sys

topicName = 'test_topic1'
kafkaServer = ["localhost:9093","localhost:9094","localhost:9095"]
#msg = sys.argv[2]

producer = KafkaProducer(bootstrap_servers=["localhost:9093","localhost:9094","localhost:9095"])

producer.send(topicName, b'Test Server !!!')
#producer.send(topicName, msg)
print("Success")
#print(msg)
producer.flush()

