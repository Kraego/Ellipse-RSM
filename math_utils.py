import math

def polar_r_ellipse(a, b, theta):
    """get r from ellipse
    see: https://en.wikipedia.org/wiki/Ellipse#Polar_form_relative_to_center
    Args:
        a (int): a axis
        b (int): b axis
        theta (float): theta in rad

    Returns:
        float: the calculated r
    """
    numerator =  a*b
    denominator = math.sqrt(math.pow(a * math.sin(theta),2) + math.pow(b * math.cos(theta), 2))
    return numerator/denominator


def get_x_y_from_polar_r(radius, theta):
    x = math.cos(theta) * radius
    y = math.sin(theta) * radius
    return (x, y)