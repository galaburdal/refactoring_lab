import cv2
import numpy as np
from PIL import Image
import os


def compute_hu_moments(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Could not read image: {image_path}")

    moments = cv2.moments(img)
    hu_moments = cv2.HuMoments(moments).flatten()  # Обчислюємо моменти Ху

    return hu_moments


def save_rotated_image(image_path, angle, output_path, center=None, translate=(0, 0), resample=Image.BICUBIC):
    im = Image.open(image_path)
    im_rotate = im.rotate(angle, expand=True, center=center, translate=translate, resample=resample)
    im_rotate.save(output_path, quality=95)
    im.close()
    return output_path


image_path = "c:\\Users\\ASUS\\Documents\\zebra.jpg"

transformed_images = {
    "Original": image_path,
    "90 degrees": save_rotated_image(image_path, 90, 'guido_90.jpg'),
    "45 degrees": save_rotated_image(image_path, 45, 'guido_45.jpg'),
    "Full rotation (90 expand)": save_rotated_image(image_path, 90, 'guido_expand_90.jpg'),
    "Full rotation (45 expand)": save_rotated_image(image_path, 45, 'guido_expand_45.jpg'),
    "Bicubic resample 45 degrees": save_rotated_image(image_path, 45, 'guido_resample_bicubic.jpg',
                                                      resample=Image.BICUBIC),
    "Change center": save_rotated_image(image_path, 45, 'guido_new_center_expand.jpg', center=(0, 100)),
    "Rotation with translation": save_rotated_image(image_path, 45, 'guido_translate_45.jpg', translate=(100, 50))
}

hu_moments_results = {desc: compute_hu_moments(path) for desc, path in transformed_images.items()}

print("\n📊 Hu Moments Comparison:")
for desc, moments in hu_moments_results.items():
    print(f"{desc}: {moments}")

original_moments = hu_moments_results["Original"]
print("\n🔍 Degree of Distortion:")
for desc, moments in hu_moments_results.items():
    if desc != "Original":
        diff = np.linalg.norm(original_moments - moments)  # Обчислюємо відстань між моментами
        print(f"{desc}: {diff:.6f}")