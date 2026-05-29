import json 
import boto3 
import time 

 

dynamodb = boto3.resource('dynamodb') 
table = dynamodb.Table('LecturaESP32') 

 

def lambda_handler(event, context): 

    try: 

        dev_id = str(event.get('device_id', 'ESP32_SENSORS')) 

        # Extraemos ambos valores del nuevo JSON 

        temp = event.get('temperatura', 0) 

        hum = event.get('humedad_suelo', 0) 

        ts = int(time.time()) 

         

        table.put_item( 

            Item={ 

                'id_dispositivo': dev_id, 

                'timestamp': ts, 

                'temperatura': temp, 

                'humedad_suelo': hum 

            } 

        ) 

        return {'statusCode': 200, 'body': 'Guardado con éxito'} 

    except Exception as e: 

        print(f"Error: {str(e)}") 

        return {'statusCode': 500} 