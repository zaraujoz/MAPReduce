def mapper(text):
    text = text.lower().strip()
    text = ''.join([c for c in text if c.isalpha() or c.isspace()])
    
    words = text.split()
    
    word_counts = []
    for word in words:
        word_counts.append((word, 1))
    
    return word_counts

def reducer(word, counts):
    return word, sum(counts)

def map_reduce(texts):
    mapped_data = []
    for text in texts:
        mapped_data.extend(mapper(text))
    
    mapped_data.sort(key=lambda x: x[0])
    
    reduced_data = []
    i = 0
    while i < len(mapped_data):
        word = mapped_data[i][0]
        counts = [x[1] for x in mapped_data[i:i+2] if x[0] == word]
        reduced_data.append(reducer(word, counts))
        i += len(counts)
    
    return reduced_data

texts = [
    "O cachorro correu pelo parque.",
    "O gato pulou no telhado.",
    "O cachorro brincou com o gato."
]
result = map_reduce(texts)
print(result)
