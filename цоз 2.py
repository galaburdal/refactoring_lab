import cv2
import numpy as np
import matplotlib.pyplot as plt

def negative_transformation(image):
    return 255 - image

def log_transformation(image, c=1):
    image = np.uint8(image)
    return np.uint8(c * np.log1p(image))

def power_law_transformation(image, gamma, c=1):
    image = np.uint8(image)
    return np.uint8(c * (image / 255) ** gamma * 255)

def add_gaussian_noise(image, mean=0, sigma=25):
    noise = np.random.normal(mean, sigma, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)
    return noisy_image

def mse(original, processed):
    return np.mean((original - processed) ** 2)

def psnr(original, processed):
    mse_value = mse(original, processed)
    if mse_value == 0:
        return 100
    return 10 * np.log10((255 ** 2) / mse_value)

def plot_images(images, titles, cmap='gray'):
    plt.figure(figsize=(15, 5))
    for i in range(len(images)):
        plt.subplot(1, len(images), i + 1)
        plt.imshow(images[i], cmap=cmap)
        plt.title(titles[i], fontsize=10)
        plt.axis('off')
    plt.show()

gray_image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

if gray_image is None:
    print("Помилка: зображення не завантажено. Перевірте шлях до файлу.")
else:
    negative_image = negative_transformation(gray_image)
    log_image = log_transformation(gray_image, c=45)
    power_image = power_law_transformation(gray_image, gamma=0.5)

    noisy_image = add_gaussian_noise(gray_image)
    
    denoised_image = log_transformation(noisy_image, c=45)  
    
    psnr_value = psnr(gray_image, denoised_image)
    print(f'PSNR після обробки: {psnr_value:.2f} дБ')
   
    plot_images([gray_image, negative_image, log_image, power_image],
                ['Оригінальне', 'Негатив', 'Логарифмічне перетворення', 'Степеневе перетворення'])
    plot_images([noisy_image, denoised_image], ['Зашумлене зображення', 'Оброблене зображення'])