import markdown
from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse

from api.docs_loader import read_doc
from api import crud
from web.templating import templates


router = APIRouter(
    prefix="/web/messages",
    tags=["web"],
    include_in_schema=False,
)

docs_router = APIRouter(prefix="/web/docs", tags=["web"], include_in_schema=False)


@router.get("", response_class=HTMLResponse)
async def get_messages_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"messages": crud.get_all()},
    )


@router.get("/create", response_class=HTMLResponse)
async def get_create_message_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="create.html",
    )


@router.post("", response_class=HTMLResponse)
async def create_message_form(request: Request, content: str = Form(...)):
    crud.create(content)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"messages": crud.get_all()},
    )


@router.get("/{message_id}", response_class=HTMLResponse)
async def get_message_detail_page(request: Request, message_id: int):
    message = crud.get_by_id(message_id)
    if message is None:
        return templates.TemplateResponse(
            request=request,
            name="error.html",
            context={"code": 404, "detail": "Сообщение не найдено"},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return templates.TemplateResponse(
        request=request,
        name="detail.html",
        context={"message": message},
    )

@docs_router.get("/{name}", response_class=HTMLResponse)
async def get_doc_page(request: Request, name: str):
    try:
        md_text = read_doc(f"{name}.md")
    except FileNotFoundError:
        return templates.TemplateResponse(
            request=request,
            name="error.html",
            context={"code": 404, "detail": f"Документ '{name}' не найден"},
            status_code=status.HTTP_404_NOT_FOUND,
        )

    html = markdown.markdown(md_text, extensions=["fenced_code", "tables"])
    return templates.TemplateResponse(
        request=request,
        name="doc.html",
        context={"content": html},
    )