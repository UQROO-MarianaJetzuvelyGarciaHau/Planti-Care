import json 
import boto3 
from decimal import Decimal 

 

# Configuración de la tabla 

dynamodb = boto3.resource('dynamodb') 
table = dynamodb.Table('LecturaESP32')  

 

# Clase para manejar números Decimal de DynamoDB en JSON 

class DecimalEncoder(json.JSONEncoder): 

    def default(self, obj): 

        if isinstance(obj, Decimal): 

            return float(obj) 

        return super(DecimalEncoder, self).default(obj) 

 

def lambda_handler(event, context): 

    try: 

        # Escaneo de la tabla 

        response = table.scan() 

        datos = response.get('Items', []) 

         

        return { 

            'statusCode': 200, 

            'headers': { 

                'Access-Control-Allow-Origin': '*', # Permitir acceso desde tu index.html 

                'Content-Type': 'application/json' 

            }, 

            'body': json.dumps(datos, cls=DecimalEncoder) 

        } 

    except Exception as e: 

        return { 

            'statusCode': 500, 

            'body': json.dumps({"error": str(e)}) 

        } 