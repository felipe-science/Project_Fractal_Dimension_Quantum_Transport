from numpy import sqrt

N = 8


def rms(N):
    return sqrt( N*((N+1)**2)  /  (((2*N+1)**2)*(2*N+3)))

for n in range(7):
    print("var"+str(rms(n)))