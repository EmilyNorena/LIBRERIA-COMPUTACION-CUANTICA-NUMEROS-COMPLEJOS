import math
def suma(a, b):
    r = a[0] + b[0]
    i = a[1] + b[1]
    return r, i
def mult(a, b):
    r = a[0]* b[0]- (a[1]*b[1])
    i = a[0]*b[1] + b[0]*a[1]
    return r, i
def resta(a,b):
    r = a[0] - b[0]
    i = a[1] - b[1]
    return r, i
def div(a, b):
    r = (a[0]*b[0] + a[1]*b[1]) / (b[0]**2 + b[1]**2)
    i = (b[0]*a[1] - a[0]*b[1]) / (b[0]**2 + b[1]**2)
    return r, i
def modulo(a):
    r = (a[0]**2 + a[1]**2) ** 0.5
    return r
def conjugado(a):
    r = a[0]
    i = -a[1]
    return r, i
def cartesiano_polar(a):
    m = (a[0]**2 + a[1]**2) ** 0.5
    f = math.atan(a[1]/a[0])
    return m, f
def polar_cartesiano(a):
    r = a[0]*math.cos(a[1])
    i = a[0]*math.sin(a[1])
    return r, i
def fase(a):
    f = math.atan(a[1]/a[0])
    return f
