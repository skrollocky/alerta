# api_integration/tasks.py
from celery import shared_task

import requests
from celery import app
from alert.models import Full

@app.task
def fetch_and_save_api_data():
    # Здесь выполните запрос к API и сохраните данные в модели APIData
    api_url = 'http://10.254.12.81:9090/api/v1/alerts'
    data = requests.get(api_url).json()


    count = len(data["data"]["alerts"])
    number_alerts = 0
    for i in range(count):
        number = data["data"]["alerts"][number_alerts]
        state_key = number["state"]
        alertname_key = number["labels"]["alertname"]
        

        try:
            server = number["labels"]["server"]
        except :
            server = None
        try:
            description_key = number["annotations"]["description"]
        except:
            description_key = None
        try:
            data_key = number["activeAt"]
        except:
            data_key = None
        number_alerts+=1
        Full.objects.create(
            server = server,
            alertname_key = alertname_key,
            description_key = description_key,
            state_key = state_key,
            active_at = data_key
        )

        print (data_key) 
    

