🌱 Planti-Care 🌱

Sistema IoT para el monitoreo de temperatura y humedad en huertos utilizando AWS.

# Descripción

Planti-Care permite recopilar datos ambientales mediante sensores conectados a un ESP32, enviarlos a la nube y visualizarlos en una aplicación web de forma sencilla e intuitiva.


# 🌐 Aplicación Web

**Enlace de acceso:**

[Agregar URL de la aplicación]


# Arquitectura

ESP32 → AWS IoT Core → AWS Lambda → DynamoDB
                                   ↓
                              API Gateway
                                   ↓
                             Aplicación Web
                                Amazon S3

# Servicios AWS implemenatados

- AWS IoT Core
- AWS Lambda
- Amazon DynamoDB
- Amazon API Gateway
- Amazon S3
- Amazon CloudWatch

# Hardware utilizado

- ESP32-S3
- Sensores (DHT22)

# 👥 Integrantes

- Mariana Garcia
- Jessica Diaz
- Luis Ponce
- Javier Macías
- Josué Pavón

Proyecto académico desarrollado con fines educativos.
