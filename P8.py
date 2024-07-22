import cv2
import numpy as np

# Load an image
img = cv2.imread('input_image.jpg')
if img is None: exit(f"Error: Unable to load image 'input_image.jpg'")

# Get image dimensions
height, width = img.shape[:2]

# Rotation by 45 degrees counter-clockwise around the center
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)
rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))

# Scale to 70% of its original size
scaled_img = cv2.resize(img, (int(width * 0.7), int(height * 0.7)), interpolation=cv2.INTER_LINEAR)

# Translate by (100, 50) pixels
translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])
translated_img = cv2.warpAffine(img, translation_matrix, (width, height))

# Display images
for title, image in zip(['Original Image', 'Rotated Image', 'Scaled Image', 'Translated Image'],
                        [img, rotated_img, scaled_img, translated_img]):
    cv2.imshow(title, image)

cv2.waitKey(0)
cv2.destroyAllWindows()
