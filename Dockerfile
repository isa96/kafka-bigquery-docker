FROM debian:latest
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
WORKDIR /root
RUN apt update -y
RUN apt upgrade -y
RUN apt install python3-pip -y
RUN apt install default-jdk -y
RUN apt install wget -y
RUN wget https://dlcdn.apache.org/kafka/3.3.1/kafka_2.13-3.3.1.tgz
RUN tar xvf kafka_2.13-3.3.1.tgz
RUN mv kafka_2.13-3.3.1 kafka && rm kafka_2.13-3.3.1.tgz
RUN pip install kafka-python
RUN pip install requests
RUN pip install pandas
RUN pip install google-cloud-bigquery
RUN pip install pyarrow