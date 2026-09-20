import re

def encode(text, vocab):
    tokens = re.split(r"([,.:;?_!\"()\']|--|\s)", text)
    cleaned_tokens = [t.strip() for t in tokens if t and t.strip()]
    return [vocab[token] for token in cleaned_tokens]

def decode(ids, vocab):
    inverse_vocab = {v: k for k, v in vocab.items()}
    tokens = [inverse_vocab[i] for i in ids]
    text = " ".join(tokens)
    text = re.sub(r"\s+([,.\?!\"\(\)\'])", r"\1", text)
    return text