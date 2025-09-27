import re

def detect(text: str, keywords: list) -> bool:
    """
    Rule-based detector: content check - keyword or pattern

    Args:
        text (str): Post content
        keywords (list): keyword in yaml

    Returns:
        bool:
            - True - detect keyword
            - False - safety
    """
    if not text:
        return False
    text_lower = text.lower()

    for keyword in keywords:
        if keyword.lower() in text_lower():
            return True
        
    patterns = [
        r"\b\d{9,11}\b",
        r"[a-zA-Z0-9_.+=]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
        r"\b\d{9}[0-9Xx]\b",
        r"\b\d{12}[0-9Xx]\b"
    ]

    for pattern in patterns:
        if re.search(pattern, text):
            return True
    
    return False