from fastapi import FastAPI, HTTPException, status, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


app = FastAPI()

templates = Jinja2Templates(directory="web/templates")
app.mount("/static", StaticFiles(directory="web/static"), name="static")


class MessageCreate(BaseModel):
    content: str


class Message(BaseModel):
    id: int
    content: str

messages_db: list[Message] = [Message(id=0, content="Первое сообщение в FastAPI")]


@app.get("/messages", response_model=list[Message])
async def read_messages() -> list[Message]:
    return messages_db


@app.get("/messages/{message_id}", response_model=Message)
async def read_message(message_id: int) -> Message:
    for message in messages_db:
        if message.id == message_id:
            return message
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")


@app.post("/messages", response_model=Message, status_code=status.HTTP_201_CREATED)
async def create_message(message_create: MessageCreate) -> Message:
    next_id = max((msg.id for msg in messages_db), default=-1) + 1
    new_message = Message(id=next_id, content=message_create.content)
    messages_db.append(new_message)
    return new_message


@app.put("/messages/{message_id}", status_code=status.HTTP_200_OK, response_model=Message)
async def update_message(message_id: int, message_create: MessageCreate) -> Message:
    for i, message in enumerate(messages_db):
        if message.id == message_id:
            updated_message = Message(id=message_id, content=message_create.content)
            messages_db[i] = updated_message
            return updated_message
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")

@app.delete("/messages/{message_id}", status_code=status.HTTP_200_OK)
async def delete_message(message_id: int) -> dict:
    for i, message in enumerate(messages_db):
        if message.id == message_id:
            messages_db.pop(i)
            return {"detail": f"Message ID={message_id} deleted!"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")


@app.delete("/messages", status_code=status.HTTP_200_OK)
async def delete_messages() -> dict:
    messages_db.clear()
    return {"detail": "All messages deleted!"}






@app.get("/web/messages", response_class=HTMLResponse)
async def get_messages_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"messages": messages_db},
    )

@app.get("/web/messages/create", response_class=HTMLResponse)
async def get_create_message_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="create.html"
    )


@app.post("/web/messages", response_class=HTMLResponse)
async def create_message_form(request: Request, content: str = Form(...)):
    next_id = max((msg.id for msg in messages_db), default=-1) + 1
    new_message = Message(id=next_id, content=content)
    messages_db.append(new_message)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"messages": messages_db},
    )

@app.get("/web/messages/{message_id}", response_class=HTMLResponse)
async def get_message_detail_page(request: Request, message_id: int):
    message = next((m for m in messages_db if m.id == message_id), None)
    if message is None:
        return templates.TemplateResponse(
            request=request,
            name="404.html",
            context={"detail": "Сообщение не найдено"},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return templates.TemplateResponse(
        request=request,
        name="detail.html",
        context={"message": message},
    )
