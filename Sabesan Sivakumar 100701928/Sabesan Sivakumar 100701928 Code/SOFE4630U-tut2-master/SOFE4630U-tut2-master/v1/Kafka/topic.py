from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers = ["localhost:9093" ,"localhost:9094" ,"localhost:9095"],
    client_id='test'
)

topic_list = []
topic_list.append(NewTopic(name='sample', num_partitions=1, replication_factor=1))
admin_client.create_topics(new_topics = topic_list, validate_only=False)
