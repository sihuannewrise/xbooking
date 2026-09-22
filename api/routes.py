from fastapi import APIRouter, HTTPException, status

from api import crud
from api.crud import Message, MessageCreate

router = APIRouter(prefix="/api/messages", tags=["messages"])


@router.get("", response_model=list[Message])
async def read_messages():
    return crud.get_all()


@router.get("/{message_id}", response_model=Message)
async def read_message(message_id: int):
    msg = crud.get_by_id(message_id)
    if msg is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return msg


@router.post("", response_model=Message, status_code=status.HTTP_201_CREATED)
async def create_message(payload: MessageCreate):
    return crud.create(payload.content)


@router.put("/{message_id}", response_model=Message)
async def update_message(message_id: int, payload: MessageCreate):
    msg = crud.update(message_id, payload.content)
    if msg is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return msg


@router.delete("/{message_id}")
async def delete_message(message_id: int):
    if not crud.delete(message_id):
        raise HTTPException(status_code=404, detail="Message not found")
    return {"detail": f"Message ID={message_id} deleted!"}


@router.delete("")
async def delete_messages():
    crud.delete_all()
    return {"detail": "All messages deleted!"}
