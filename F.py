import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Veriyi yükleme
data = pd.read_csv('movie_reviews.csv')

# Sütun adlarını kontrol etme
print(data.columns)

# Özellik çıkarma (doğru sütun adlarını kullanarak)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['text'])
y = data['label']

# Veriyi eğitim ve test setlerine katmanlı olarak bölme
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Model oluşturma ve eğitme
model = MultinomialNB()
model.fit(X_train, y_train)

# Tahmin yapma ve doğruluk hesaplama
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Doğruluk: {accuracy}')

# Sınıflandırma raporunu gösterme
print("\nSınıflandırma Raporu:")
print(classification_report(y_test, y_pred))

# Karışıklık matrisini gösterme
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=['Negative', 'Positive'], yticklabels=['Negative', 'Positive'])
plt.xlabel('Tahmin Edilen')
plt.ylabel('Gerçek')
plt.title('Karışıklık Matrisi')
plt.show()
