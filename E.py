import nltk
import logging
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# NLTK kayıt seviyesini düşür
logging.getLogger('nltk').setLevel(logging.ERROR)

# Gerekli paketleri sessizce indir
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

# Metin örneği
text = "OpenAI is creating amazing artificial intelligence."

# Tokenizasyon (kelimelere bölme)
tokens = word_tokenize(text)

# Küçük harfe çevirme ve durdurma kelimeleri kaldırma
tokens = [word.lower() for word in tokens if word.isalnum()]
stop_words = set(stopwords.words('english'))
tokens = [word for word in tokens if word not in stop_words]

# Lemmatizasyon (kelimeleri köklerine indirme)
lemmatizer = WordNetLemmatizer()
tokens = [lemmatizer.lemmatize(word) for word in tokens]

# İşlenmiş kelimeleri yazdırma
print(tokens)
