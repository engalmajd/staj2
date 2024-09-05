import cv2

# Görüntü yükleme
image = cv2.imread('majd.jpg')

# Gri tonlamaya çevirme
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Kenar tespiti
edges = cv2.Canny(gray_image, 100, 200)

# Görüntüleri gösterme
cv2.imshow('Original Image', image)
cv2.imshow('Gray Image', gray_image)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
