import cv2
import matplotlib.pyplot as plt

# Function to split an image into 4 quadrants
def split_image_into_quadrants(image):
    # Get image dimensions
    height, width, channels = image.shape

    # Calculate midpoints
    mid_x = width // 2
    mid_y = height // 2

    # Split image into quadrants
    top_left = image[:mid_y, :mid_x]
    top_right = image[:mid_y, mid_x:]
    bottom_left = image[mid_y:, :mid_x]
    bottom_right = image[mid_y:, mid_x:]

    return top_left, top_right, bottom_left, bottom_right

# Read the image
image_path = 'image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Unable to read image at '{image_path}'")
else:
    # Split image into quadrants
    quadrants = split_image_into_quadrants(image)

    # Display each quadrant using matplotlib
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))

    axs[0, 0].imshow(cv2.cvtColor(quadrants[0], cv2.COLOR_BGR2RGB))
    axs[0, 0].set_title('Top Left Quadrant')
    axs[0, 0].axis('off')

    axs[0, 1].imshow(cv2.cvtColor(quadrants[1], cv2.COLOR_BGR2RGB))
    axs[0, 1].set_title('Top Right Quadrant')
    axs[0, 1].axis('off')

    axs[1, 0].imshow(cv2.cvtColor(quadrants[2], cv2.COLOR_BGR2RGB))
    axs[1, 0].set_title('Bottom Left Quadrant')
    axs[1, 0].axis('off')

    axs[1, 1].imshow(cv2.cvtColor(quadrants[3], cv2.COLOR_BGR2RGB))
    axs[1, 1].set_title('Bottom Right Quadrant')
    axs[1, 1].axis('off')

    plt.tight_layout()
    plt.show()
