#!/usr/bin/python3

from kafka import KafkaConsumer
from google.cloud import bigquery
import pandas as pd
import json

consumer = KafkaConsumer('twitter', bootstrap_servers='localhost', value_deserializer=lambda x: json.loads(x.decode('utf-8')))

client = bigquery.Client()
client.create_dataset('twitter', exists_ok=True)
dataset = client.dataset('twitter')

schema = [
    bigquery.SchemaField('id', 'INTEGER'),
    bigquery.SchemaField('text', 'STRING')
]

table_ref = bigquery.TableReference(dataset, 'search_tweets')
table = bigquery.Table(table_ref, schema=schema)
client.create_table(table, exists_ok=True)

for message in consumer:
    data = json.loads(message.value)
    for row in data:
        df = pd.json_normalize(row)
        print(df[['id', 'text']])
        client.insert_rows_from_dataframe(table, df[['id', 'text']])