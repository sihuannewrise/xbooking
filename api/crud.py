from pydantic import BaseModel


class MessageCreate(BaseModel):
    content: str


class Message(BaseModel):
    id: int
    content: str


messages_db: list[Message] = [Message(id=0, content="Первое сообщение в FastAPI")]


def get_all() -> list[Message]:
    return messages_db


def get_by_id(message_id: int) -> Message | None:
    return next((m for m in messages_db if m.id == message_id), None)


def create(content: str) -> Message:
    next_id = max((m.id for m in messages_db), default=-1) + 1
    new_message = Message(id=next_id, content=content)
    messages_db.append(new_message)
    return new_message


def update(message_id: int, content: str) -> Message | None:
    msg = get_by_id(message_id)
    if msg is None:
        return None
    msg.content = content
    return msg


def delete(message_id: int) -> bool:
    msg = get_by_id(message_id)
    if msg is None:
        return False
    messages_db.remove(msg)
    return True


def delete_all() -> None:
    messages_db.clear()
