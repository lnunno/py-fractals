from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
# import cv2

def mandelbrot(z, c):
    return (z**2) + c

def complex_to_color(c, i):
    '''
    :param c: Complex number
    :param i: number of iterations done to get this complex number.
    '''
    return (c.real, c.imag, i)

def fractal(z, c, z_func=mandelbrot, color_func=complex_to_color):
    '''
    :return: True if this z value is in the set, False otherwise.
    '''
    num_iterations = 256
    zn = z
    for i in xrange(1,num_iterations):
        zn1 = z_func(z,c)
        if abs(zn1) > 2:
            return i
        z = zn1
    return i


def complex_plane(start_real, start_complex, end_real, end_complex, num_points):
    x = np.linspace(complex(start_real), complex(end_real), num=num_points)
    y = np.linspace(complex(0, start_complex), complex(0,end_complex), num=num_points)
    XX, YY = np.meshgrid(x,y)
    XX_corrected = XX
    YY_corrected = np.flipud(YY)
    return XX_corrected + YY_corrected

def make_mandel_array(num_points):
    plane = complex_plane(-2, -2, 1, 1, num_points)
    matrix_function = np.vectorize(lambda c: fractal(complex(0),c))
    result = matrix_function(plane)
    return result
