import cv2
import numpy as np
import os

ALPHA = 1.5 # Contrast control (1.5 increases contrast)
BETA = 0 # Brightness control (0 has no effect)

OG_DIRECTORY = "datasets/original/"
PP_DIRECTORY = "datasets/preprocessed/"


def adjust_contrast(image):
    """
    Adjusts the contrast and brightness of an image from an
    image path and variables: alpha, and beta.
    """
    # Convert the image from uint8 to float to avoid overflow/underflow
    image = image.astype(np.float64)

    # Adjust contrast and brightness using `f(x) = alpha * x + beta` formula
    image = image * ALPHA + BETA
    # Clamp values to stay within the 0-255 range and convert back to uint8
    image = np.clip(image, 0, 255).astype(np.uint8)

    return image


def preprocess_initial_data():
    """
    Initial preprocessing of every image in the dataset from the original
    data path and saving to new preprocessed directory.    
    """
    for filename in os.listdir(OG_DIRECTORY):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            input_image_path = os.path.join(OG_DIRECTORY, filename)
            output_image_path = os.path.join(PP_DIRECTORY, filename)
            image = cv2.imread(input_image_path)
            if image is not None:
                adjusted_image = adjust_contrast(image)
                cv2.imwrite(output_image_path, adjusted_image)

