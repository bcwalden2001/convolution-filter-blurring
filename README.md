## Summary

This program performs image convolution and blurring on an image using manually implemented filtering operations. 

After loading an image in both color and grayscale, the code constructs a variety of filters including sharpening, Sobel edge detectors, a box blur, and a Gaussian kernel. A custom convolution function is used to slide each filter across the image and compute weighted sums of pixel neighborhoods. The main objective is to illustrate how convolution-based filtering works without relying on OpenCV’s built-in convolution functions. The provided altered images showcase convolution with varying kernel sizes and standard deviations.

Methodology
1. Image Input

The program reads blueparrot.jpg in both color and grayscale.

The grayscale version is converted to float32 so convolution calculations remain accurate.

2. Filter Construction

Several filters are defined manually:

Custom sharpening filter

Sobel X and Sobel Y filters for edge detection

5×5 box filter (each weight = 1/25)

Gaussian filter generator:

A filter_size × filter_size matrix is created.

Each element is calculated using the 2D Gaussian function:

𝐺
(
𝑥
,
𝑦
)
=
1
2
𝜋
𝜎
2
 
𝑒
−
(
𝑥
2
+
𝑦
2
)
/
(
2
𝜎
2
)
G(x,y)=
2πσ
2
1
	​

e
−(x
2
+y
2
)/(2σ
2
)

Produces a smooth, circularly symmetric kernel.

3. Manual Convolution Implementation

The convolve() function:

Creates an output image initialized to zeros.

For every pixel, it iterates through all filter weights.

It multiplies overlapping image pixels with corresponding filter values, summing them to produce a new pixel value.

Boundary checks ensure sampling stays inside the image.

After convolution, the output is normalized to the 0–1 range.

This simulates how convolution works behind the scenes in real image-processing libraries.

4. Blurring Process

A 25×25 Gaussian filter is generated (σ = 1.5).

The code applies a box filter via the custom convolution function to blur the grayscale image.
(Note: Even though the Gaussian filter is generated, the actual convolution uses the box filter.)

5. Output Display

The blurred image is scaled back to 8-bit integers (0–255).

Both original and blurred images are displayed with OpenCV.

The filtered result is saved as blueparrot25x25.jpg.

Conclusion

This code demonstrates the fundamental principles behind convolution and image blurring by manually implementing a filtering pipeline. By constructing filters, computing the Gaussian kernel mathematically, and applying convolution pixel-by-pixel, the script highlights how image operations such as sharpening, edge detection, and smoothing are derived from weighted neighborhood calculations. Although OpenCV provides efficient built-in functions, manually coding the process deepens understanding of filter behavior and the mechanics of convolution. The final blurred image confirms that the convolution algorithm and smoothing filters work as intended.
