from transformers import pipeline

class SentimentDetector:
    def __init__(self):
        self._pipe = pipeline("sentiment-analysis")

    def analyze(self, text: str):
        out = self._pipe(text)[0]
        label = out["label"].lower()
        if label == "negative":
            if any(w in text.lower() for w in ["angry", "furious", "rage"]):
                label = "angry"
            elif any(w in text.lower() for w in ["frustrated", "annoyed", "upset"]):
                label = "frustrated"
        return type("Senti", (), {"label": label, "score": float(out["score"])})


