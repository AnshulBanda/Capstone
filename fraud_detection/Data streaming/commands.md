## Command to stop and run docker
```bash
docker-compose down -v
docker-compose up -d
```

## Verify config
```bash
docker exec -it <kafka-container> env | grep ADVERTISED

# To find <kafka-container> run docker ps and paste the kafka container name
```

## Create Topic (Sia)
```bash
docker exec -it <kafka-container> \
kafka-topics --create \
--topic bank_1_transactions \
--bootstrap-server 172.22.19.172:9092 \
--partitions 1 \
--replication-factor 1
# do the same docker ps stuff

```

## Ping sia network
```bash
ping 172.22.19.172
```


## Start consumer (shuchika)
```bash
docker exec -it <kafka-container> \
kafka-console-consumer \
--bootstrap-server 172.22.19.172:9092 \
--topic bank_1_transactions \
--from-beginning
```

## start streaming
```bash
python producer.py
```
