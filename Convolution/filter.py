# Author: Bailey Walden

import cv2
import numpy as np
from math import pi, e

# Reading the image in
img = cv2.imread("blueparrot.jpg")  # Use a custom image
filter_img = cv2.imread("blueparrot.jpg", 0).astype(np.float32) # Greyscale

# Getting image dimensions
image_height = img.shape[0]
image_width = img.shape[1]

# Filters
custom_filter = np.array([(-1, -1, -1), (-1, 9, -1), (-1, -1, -1)])
sobelX_filter = np.array([(-1, 0, 1), (-2, 0, 2), (-1, 0, 1)])
sobelY_filter = np.array([(1, 2, 1), (0, 0, 0), (-1, -2, -1)])
box_filter = np.array([(1/25, 1/25, 1/25, 1/25, 1/25), 
                       (1/25, 1/25, 1/25, 1/25, 1/25), 
                       (1/25, 1/25, 1/25, 1/25, 1/25),
                       (1/25, 1/25, 1/25, 1/25, 1/25),
                       (1/25, 1/25, 1/25, 1/25, 1/25)])

# Creating the Gaussian filter
def get_gaussian_filter(filter_size, standard_deviation):

    filter = np.zeros((filter_size, filter_size), dtype=np.float32)
    half_window = filter_size // 2
    x = -(filter_size // 2)
    y = (filter_size // 2)

    for i in range(filter_size):
        y = i - half_window    # y-coordinate in filter
        for j in range(filter_size):
            x = j - half_window    # x-coordinate in filter 
            filter[i][j] = gaussian_function(x, y, standard_deviation)

    return filter

def gaussian_function(x, y, standard_deviation):
    return (1/(2*pi*(standard_deviation)**2)) * (e **((-((x)**2 + (y)**2))/(2*(standard_deviation**2))))

def convolve(image, filter):
    filter_img = np.zeros_like(image)
    filter_height, filter_width = filter.shape
    half_window = len(filter) // 2

    for i in range(image_height):
        for j in range(image_width):
            window_sum = 0
            for k in range(filter_height):
                for l in range(filter_width):
                    y_coord = i + k - half_window
                    x_coord = j + l - half_window
                    if (0 <= y_coord < image_height) and (0 <= x_coord < image_width):
                        window_sum += image[y_coord][x_coord] * filter[k][l]
            filter_img[i, j] = window_sum

    # Normalizing pixels to the 0 to 1 range
    filter_img /= np.max(filter_img)
    return filter_img

# Blurring the image using a gaussian filter
gaussian_filter = get_gaussian_filter(25, 1.5)
blur = convolve(filter_img, box_filter)

# Scaling pixel to the 0-255 range for displaying
blur = (blur * 255).astype(np.uint8)

cv2.imshow("Original image", img)
cv2.imshow("Image after convolution", blur)
cv2.imwrite("blueparrot25x25.jpg", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()