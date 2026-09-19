def unigram_probability(corpus: str, word: str) -> float:
    tokens = corpus.split(" ")
    n_tokens = len(tokens)
    # count word in tokens
    word_count = tokens.count(word)
    probability = round(word_count / n_tokens, 4)
    return probability