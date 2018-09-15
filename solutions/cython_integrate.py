%%cython -a

cdef double f(double x):
    return x**2-x

def integrate_f(double a, double b, int N):
    cdef int i
    cdef double dx, s
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx
