import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelBinarizer

# Iris veri setini yükleme
data = load_iris()
X = data.data
y = data.target

# Sadece iki sınıfı seçme (örneğin, sınıf 0 ve 1)
X = X[y != 2]
y = y[y != 2]

# Veriyi standartlaştırma
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Veri setini bölme
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Etiketleri ikili formata dönüştürme
lb = LabelBinarizer()
y_train = lb.fit_transform(y_train).flatten()
y_test = lb.transform(y_test).flatten()

# Model oluşturma
model = Sequential()
model.add(Input(shape=(X_train.shape[1],)))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Modeli derleme
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Modeli eğitme
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Modeli değerlendirme
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test doğruluğu: {accuracy}')
