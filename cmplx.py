from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import cv2

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


def complex_plane(size_real, size_complex, num_points, start_real=0, start_complex=0):
    x = np.linspace(complex(start_real), complex(size_real), num=num_points)
    y = np.linspace(complex(0, start_complex), complex(0,size_complex), num=num_points)
    XX, YY = np.meshgrid(x,y)
    XX_corrected = XX - ((start_real+size_real)/2)
    YY_corrected = np.flipud(YY) - (complex(0, ((start_complex+size_complex)/2)))
    return XX_corrected + YY_corrected

def make_fractal_image(size_real, size_complex, num_points, start_real=0, start_complex=0):
    plane = complex_plane(size_real, size_complex, num_points, start_real, start_complex)
    matrix_function = np.vectorize(lambda c: fractal(complex(0),c))
    result = matrix_function(plane)
    return result
