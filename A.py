import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Veri oluşturma
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([1, 4, 3, 6, 7])

# Model oluşturma ve eğitme
model = LinearRegression()
model.fit(X, y)

# Tahmin yapma
y_pred = model.predict(X)

# Sonuçları görselleştirme
plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.title('Basit Lineer Regresyon')
plt.xlabel('X')
plt.ylabel('y')
plt.show()
