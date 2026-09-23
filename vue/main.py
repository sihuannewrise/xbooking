from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Messages CRUD")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class MessageCreate(BaseModel):
    content: str

class MessageUpdate(BaseModel):
    content: str | None = None

class Message(BaseModel):
    id: int
    content: str

messages_db: list[Message] = [Message(id=0, content="First post in FastAPI")]

def next_id() -> int:
    return max((m.id for m in messages_db), default=-1) + 1


def get_index(message_id: int) -> int:
    return next((i for i, m in enumerate(messages_db) if m.id == message_id), -1)

@app.get("/messages", response_model=list[Message])
async def list_messages() -> list[Message]:
    return messages_db


@app.post("/messages", response_model=Message, status_code=201)
async def create_message(payload: MessageCreate) -> Message:
    m = Message(id=next_id(), content=payload.content)
    messages_db.append(m)
    return m


@app.get("/messages/{message_id}", response_model=Message)
async def get_message(message_id: int) -> Message:
    if (idx := get_index(message_id)) < 0:
        raise HTTPException(status_code=404, detail="Message not found")
    return messages_db[idx]

@app.patch("/messages/{message_id}", response_model=Message)
async def update_message(message_id: int, payload: MessageUpdate) -> Message:
    if (idx := get_index(message_id)) < 0:
        raise HTTPException(status_code=404, detail="Message not found")
    if payload.content is not None:
        messages_db[idx].content = payload.content
    return messages_db[idx]

@app.put("/messages/{message_id}", response_model=Message)
async def replace_message(message_id: int, payload: MessageCreate) -> Message:
    if (idx := get_index(message_id)) < 0:
        raise HTTPException(status_code=404, detail="Message not found")
    updated = Message(id=message_id, content=payload.content)
    messages_db[idx] = updated
    return updated

@app.delete("/messages/{message_id}", status_code=204)
async def delete_message(message_id: int):
    if (idx := get_index(message_id)) < 0:
        raise HTTPException(status_code=404, detail="Message not found")
    messages_db.pop(idx)
    return Response(status_code=204)
