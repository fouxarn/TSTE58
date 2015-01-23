import cmath
import math

Yi = complex((1/math.sqrt(2)), -(1/math.sqrt(2)))
Yi = Yi * pow(10, 2)
# Yi = Yi * pow(10, -2)
print("Yi: " + str(Yi))

Y1 = complex(1/950, 0)
# Y1 = Y1 / pow(10, -2)
print("Y1: " + str(Y1))

Y2 = complex(1750, 480)
Y2 = 1/Y2
# Y2 = Y2 * pow(10, -2)
print("Y2: " + str(Y2))

Y3 = complex(0, (0.86 * pow(10, -3)))
# Y3 = Y3 * pow(10, -2)
print("Y3: " + str(Y3))

Yp = complex(1/5.5, -(1/8.6))
Yp = Yp * pow((1/10), 2)
# Yp = Yp * pow(10, -2)
# Yp = math.pow((1/2), 2) * Yp
print("Yp: " + str(Yp))

Ytot = Yi + Y1 + Y2 + Y3 + Yp
# print("Ytot: " + str(Ytot))
# print(cmath.polar(Ytot))
Ytot = Ytot / pow(10, -2)
print("Ytot: " + str(Ytot))
print(cmath.polar(Ytot))

U0 = cmath.exp(complex(0, -cmath.pi))/Ytot
print("U0: " + str(cmath.polar(U0)))

U = cmath.polar(U0)
U = list(U)
U[0] = U[0]/-10
print("U: " + str(U))


Ue = U[0]/math.sqrt(2)
print("Ue: " + str(Ue))

P = pow(Ue, 2)/5.5
print("P: " + str(P))

Q = pow(Ue, 2)/(8.6*pow(10, -3))
print("Q: " + str(Q))
