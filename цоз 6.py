import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import peak_signal_noise_ratio as psnr

def add_gaussian_noise(image, mean=0, sigma=25):
    noise = np.random.normal(mean, sigma, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)
    return noisy_image

def mean_filter(image, kernel_size=3):
    return cv2.blur(image, (kernel_size, kernel_size))

def median_filter(image, kernel_size=3):
    return cv2.medianBlur(image, kernel_size)

image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    raise ValueError("Помилка: зображення не завантажено. Перевірте шлях до файлу.")

noisy_image = add_gaussian_noise(image)

mean_filtered = mean_filter(noisy_image, kernel_size=3)
median_filtered = median_filter(noisy_image, kernel_size=3)

psnr_mean = psnr(image, mean_filtered)
psnr_median = psnr(image, median_filtered)

print(f'PSNR середньоарифметичного фільтра: {psnr_mean:.2f} дБ')
print(f'PSNR медіанного фільтра: {psnr_median:.2f} дБ')

plt.figure(figsize=(12, 6))

plt.subplot(1, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Оригінальне зображення')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(noisy_image, cmap='gray')
plt.title('Зашумлене зображення')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(mean_filtered, cmap='gray')
plt.title('Середньоарифметичний фільтр')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(median_filtered, cmap='gray')
plt.title('Медіанний фільтр')
plt.axis('off')

plt.show()
