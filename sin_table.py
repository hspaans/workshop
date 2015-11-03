""" Generates sine table for 0 to 90 degrees (using math.sin) """
from __future__ import division
import math

DEGREES = 360
sine_table = []

def init_table():
    """ Initialize table from math.sin by step of 1 degree [0:90] """
    for i in range(0, int((DEGREES / 4) + 1)):
        sine_table.append(math.sin(2 * math.pi * i / DEGREES))
	

def sin(i):
    """ Look up sine of degree i in table """
    i = i % 360
    q = i % (DEGREES // 4)

    if i < 90:
        return sine_table[q]
    elif i < 180:
        return sine_table[90 - q]
    elif i < 270:
        return -sine_table[q]
    else:
        return -sine_table[90 - q]


def cos(i):
    """ Look up cosine of degree i in table """
    return sin(i + 90)


def tan(i):
    """ Lookup sin/cos in table and divide to get tangent """
    cos_v = cos(i)
    if cos(i) == 0:
        return float('nan')
    else:
        return sin(i) / cos_v


def asin(i):
    """ Approximate arc sine of i by neareast value in table and return it's
        index(=~ degree)
    """
    if i < -1 or i > 1:
        raise ValueError('math domain error')

    j = math.copysign(i,1)
    idx = min(range(len(sine_table)), key=lambda k: abs(sine_table[k] - j))
    return math.copysign(idx,i);


def acos(i):
    """ Approximate arc cosine of i by neareast value in table and return it's
        index(=~ degree)
    """
    return 90 - asin(i)


def atan(i):
    """ Approximate arc tangent of i by neareast value in table and return it's
        index(=~ degree), any result endinging(i > 81) in (-)90 will be rounded
        down to (-)89 as this is the fist valid result in whole degree

        Note: this an partian lookup as as the term for arcsin is calculated
        as i divided by square root of (i squared + 1)
    """
    val = asin(i / math.sqrt(i*i + 1))
    if abs(val) == 90:
        return copysign(val - 1, val)
    else:
        return val


def print_table():
    """ Print the generated sine(and cosine/tangent) tables """ 

    print('angle:      sine         cosine         tangent')
    for angle in range(0, 360 + 1):
        print('{:5d}: {: 1.10f} {: 1.10f} {:14.10f}'.
              format(angle,sin(angle),cos(angle),tan(angle)))
        

init_table()

if __name__ == '__main__':
    print_table()
