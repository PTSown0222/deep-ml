import re

def tokenize_text(text: str) -> list:
    """
    Split raw text into tokens using regex-based splitting on whitespace
    and punctuation. Returns a list of non-empty stripped tokens.
    """
    tokens = re.split(r"([,.:;?_!\"()\']|--|\s)", text)
    cleaned_tokens = [t.strip() for t in tokens if t and t.strip()]
    return cleaned_tokens
