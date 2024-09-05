import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Veri yükleme
data = pd.read_csv('data.csv')

# Özellikleri ve hedef değişkeni ayırma
X = data.drop('target', axis=1)
y = data['target']

# Veriyi eğitim ve test setlerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Karar ağacı modelini oluşturma ve eğitme
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Test seti üzerinde tahmin yapma
y_pred = model.predict(X_test)

# Modelin doğruluğunu hesaplama
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Doğruluğu: {accuracy}')
