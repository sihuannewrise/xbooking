from fastapi import FastAPI
from fastapi import status, HTTPException, Body

app = FastAPI()

messages_db = {0: "First post in FastAPI"}

@app.get("/messages")
async def read_messages() -> dict:
    return messages_db

@app.get("/messages/{message_id}")
async def read_message(message_id: int) -> str:
    try:
        return messages_db[message_id]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")

@app.post("/messages", status_code=status.HTTP_201_CREATED)
async def create_message(message: str = Body(...)) -> str:
    current_index = max(messages_db) + 1 if messages_db else 0
    messages_db[current_index] = message
    return "Message created!"

@app.put("/messages/{message_id}")
async def update_message(message_id: int, message: str) -> str:
    pass

@app.delete("/messages/{message_id}")
async def delete_message(message_id: int) -> str:
    pass

@app.delete("/messages")
async def delete_messages() -> str:
    pass
