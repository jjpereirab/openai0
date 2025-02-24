import os
from openai import OpenAI
from dotenv import load_dotenv
import json 
import requests

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

model_ = "gpt-4o-mini"

def get_weather(latitude: float, longitude: float) -> str:
    print("Obteniendo clima...")
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    weather_data = response.json()

    return json.dumps(weather_data)

# bogota (latitud, longitud) = (4.7110, 74.0721)
messages_ = [
    {
        "role": "system",
        "content": "Eres un asistente que da el clima en tiempo real, puedes usar la funcion get_weather"
    },
    {
        "role": "user",
        "content": "cual es el clima de Bogotá? Tambien dime de donde estas sacando la informacion de latitud y longitud que usas para darle a la API externa en la funcion get_weather"
    }
]

functions = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Usa esta funcion para obtener informacion sobre el clima",
            "parameters": {
                "type": "object",
                "properties": {
                    "latitude": {
                        "type": "number",
                        "description": "Latitud del lugar"
                    },
                    "longitude": {
                        "type": "number",
                        "descripcion": "Longitud del lugar"
                    }
                },
                "required" : ["latitude", "longitude"]
            },
            "output": {
                "type": "string",
                "description": "Clima de la ubicacion pedida por el usuario"
            }
        }
    }
]

response = client.chat.completions.create(
    model=model_,
    messages=messages_,
    tools=functions
)

assistant_message = response.choices[0].message

print("Respuesta inicial del asistente (retorno de la API del clima)")
print(assistant_message)

if assistant_message.tool_calls:
    for tool_call in assistant_message.tool_calls:
        if tool_call.type == "function":
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)

            if function_name == "get_weather":
                print(f"El asistente está llamando a la función get_weather")
                weather_info = get_weather(
                    latitude=function_args.get("latitude"),
                    longitude=function_args.get("longitude")
                )

                messages_.append(assistant_message)
                messages_.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": function_name,
                    "content": weather_info
                })

second_response = client.chat.completions.create(
    model=model_,
    messages=messages_
)

final_reply = second_response.choices[0].message.content

print("Respuesta final del asistent")
print(final_reply)