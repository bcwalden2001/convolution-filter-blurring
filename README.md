## Summary

This program performs image convolution and blurring on an image using filtering operations. 

This program performs image filtering using a custom filter, Sobel, box, and Gaussian by manually convolving a grayscale image, then displaying and saving the results as a new image.

## Methodology

### 1. Image Input

- The program reads the starting demo image (blueparrot.jpg) in both color and grayscale.
- The grayscale version is converted to float32 so convolution calculations remain accurate.

### 2. Filter Construction

Several filters are defined:

- Custom sharpening filter
- Sobel X and Sobel Y filters for edge detection
- 5×5 box filter (each weight = 1/25)
- Gaussian filter generator

A "filter_size × filter_size" matrix is created and each element is calculated using this 2D Gaussian function:

<img width="297" height="57" alt="image" src="https://github.com/user-attachments/assets/92528a70-cb34-4f6a-9ede-37bb931352d9" />

This produces a smooth, circularly symmetric kernel.

### 3. Manual Convolution Implementation

The convolve function:

- Creates an output image initialized to zeros.
- For every pixel, it iterates through all filter weights.
- It multiplies overlapping image pixels with corresponding filter values, summing them to produce a new pixel value.
- Boundary checks ensure sampling stays inside the image.
- After convolution, the output is normalized to the 0–1 range.

This simulates how convolution works behind the scenes in real image-processing libraries.

### 4. Blurring Process

- A Gaussian filter is generated given a filter size and standard deviation
- The code applies the Gaussian filter via the custom convolution function to blur the grayscale image.
(Note: the convolve function will work with all other filters)

### 5. Output Display

- The blurred image is scaled back to 8-bit integers (0–255).
- The results are already provided with indications ofthe filter size or standard deviation in the file name.

## Conclusion

This program demonstrates the fundamental principles behind convolution and image blurring by manually implementing a filtering pipeline.

Although OpenCV provides efficient built-in functions already, manual implementation deepens understanding of filter behavior and the mechanics of convolution and effectively replicates sharpening, blurring, and edge detection of raster images. 
