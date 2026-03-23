# Capstone
This is the first notebook we will use for the preprocessing and testing the streaming and initial parts of our project pipeline.

**Goal:**
Simulate multiple banks sharing model insights without sharing raw transaction data.

**Datasets:**
1. [IEEE-CIS Fraud Detection](https://www.kaggle.com/competitions/ieee-fraud-detection)

**Current Progress:**
- Dataset loaded
- Transaction + identity tables merged
- Initial exploration started

**Next Steps:**
1. Data preprocessing
2. Feature engineering
3. Fraud detection model
4. Simulate bank-to-bank data streaming
5. Federated learning experiment

**What to do to set it up for yourself:**
1. **Run & Document:** Open the notebook and run it. **IMPORTANT:** Add text cells explaining any codes and changes made so the team can track progress without confusion.
2. **Kaggle API:** To avoid massive local downloads, we pull datasets directly into Colab.
   - Locate your `kaggle.json` file (Windows: `C:\Users\<YourName>\.kaggle`; Mac path may differ).
   - Upload this file into the first step of the notebook when prompted.
3. Run the dataset and continue working on it.

**Left out work:**
- Data preprocessing
- Model training
- Streaming simulation
- Federated learning implementation

---

## Infrastructure Setup (Kafka & Docker)
To simulate the bank-to-bank data streaming, follow these steps to configure your environment:

### Step 1: Install Docker
```bash
sudo apt update
sudo apt install docker.io docker-compose -y
```

Verify with `docker --version` and start the service:
```bash
sudo systemctl start docker && sudo systemctl enable docker
```

### Step 2: Project Configuration
1. Create a folder: `mkdir kafka-setup && cd kafka-setup`
2. Create the config file: `nano docker-compose.yml`
3. Paste the following (replace `<YOUR_VM_IP>` with the result of `hostname -I`):
```yaml
version: '3'

services:
  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181

  kafka:
    image: confluentinc/cp-kafka:latest
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://<YOUR_VM_IP>:9092
      KAFKA_LISTENERS: PLAINTEXT://0.0.0.0:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
```

### Step 3: Launch & Create Topics
1. Start Kafka: `docker-compose up -d`
2. Open the firewall: `sudo ufw allow 9092`
3. Enter the container: `docker exec -it <kafka_container_name> bash`
4. Create required topics:
```bash
kafka-topics --create --topic test-topic --bootstrap-server localhost:9092
kafka-topics --create --topic bank_1_transactions --bootstrap-server localhost:9092
kafka-topics --create --topic bank_2_transactions --bootstrap-server localhost:9092
```

### Step 4: Connection Test
- **Terminal 1 (Consumer):**
```bash
  kafka-console-consumer --topic test-topic --from-beginning --bootstrap-server localhost:9092
```
- **Terminal 2 (Producer):** Enter the container and run:
```bash
  kafka-console-producer --topic test-topic --bootstrap-server localhost:9092
```
- **Action:** Type a message in Terminal 2 — it should appear in Terminal 1.

---

## Remaining Tasks
- [ ] Data preprocessing
- [ ] Feature engineering
- [ ] Fraud detection model training
- [ ] Bank-to-bank streaming simulation
- [ ] Federated learning experiment

---

## Important Notes
- If `docker ps` is empty or after a VM restart, run `docker-compose up -d`.
- Ensure you are inside the container to run `kafka-console` commands.
 
