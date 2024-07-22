import cv2

def display_image(image, title="Image"):
    cv2.imshow(title, image)

image_path = 'rose.jpg'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print(f"Error: Unable to load image '{image_path}'. Please check the file path.")
    exit()

edges = cv2.Canny(img, 100, 200)
blurred_img = cv2.GaussianBlur(img, (5, 5), 0)

display_image(img, "Original Image")
display_image(edges, "Edges Detected")
display_image(blurred_img, "Blurred Image")

cv2.waitKey(0)
cv2.destroyAllWindows()
