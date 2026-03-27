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

## Data Streaming 

## Setup Guide

Follow these steps to configure your environment and install the necessary dependencies for the data streaming pipeline.

### Step 1: System Update and Kafka Installation
First, ensure your system packages are up to date and download the Kafka binaries.

```bash
# Update system packages
sudo apt update

# Download Kafka 3.7.0
wget [https://downloads.apache.org/kafka/3.7.0/kafka_2.13-3.7.0.tgz](https://downloads.apache.org/kafka/3.7.0/kafka_2.13-3.7.0.tgz)

# Extract the archive
tar -xzf kafka_2.13-3.7.0.tgz

# Navigate to the Kafka directory
cd kafka_2.13-3.7.0
```
### Step 2: Containerization Setup
Install Docker and Docker Compose to manage streaming services.

```bash
# Install Docker and Docker Compose
sudo apt install docker.io docker-compose -y

# Start and enable the Docker service
sudo systemctl start docker
sudo systemctl enable docker
```

### Step 3: Python Environment
Install Python and the tools required to manage virtual environments and packages.
```bash
# Install Python, venv, and pip
sudo apt install python3 python3-venv python3-pip -y
```

## Create Project Folder and Create Project Folder:

Follow these steps to set up the directory structure and the Docker environment for the streaming pipeline.

### Step 1: Create Project Directory
Create a dedicated folder for the Kafka setup and navigate into it.

```bash
mkdir kafka-setup
cd kafka-setup
```
### Step 2: Configure Docker Compose
Create a docker-compose.yml file and define the Zookeeper and Kafka services.

```bash
# Create and open the file
nano docker-compose.yml
```

Paste the following configuration into the file:

```bash
version: '3'

services:
  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181

  kafka:
    image: confluentinc/cp-kafka:7.5.0
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_LISTENERS: PLAINTEXT://0.0.0.0:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
```

### Step 3: Launch Services
Start the containers in detached mode.

```bash
docker-compose up -d
```

### Step 4: Verify Installation
Check the status of the running containers to ensure both Zookeeper and Kafka are healthy.

```bash
docker ps
```



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
 
