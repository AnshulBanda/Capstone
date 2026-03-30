from kafka import KafkaProducer
import csv
import json
import time

producer = KafkaProducer(
    bootstrap_servers="172.22.19.172:9092",
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

with open("cleaned_elliptic.csv", "r") as file:
    reader = csv.DictReader(file)

    for i, row in enumerate(reader):
        producer.send("bank_1_transactions", value=row)
        print("Sent:", row)

        time.sleep(0.05)

        if i > 50:  # limit for testing
            break

producer.flush()