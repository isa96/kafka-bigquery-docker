### Using Apache Kafka to ingest stream data from Twitter and load into Google BigQuery

Ingest stream data of Twitter recent search using Twitter API. 
The stream data will be published in JSON and the results loaded into Google BigQuery table.
Kafka server and Zookeeper will automatically run after compose up.

##### Clone this repository and enter the directory
```bash
git clone https://github.com/isa96/kafka-bigquery-docker && cd kafka-bigquery-docker
```

##### Modify "key.json" according to your Google service account credentials
```bash
nano key.json
```

##### Create Kafka stacks with Docker Compose
```bash
sudo docker compose up -d
```

##### Create Kafka topic
```bash
sudo docker exec -it kafka-server bash -c "kafka/bin/kafka-topics.sh --create --topic twitter --bootstrap-server localhost:9092"
```

##### Run Kafka producer to publish the data
```bash
sudo docker exec -it kafka-server bash -c "python3 producer.py"
```

##### Run Kafka consumer to consume the data
```bash
sudo docker exec -it kafka-server bash -c "python3 consumer.py"
```

##### Results in BigQuery
![Kafka Twitter](https://user-images.githubusercontent.com/110159876/207465787-800b74fe-6fd0-4397-b277-522ac84f54c2.jpg)

