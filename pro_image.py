import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Carregando a imagem
img = mpimg.imread('imagem.jpg')

# Exibindo a imagem original
plt.imshow(img)
plt.title('Imagem Original')
plt.show()

# Convertendo a imagem para escala de cinza
img_gray = mpimg.imread('imagem.jpg', 0)

# Exibindo a imagem em escala de cinza
plt.imshow(img_gray, cmap='gray')
plt.title('Imagem em Escala de Cinza')
plt.show()

# Realizando um zoom na imagem em escala de cinza
plt.imshow(img_gray[100:300, 200:400], cmap='gray')
plt.title('Zoom na Imagem em Escala de Cinza')
plt.show()

# Redimensionando a imagem em escala de cinza
img_gray_resized = mpimg.imresize(img_gray, (100, 100))

# Exibindo a imagem redimensionada
plt.imshow(img_gray_resized, cmap='gray')
plt.title('Imagem Redimensionada')
plt.show()
