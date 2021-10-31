import matplotlib.pyplot as pl
import numpy as np
import math

# ThrustASL = 25.7  # kN
ThrustASL = 25700  # N
AltASL = 0  # m
AltMax = 11000  # m
RhoASL = 0.95  # kg/m^3
TempASL = 294  # degree K
Grav = 9.81  # m/s^2
RConst = 287  # J/(kg*degree K)
AConst = -6.5 * 10 ** -3
Weight = 135000  # N
BSpan = 22.04  # m
SArea = 50.4  # m^2
CD0 = 0.03
Oswald = 0.8


AR = (BSpan ** 2) / SArea

K = 1 / (math.pi * Oswald * AR)

LDMax = math.sqrt(1 / (4 * K * CD0))

Z = 1 + math.sqrt(1 + (3 / ((LDMax ** 2) * ((ThrustASL / Weight) ** 2))))


VROCMax = ((((ThrustASL / Weight) * (Weight / SArea)) / (3 * RhoASL * CD0)) * Z) ** 0.5

print(VROCMax)

ClimbRateMax = (
    ((((Weight / SArea) * Z) / (3 * RhoASL * CD0)) ** 0.5)
    * ((ThrustASL / Weight) ** (3 / 2))
    * (1 - (Z / 6) - (3 / (2 * ((ThrustASL / Weight) ** 2) * ((LDMax) ** 2) * Z)))
)

print(ClimbRateMax)

ThetaMaxClimbRate = math.degrees(math.asin(ClimbRateMax / VROCMax))
print(ThetaMaxClimbRate)

MaxClimbAngle = math.asin((ThrustASL / Weight) - math.sqrt(4 * CD0 * K))
print(math.degrees(MaxClimbAngle))

VMaxClimbAngle = math.sqrt((2/RhoASL)*((K/CD0)**.5)*(Weight/SArea)*math.cos(MaxClimbAngle))
print(VMaxClimbAngle)


"""
ThrustReq = (.5*RhoASL*VROCMax**2)*SArea*CD0+(K*(Weight**2)*math.cos(math.radians(Theta)))/((.5*RhoASL*VROCMax**2)*SArea)

print(ThrustReq)

ThrustAvail = (.5*RhoASL*VROCMax**2)*SArea*CD0+(K*(Weight**2)/((.5*RhoASL*VROCMax**2)*SArea))

print(ThrustAvail)
"""


"""
Alts = np.arange(0, AltMax + 100, 100)
YAxis = Alts

XAxis = []

for Var1 in Alts:
    TempEq = TempASL + AConst * (Var1 - AltASL)
    RhoEq = RhoASL * (TempEq / TempASL) ** ((-Grav / (AConst * RConst)) - 1)
    ThrustAtAlt = ThrustASL * (RhoEq / RhoASL)
    XAxis.append(ThrustAtAlt)


fig, ax = pl.subplots()
ax.plot(XAxis, YAxis)

ax.set(xlabel="Thrust (kN)", ylabel="Altitude (m)", title="Turbo Jet Thrust vs Altitude")
ax.grid()

pl.show()
#fig.savefig("test.png")
"""
