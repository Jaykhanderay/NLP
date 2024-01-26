import nltk
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
set(stopwords.words('english'))

text=""" HI i am jay .i am artificial intelligence student and machine
 learning student.i am like to play the cricket ,football and many outdoor games
 i am always on the date with my lappy."""

# set of stop words

stop_words=set(stopwords.words('english'))

#token of  words

word_tokens= word_tokenize(text)

filtered_sentence = []

for w in word_tokens:
    if w not in word_tokens:
        filtered_sentence.append(w)

print("original sentence")
print(" ".join(word_tokens))

print("Filtered Sentence")
print(" ".join(filtered_sentence))

