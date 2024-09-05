from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Iris veri setini yükleme
data = load_iris()
X = data.data
y = data.target

# Veriyi standartlaştırma
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Veri setini bölme
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=48)

# Model oluşturma ve eğitme
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Tahmin yapma ve doğruluk hesaplama
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Doğruluk: {accuracy}')

