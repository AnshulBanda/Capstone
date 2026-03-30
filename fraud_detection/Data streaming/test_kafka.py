from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="172.22.19.172:9092")

producer.send("bank_1_transactions", b"hello-test")
producer.flush()

print("✅ sent")