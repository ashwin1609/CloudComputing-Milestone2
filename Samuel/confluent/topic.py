from confluent_kafka.admin import AdminClient, NewTopic


admin_client = AdminClient({
    "bootstrap.servers": ['localhost:9093', 'localhost:9094', 'localhost:9095']
})

topic_list = []
topic_list.append(NewTopic("Users", 3, 3))
admin_client.create_topics(topic_list)