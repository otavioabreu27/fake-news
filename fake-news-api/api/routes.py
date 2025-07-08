from fastapi import APIRouter
from .models import NewsInput, ClassificationResult, NewsInputType, StatusResponse
from .service import classify_text, fetch_text_from_url, is_model_ready
from .store import exists, get_by_text, save_result, get_history

router = APIRouter()

@router.post("/classificar-noticia", response_model=ClassificationResult)
def classificar_noticia(news: NewsInput):
    if not news.content:
        raise ValueError("Campo 'content' é obrigatório.")

    if news.input_type == NewsInputType.text:
        if exists(news.content):
            item = get_by_text(news.content)
            # retorna com o tipo da requisição atual (text)
            return ClassificationResult(**item.dict(), type=NewsInputType.text)
        result = classify_text(news.content)
        save_result(news.content, result, NewsInputType.text)
        return ClassificationResult(**result, type=NewsInputType.text)

    elif news.input_type == NewsInputType.url:
        text = fetch_text_from_url(news.content)
        if exists(text):
            item = get_by_text(text)
            # retorna com o tipo da requisição atual (url)
            return ClassificationResult(**item.dict(), type=NewsInputType.url)
        result = classify_text(text)
        save_result(text, result, NewsInputType.url)
        return ClassificationResult(**result, type=NewsInputType.url)

    raise ValueError("Tipo de entrada inválido.")


@router.get("/historico", response_model=list[ClassificationResult])
def historico():
    return get_history()


@router.get("/status", response_model=StatusResponse)
def status():
    return StatusResponse(status="ready" if is_model_ready() else "loading")
