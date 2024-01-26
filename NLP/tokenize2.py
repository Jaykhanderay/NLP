from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize,word_tokenize


sentence="Hello i want to go to home . because i am to late and i dont feel good"

words= word_tokenize(sentence)

ps = PorterStemmer()

for w in words:
         rootWord=ps.stem(w)
         print(rootWord)




