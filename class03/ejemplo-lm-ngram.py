from collections import defaultdict
import math

# Corpus pequeño
corpus = [
    "el gato duerme",
    "el perro ladra",
    "el gato maúlla",
    "el perro duerme"
]

# Tokenización simple
tokenized_sentences = [sentence.split() for sentence in corpus]

# Contadores
unigram_counts = defaultdict(int)
bigram_counts = defaultdict(int)

# Contar unigrams y bigrams
for sentence in tokenized_sentences:
    for i in range(len(sentence)):
        unigram_counts[sentence[i]] += 1
        if i > 0:
            bigram = (sentence[i-1], sentence[i])
            bigram_counts[bigram] += 1

# Calcular MLE para cada bigrama
bigram_probs = dict()
for (w1, w2), count in bigram_counts.items():
    bigram_probs[(w1, w2)] = count / unigram_counts[w1]

# Mostrar probabilidades estimadas
print("Probabilidades MLE de bigramas:\n")
for (w1, w2), prob in bigram_probs.items():
    print(f"P({w2} | {w1}) = {prob:.3f}")

# Evaluar la probabilidad de una oración
def sentence_log_probability(sentence_tokens, bigram_probs, unigram_counts):
    prob_log_sum = 0.0
    for i in range(1, len(sentence_tokens)):
        w1, w2 = sentence_tokens[i-1], sentence_tokens[i]
        if (w1, w2) in bigram_probs:
            prob_log_sum += math.log(bigram_probs[(w1, w2)])
        else:
            # Si el bigrama no está, probabilidad 0 → log(1e-10) (muy baja)
            prob_log_sum += math.log(1e-10)
    return prob_log_sum

# Frase a evaluar
sentence = "el gato duerme".split()
log_prob = sentence_log_probability(sentence, bigram_probs, unigram_counts)
print(f"\nLog-verosimilitud de la frase '{' '.join(sentence)}': {log_prob:.3f}")
