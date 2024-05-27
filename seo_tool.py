import nltk
from nltk.corpus import wordnet

# Descarga los datos necesarios de NLTK
nltk.download('wordnet')

# Función para encontrar palabras relacionadas con las palabras clave
def find_related_words(keywords):
    related_words = []
    for keyword in keywords:
        synsets = wordnet.synsets(keyword)
        for synset in synsets:
            related_words.extend(synset.lemma_names())
    return related_words

# Función principal para crear micronichos
def create_microniche(base_keywords, region='ES'):
    related_words = find_related_words(base_keywords)
    # Aquí puedes usar las palabras relacionadas para crear micronichos
    microniches = related_words
    return microniches

# Ejemplo de uso 
if __name__ == "__main__":
    base_keywords = ['palabras', 'clave', 'seo']
    microniches = create_microniche(base_keywords)
    print("Microniches:", microniches)

