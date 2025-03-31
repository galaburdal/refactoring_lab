import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, exp
from skimage.metrics import peak_signal_noise_ratio as psnr

# Функція для обчислення відстані
def distance(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Низькочастотні фільтри
def butterworth_lp(D0, img_shape, n):
    base = np.zeros(img_shape[:2])
    rows, cols = img_shape[:2]
    center = (rows / 2, cols / 2)
    for x in range(cols):
        for y in range(rows):
            base[y, x] = 1 / (1 + (distance((y, x), center) / D0) ** (2 * n))
    return base

def gaussian_lp(D0, img_shape):
    base = np.zeros(img_shape[:2])
    rows, cols = img_shape[:2]
    center = (rows / 2, cols / 2)
    for x in range(cols):
        for y in range(rows):
            base[y, x] = exp(((-distance((y, x), center) ** 2) / (2 * (D0 ** 2))))
    return base

# Високочастотні фільтри (1 - низькочастотний фільтр)
def butterworth_hp(D0, img_shape, n):
    return 1 - butterworth_lp(D0, img_shape, n)

def gaussian_hp(D0, img_shape):
    return 1 - gaussian_lp(D0, img_shape)

# Функція для застосування фільтра
def apply_filter(img, filter_kernel):
    dft = np.fft.fft2(img)
    dft_shifted = np.fft.fftshift(dft)
    filtered_dft = dft_shifted * filter_kernel
    idft_shifted = np.fft.ifftshift(filtered_dft)
    filtered_img = np.fft.ifft2(idft_shifted)
    return np.abs(filtered_img)

# Завантаження зображення
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    raise ValueError("Помилка: зображення не завантажено. Перевірте шлях до файлу.")

D0 = 50  # Гранична частота
n = 2  # Порядок фільтра Баттерворта

# Створення низькочастотних фільтрів
butter_lp_filter = butterworth_lp(D0, image.shape, n)
gaussian_lp_filter = gaussian_lp(D0, image.shape)

# Створення високочастотних фільтрів
butter_hp_filter = butterworth_hp(D0, image.shape, n)
gaussian_hp_filter = gaussian_hp(D0, image.shape)

# Застосування фільтрів
butter_lp_image = apply_filter(image, butter_lp_filter)
gaussian_lp_image = apply_filter(image, gaussian_lp_filter)
butter_hp_image = apply_filter(image, butter_hp_filter)
gaussian_hp_image = apply_filter(image, gaussian_hp_filter)

# Обчислення PSNR
psnr_butter_lp = psnr(image, butter_lp_image)
psnr_gaussian_lp = psnr(image, gaussian_lp_image)
psnr_butter_hp = psnr(image, butter_hp_image)
psnr_gaussian_hp = psnr(image, gaussian_hp_image)

print(f'PSNR Баттерворта (НЧ): {psnr_butter_lp:.2f} дБ')
print(f'PSNR Гауса (НЧ): {psnr_gaussian_lp:.2f} дБ')
print(f'PSNR Баттерворта (ВЧ): {psnr_butter_hp:.2f} дБ')
print(f'PSNR Гауса (ВЧ): {psnr_gaussian_hp:.2f} дБ')

# Візуалізація результатів
plt.figure(figsize=(12, 8))

plt.subplot(231)
plt.imshow(image, cmap='gray')
plt.title('Оригінальне зображення')
plt.axis('off')

plt.subplot(232)
plt.imshow(butter_lp_image, cmap='gray')
plt.title('Фільтр Баттерворта (НЧ)')
plt.axis('off')

plt.subplot(233)
plt.imshow(gaussian_lp_image, cmap='gray')
plt.title('Гаусівський фільтр (НЧ)')
plt.axis('off')

plt.subplot(234)
plt.imshow(butter_hp_image, cmap='gray')
plt.title('Фільтр Баттерворта (ВЧ)')
plt.axis('off')

plt.subplot(235)
plt.imshow(gaussian_hp_image, cmap='gray')
plt.title('Гаусівський фільтр (ВЧ)')
plt.axis('off')

plt.tight_layout()
plt.show()
