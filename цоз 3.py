import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_float
from skimage.metrics import peak_signal_noise_ratio as psnr

image = cv2.imread('image.jpg', 0) 

# Лапласіанський фільтр (виділення контурів)
laplacian_kernel = np.array([[0, -1, 0],
                              [-1, 4, -1],
                              [0, -1, 0]], np.float32)

# Високочастотний фільтр (підсилення контурів)
high_pass_kernel = np.array([[-1, -1, -1],
                              [-1, 8, -1],
                              [-1, -1, -1]], np.float32)

# Низькочастотний (згладжуючий) фільтр (усереднювання)
low_pass_kernel = np.array([[1/9, 1/9, 1/9],
                             [1/9, 1/9, 1/9],
                             [1/9, 1/9, 1/9]], np.float32)

# Застосування фільтрів
laplacian_filtered_image = cv2.filter2D(image, -1, laplacian_kernel)
high_pass_filtered_image = cv2.filter2D(image, -1, high_pass_kernel)
low_pass_filtered_image = cv2.filter2D(image, -1, low_pass_kernel)

# Додавання шуму
noise = np.random.normal(0, 25, image.shape)
noisy_image = np.clip(image + noise, 0, 255)

# Фільтрація зашумленого зображення
filtered_noisy_image = cv2.filter2D(noisy_image.astype(np.uint8), -1, low_pass_kernel)

# Обчислення PSNR для кожного зображення
psnr_value_original = psnr(img_as_float(image), img_as_float(image))
psnr_value_laplacian = psnr(img_as_float(image), img_as_float(laplacian_filtered_image))
psnr_value_high_pass = psnr(img_as_float(image), img_as_float(high_pass_filtered_image))
psnr_value_low_pass = psnr(img_as_float(image), img_as_float(low_pass_filtered_image))
psnr_value_noisy = psnr(img_as_float(image), img_as_float(noisy_image))
psnr_value_filtered_noisy = psnr(img_as_float(image), img_as_float(filtered_noisy_image))

# Виведення результатів PSNR
print(f'PSNR (Оригінальне зображення): {psnr_value_original:.2f} дБ')
print(f'PSNR (Лапласіанське перетворення): {psnr_value_laplacian:.2f} дБ')
print(f'PSNR (Високочастотне перетворення): {psnr_value_high_pass:.2f} дБ')
print(f'PSNR (Низькочастотне перетворення): {psnr_value_low_pass:.2f} дБ')
print(f'PSNR (Зашумлене зображення): {psnr_value_noisy:.2f} дБ')
print(f'PSNR (Зашумлене після фільтрації): {psnr_value_filtered_noisy:.2f} дБ')

# Відображення результатів
plt.figure(figsize=(12, 6))

plt.subplot(231)
plt.imshow(image, cmap='gray')
plt.title(f'Оригінальне зображення\nPSNR: {psnr_value_original:.2f} дБ')
plt.axis('off')

plt.subplot(232)
plt.imshow(laplacian_filtered_image, cmap='gray')
plt.title(f'Лапласіанське перетворення\nPSNR: {psnr_value_laplacian:.2f} дБ')
plt.axis('off')

plt.subplot(233)
plt.imshow(high_pass_filtered_image, cmap='gray')
plt.title(f'Високочастотне перетворення\nPSNR: {psnr_value_high_pass:.2f} дБ')
plt.axis('off')

plt.subplot(234)
plt.imshow(low_pass_filtered_image, cmap='gray')
plt.title(f'Низькочастотне перетворення\nPSNR: {psnr_value_low_pass:.2f} дБ')
plt.axis('off')

plt.subplot(235)
plt.imshow(noisy_image, cmap='gray')
plt.title(f'Зашумлене зображення\nPSNR: {psnr_value_noisy:.2f} дБ')
plt.axis('off')

plt.subplot(236)
plt.imshow(filtered_noisy_image, cmap='gray')
plt.title(f'Зашумлене після фільтрації\nPSNR: {psnr_value_filtered_noisy:.2f} дБ')
plt.axis('off')

plt.tight_layout()
plt.show()

