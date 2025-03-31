import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color

# Функція для застосування низькочастотного фільтра
def apply_lowpass_filter(f_transform_shifted, cutoff):
    rows, cols = f_transform_shifted.shape
    center = (rows // 2, cols // 2)
    mask = np.zeros((rows, cols))
    for x in range(cols):
        for y in range(rows):
            if np.sqrt((x - center[1])**2 + (y - center[0])**2) <= cutoff:
                mask[y, x] = 1
    return f_transform_shifted * mask

# Завантаження зображення
image = io.imread('image.jpg')
gray_image = color.rgb2gray(image)

# Двовимірне перетворення Фур'є
f_transform = np.fft.fft2(gray_image)
f_transform_shifted = np.fft.fftshift(f_transform)

# Амплітудний та фазовий спектр
amplitude_spectrum = np.abs(f_transform_shifted)
phase_spectrum = np.angle(f_transform_shifted)

# Візуалізація амплітудного та фазового спектрів
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(np.log1p(amplitude_spectrum), cmap='gray')
plt.title('Амплітудний спектр')
plt.colorbar()
plt.subplot(1, 2, 2)
plt.imshow(phase_spectrum, cmap='gray')
plt.title('Фазовий спектр')
plt.colorbar()
plt.show()

# Відновлення зображення лише за фазою
f_phase_only = np.exp(1j * phase_spectrum)
f_ishifted_phase = np.fft.ifftshift(f_phase_only)
restored_phase = np.fft.ifft2(f_ishifted_phase)
restored_phase_real = np.real(restored_phase)

# Відновлення зображення лише за амплітудою
normalized_amplitude = amplitude_spectrum / np.max(amplitude_spectrum)
f_amplitude_only = normalized_amplitude * np.exp(1j * np.zeros_like(phase_spectrum))
f_ishifted_amplitude = np.fft.ifftshift(f_amplitude_only)
restored_amplitude = np.fft.ifft2(f_ishifted_amplitude)
restored_amplitude_real = np.real(restored_amplitude)

# Відновлення повного зображення
f_ishifted_full = np.fft.ifftshift(f_transform_shifted)
restored_full = np.fft.ifft2(f_ishifted_full)
restored_full_real = np.real(restored_full)

# Візуалізація відновлених зображень
plt.figure(figsize=(12, 8))
plt.subplot(1, 3, 1)
plt.imshow(restored_phase_real, cmap='gray')
plt.title('Відновлене (лише фаза)')
plt.subplot(1, 3, 2)
plt.imshow(restored_amplitude_real, cmap='gray')
plt.title('Відновлене (лише амплітуда)')
plt.subplot(1, 3, 3)
plt.imshow(restored_full_real, cmap='gray')
plt.title('Відновлене (амплітуда і фаза)')
plt.show()

# Низькочастотна фільтрація
cutoff = 50  # Радіус фільтра
f_filtered = apply_lowpass_filter(f_transform_shifted, cutoff)
f_ishifted_filtered = np.fft.ifftshift(f_filtered)
restored_filtered = np.fft.ifft2(f_ishifted_filtered)
restored_filtered_real = np.real(restored_filtered)

# Візуалізація фільтрованого зображення
plt.figure(figsize=(6, 6))
plt.imshow(restored_filtered_real, cmap='gray')
plt.title('Фільтроване зображення (НЧ)')
plt.show()
