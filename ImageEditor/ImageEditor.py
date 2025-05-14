"""
ImageEditor.py
==================
This script provides a simple image editor that allows users to perform basic operations
such as blurring, sharpening, and edge detection on images. It uses the OpenCV library for image
processing and the Tkinter library for the GUI. The script also includes a simple command-line
"""

import cv2
import numpy as np

class ImageEditor:
    """
    A simple image editor that allows users to perform basic operations on images.
    """

    def __init__(self):
        """
        Initializes the ImageEditor class.
        """
        self.image = None
        self.processed_image = None
        self.operations = {
            "blur": self.blur_image,
            "sharpen": self.sharpen_image,
            "edge_detection": self.edge_detection_image
        }

    def load_image(self, file_path):
        """
        Loads an image from the specified file path.
        """
        self.image = cv2.imread(file_path)
        if self.image is None:
            raise ValueError("Could not load image.")
        self.processed_image = self.image.copy()
        self.show_image(self.image)

    def show_image(self, image):
        """
        Displays the image in a window.
        """
        cv2.imshow("Image Editor", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save_image(self, file_path):
        """
        Saves the processed image to the specified file path.
        """
        if self.processed_image is None:
            raise ValueError("No processed image to save.")
        cv2.imwrite(file_path, self.processed_image)

    def apply_operation(self, operation):
        """
        Applies the specified operation to the image.
        """
        if operation not in self.operations:
            raise ValueError("Invalid operation.")
        self.processed_image = self.operations[operation]()
        self.show_image(self.processed_image)

    def blur_image(self, kernel_size=(5, 5), sigma=0):
        """
        Applies a Gaussian blur to the image based on the provided arguments
        """
        if self.image is None:
            raise ValueError("No image loaded.")
        return cv2.GaussianBlur(self.image, kernel_size, sigma)
    
    def sharpen_image(self):
        """
        Applies a sharpening filter to the image.
        """
        if self.image is None:
            raise ValueError("No image loaded.")
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        return cv2.filter2D(self.image, -1, kernel)
    
    def edge_detection_image(self):
        """
        Applies Canny edge detection to the image.
        """
        if self.image is None:
            raise ValueError("No image loaded.")
        return cv2.Canny(self.image, 100, 200)
    
if __name__ == "__main__":
    editor = ImageEditor()
    input_file = input("Enter the path to the image file: ")
    editor.load_image(input_file)
    
    operation = input("Enter the operation (blur, sharpen, edge_detection): ")
    editor.apply_operation(operation)

    save_file = input("Enter the path to save the processed image: ")
    editor.save_image(save_file)

    print("Image processing complete. Processed image saved.")