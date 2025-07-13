from fastapi import FastAPI, Request
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Requisição recebida: {request.method} {request.url}")
    response = await call_next(request)
    print(f"Resposta enviada: {response.status_code}")
    return response

@app.post("/analyze")
def analyze_sentiment(input_text: TextInput):
    blob = TextBlob(input_text.text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = "positivo"
    elif polarity < 0:
        sentiment = "negativo"
    else:
        sentiment = "neutro"
    return {"sentimento": sentiment, "polaridade": polarity}