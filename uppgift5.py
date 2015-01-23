import math

Rl = 50
R3 = 4650
R4 = 20000
R5 = 75000
R6 = 300
Idss = 10 * pow(10, -3)
Up = -3.5
Ugsq = Up * (math.sqrt(0.001/Idss) - 1)
Ra = (Rl*R6)/(Rl+R6)
Rb = 1/((1/R3)+(1/R4)+(1/R5))
print("Rb: " + str(Rb))
print("Ugsq: " + str(Ugsq))


Gm = ((-2*Idss)/Up)*(1-(Ugsq/Up))
h21 = 100
h11 = 2000

Uut = -((Ra * Gm * h21 * Rb)/((Rb + h11) + (Ra * (1+h21))))
print("Uut: " + str(Uut))
