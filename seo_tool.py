import nltk
from nltk.corpus import wordnet

# Descarga los datos necesarios
nltk.download('wordnet')

def find_related_words(keywords):
    related_words = []
    for keyword in keywords:
        synsets = wordnet.synsets(keyword)
        for synset in synsets:
            related_words.extend(synset.lemma_names())
    return related_words

def create_microniche(base_keywords, region='ES'):
    related_words = find_related_words(base_keywords)
    microniches = related_words  # Aquí puedes modificar para crear micronichos
    return microniches

if __name__ == "__main__":
    base_keywords = ['palabras', 'clave', 'seo']
    microniches = create_microniche(base_keywords)
    print("Microniches:", microniches)
