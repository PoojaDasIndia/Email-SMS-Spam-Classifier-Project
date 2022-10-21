import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def text_transformer(text):
    # 1. Make text lower
    text = text.lower()

    # 2. Tokenization
    text = nltk.word_tokenize(text)

    # 3. Removing special characters
    list_storage = [word for word in text if word.isalnum()]

    # 4.  Removing stop words
    text = list_storage.copy()
    list_storage = [word for word in text if word not in stopwords.words('english')]

    # 5. Stemming
    text = list_storage.copy()
    list_storage = [ps.stem(word=word) for word in text]

    return " ".join(list_storage)


