import nltk

# Download the 'wordnet' resource
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
text = "'studies studiying cries cry "
tokenization=nltk.word_tokenize(text)
for w in tokenization:
    print("lemma for {} is {}".format(w,wordnet_lemmatizer.lemmatize(w)))
