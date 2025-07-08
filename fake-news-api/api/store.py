import hashlib
from collections import OrderedDict
from .models import ClassificationResult, NewsInputType

MAX_ENTRIES = 1000
_memory_store: OrderedDict[str, ClassificationResult] = OrderedDict()

def _hash(text: str) -> str:
    """Gera um hash SHA-256 do texto para indexação eficiente"""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def save_result(text: str, result: dict, input_type: NewsInputType):
    key = _hash(text)
    if key in _memory_store:
        return

    if len(_memory_store) >= MAX_ENTRIES:
        _memory_store.popitem(last=False)

    enriched = {
        **result,
        "type": input_type
    }

    _memory_store[key] = ClassificationResult(**enriched)

def exists(text: str) -> bool:
    return _hash(text) in _memory_store

def get_by_text(text: str) -> ClassificationResult | None:
    return _memory_store.get(_hash(text))

def get_history() -> list[ClassificationResult]:
    return list(_memory_store.values())
