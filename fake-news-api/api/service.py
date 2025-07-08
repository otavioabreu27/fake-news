from transformers import pipeline
from newspaper import Article
import numpy as np

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

label_candidates = ["REAL", "FAKE"]

def fetch_text_from_url(url: str) -> str:
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        raise ValueError(f"Erro ao processar URL: {e}")

def split_into_chunks(text: str, max_chars: int = 1000) -> list[str]:
    """Divide o texto em pedaços de no máximo `max_chars` caracteres"""
    return [text[i:i+max_chars] for i in range(0, len(text), max_chars)]

def classify_text(text: str) -> dict:
    chunks = split_into_chunks(text)

    if not chunks:
        raise ValueError("Texto inválido ou vazio.")

    results = [classifier(chunk, candidate_labels=label_candidates) for chunk in chunks]

    label_scores = {"FAKE": [], "REAL": []}
    for r in results:
        for label, score in zip(r["labels"], r["scores"]):
            label_scores[label].append(score)

    final_label = max(label_scores, key=lambda lbl: (len(label_scores[lbl]), np.mean(label_scores[lbl])))
    final_score = round(np.mean(label_scores[final_label]) * 100, 2)

    return {
        "text": text[:1024] + ("..." if len(text) > 1024 else ""),
        "label": final_label,
        "score": final_score
    }

def is_model_ready() -> bool:
    return classifier is not None
