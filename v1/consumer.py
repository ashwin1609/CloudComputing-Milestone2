from ensurepip import bootstrap
from kafka import KafkaConsumer

topicName = 'test_topic1'
consumer = KafkaConsumer(topicName,bootstrap_servers=["localhost:9093","localhost:9094","localhost:9095"])

for message in consumer:
    print("Topic= %s Value=%s" % (message.topic,message.value))

consumer.close()




