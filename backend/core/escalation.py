KEYWORDS = ["refund", "return", "chargeback", "support agent", "human", "complaint"]

def detect_keywords(text: str) -> bool:
    t = text.lower()
    return any(k in t for k in KEYWORDS)

def should_escalate(model_conf: float, sentiment_label: str, keyword_hit: bool) -> bool:
    if keyword_hit:
        return True
    if model_conf < 0.6:
        return True
    if sentiment_label in ["angry", "frustrated", "negative"]:
        return True
    return False


