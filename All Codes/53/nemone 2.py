from math import pi
from math import pow

def p_circle(r):
    '''enter radius and recive answer:
    p_circle(2)
    >>>12.56
    '''
    return 2*pi*r

def s_circle(r):
    '''enter radius and recive answer:
    s_circle(2)
    >>>12.56
    '''
    return r**2*pi

def s_triangel(a,h):
    '''enter a from triangle and hight (a,h) to recive answer:
    s_tringle(3,2)
    >>>3
    '''
    return a*h/2

def p_triangle(a,b,c):
    '''enter a,b,c from triangle to recive answer:
    p_triangle(2,3,4)
    >>>10
    '''
    return a+b+c

def plus3(number):
    '''enter a number to riceve answer:
    plus3(2)
    >>>5
    '''
    return number+3

def cube(number):
    '''enter a number to recive the answer:
    cube(3)
    >>>27
    '''
    return pow(number,3)


    
