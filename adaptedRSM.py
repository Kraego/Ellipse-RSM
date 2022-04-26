import math
import numpy as np
from math_utils import polar_r_ellipse, get_x_y_from_polar_r


def _is_in_image(image, x, y):
    width = image.shape[0]
    height = image.shape[1]

    return 0 < x < width and 0 < y < height 


def daugman_normalization_ellipse(image, from_theta, to_theta, center, inner_axis, rotation, ellipse_thickness, samples):
    """Implementation of ruber-sheet model by daugman adapted to ellipses, creates a rectangular, polarlike representation.
       The rotation is clock wise from start theta to theta, output image: left is from_theta - right is to_theta.
       If the calculated pixel is outside of source image the pixel will be red in the result!

    Args:
        image (np.array): the input image
        from_theta (float): start angle in rad
        to_theta (float): end angle in rad
        center (int, int): center coordinates (x, y) of the ellipse
        inner_axis (int, int): inner axis (a,b)
        rotation: rotation angle of the ellipse
        ellipse_thickness (int): thickness of the band (like radius of iris (see paper) (y-Axis of the rectangular polar form))
        samples (int): number of samples for theta range (x-Axis of rectangular polar form)

    Returns:
        np.array: rectangular polar form of the provided image
    """
    to_theta = to_theta + np.pi * 2 if to_theta < from_theta else to_theta
    thetas = np.arange(from_theta, to_theta, abs(to_theta - from_theta) / samples)  

    # Create empty flatten image - rectangular region in polar coordinates
    polarForm = np.zeros((ellipse_thickness, samples, 3), np.uint8)

    for r in range(ellipse_thickness):
        # increase axis lengths  
        a = inner_axis[1] + r
        b = inner_axis[0] + r  
        # create 
        for sample in range(samples):
            # x of polarfrom
            theta = thetas[sample]   # value of theta 

            # Additional step calculate r from axis and theta
            radius = polar_r_ellipse(a,b, theta)
            x_offset , y_offset = get_x_y_from_polar_r(radius, theta)

            # adapt to rotation - with inplace rotation matrix
            xr = (x_offset * math.cos(-rotation)) - (y_offset * math.sin(-rotation))
            yr = (x_offset * math.sin(-rotation)) + (y_offset * math.cos(-rotation))

            x = center[1] + xr
            y = center[0] + yr

            if _is_in_image(image, x, y):
                # thru 90° rotation (different axis) - width and height are switched
                pixel = image[int(x)][int(y)]  # get Cartesian pixel
            else:
                pixel = (0, 0, 255)
            polarForm[r][sample] = pixel
    return polarForm 
