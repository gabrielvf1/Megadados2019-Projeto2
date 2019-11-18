import json
from time import sleep

from kafka import KafkaConsumer

if __name__ == '__main__':
    parsed_topic_name = 'parsed_recipes'
    # Notify if a recipe has more than 200 calories
    calories_threshold = int(input("User input: \nquantas calorias no maximo\n "))
    calories_group= str(calories_threshold) + "_group"
    
    while True:
        consumer = KafkaConsumer(parsed_topic_name, auto_offset_reset='earliest',
                             bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000,group_id=calories_group)
        for msg in consumer:
            try:
                record = json.loads(msg.value)
                calories = int(record['calories'])
                title = record['title']

                if calories > calories_threshold:
                    print('Alert: {} calories count is {}'.format(title, calories))
            except:
                pass

        consumer.close()


    

