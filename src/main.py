from typing import Dict
from fastapi import FastAPI
from src.message_service import MessageService
app = FastAPI()


my_servicio = MessageService()

@app.post("/api/message")
def send_message(message: Dict): 
    my_servicio.add_message(message)    
    return { "message": "Message received" }


@app.get("/api/message")
def read_messages():
    return my_servicio.get_messages()

@app.put("/api/message/{id}")
def update_message(id:str, message:Dict):
    result = my_servicio.update_message(id, message)
    if result:
        return { "message": "Message updated" }
    else:
        return { "message": "Message not found" }
    
@app.put("/api/message/{id}")
def delete_message(id:str):
    result = my_servicio.delete_message(id)
    if result:
        return { "message": "Message updated" }
    else:
        return { "message": "Message not found" }   