#!/usr/bin/python3

from kafka import KafkaProducer
import requests
import json
import time

producer = KafkaProducer(bootstrap_servers='localhost', value_serializer=lambda x: json.dumps(x).encode('utf-8'))

url = 'https://api.twitter.com/2/tweets/search/recent?query=blockchain&max_results=10'
bearer_token = '[BEARER_TOKEN]'
headers = {'Authorization': f"Bearer {bearer_token}", "User-Agent": "v2SampledStreamPython"}

while True:
    response = requests.get(url, headers=headers, stream=True)
    for responses in response.iter_lines():
        json_response = json.loads(responses)
        data = json.dumps(json_response['data'], indent=1)
        print(data)
        producer.send('twitter', data)
        time.sleep(1)