import json
import datetime

def lambda_handler(event, context):
    # Obtener parámetros de la URL
    nombre = event.get("queryStringParameters", {}).get("nombre", "Invitado")
    email = event.get("queryStringParameters", {}).get("email", "No proporcionado")

    # Generar respuesta JSON
    respuesta = {
        "mensaje": f"¡Hola {nombre}! Hemos recibido tu email: {email}",
        "datos_recibidos": {
            "nombre": nombre,
            "email": email
        },
        "estatus": "Éxito",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"  # Permite llamadas desde el frontend
        },
        "body": json.dumps(respuesta)
    }

