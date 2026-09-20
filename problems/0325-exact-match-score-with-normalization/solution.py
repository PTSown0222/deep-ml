import string

def exact_match_score(predictions: list[str], references: list[str]) -> float:
    """
    Calculate the exact match score between predictions and references.
    
    Args:
        predictions: List of predicted strings
        references: List of reference (ground truth) strings
    
    Returns:
        Exact match score as a float between 0 and 1
    """
    if not predictions and not references:
        return 0.0
    def normalization(text):
        text = text.lower()
        text = "".join([char for char in text if char not in string.punctuation])
        text = " ".join(text.split())
        return text
    norm_preds = [normalization(p) for p in predictions]
    norm_refs = [normalization(r) for r in references]
    matches = sum(1 for p, r in zip(norm_preds, norm_refs) if p == r)
    return float(matches / len(predictions))