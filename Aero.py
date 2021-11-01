import os, math
import isacalc as isa
import matplotlib.pyplot as pl
import numpy as np

os.system("cls" if os.name == "nt" else "clear")

# Wing dimensions

ChordRoot = 0.8  # m
ChordTip = 0.16  # m
TaperRatio = ChordTip / ChordRoot
Wingspan = 2.5  # m
WingArea = 1.08236  # m^2
SWetWing = 0.82636  # m^2, area of wing exposed to stream lines
Sweep = math.radians(0)  # degrees, converted to radians, only non 0 when transsonic +
AverageChord = WingArea / Wingspan
ARD = 4 / math.tan(math.radians(90 - 60.7))
AR = (Wingspan ** 2) / WingArea
XC = 0.25  # Location of center of mass in % of chord
TC = 0.20  # Tip thickness in % of chord NACA 0020
QWing = 1

# Fuselage dimensions

FuselageLength = 0.8  # m
Height = ChordRoot * TC  # m
QWingFuse = 1
# AWingFuse = 0.8704  # m^2
# SWetWingFuse = 0.6144  # m^2
SWetWingFuse = 0.535  # m^2
F = FuselageLength / (0.8 * 0.2 * 0.8)

# variable setups

Gamma = 1.4  # Ratio of specific heats for dry air
R = 287  # J/kgK specific gas constant for dry air
E = 0.85
Oswald = 1.78 * (1 - 0.045 * (ARD) ** 0.68) - 0.64
A0 = 0.0955
Cd0 = 0.00717
A = A0 / (1 + ((57.3 * A0) / (math.pi * E * ARD)))
Alpha = 17.8  # degrees
AlphaL0 = 0  # degrees
K = (math.pi * Oswald * ARD) ** (-1)

# Altitude and speed variables

Altitude = 2000  # int(input("Altitude: "))  # m
Velocity = 30  # int(input("Velocity: "))  # m/s

Atmosphere = isa.get_atmosphere()
Temp, Pressure, Density, SpeedSound, DynamicViscosity = isa.calculate_at_h(
    Altitude, Atmosphere
)

Mach = Velocity / SpeedSound

# Reynolds number

ReWing = (Density * Velocity * AverageChord) / DynamicViscosity
ReWingFuse = (Density * Velocity * FuselageLength) / DynamicViscosity

#print ("----------------------------------------------------------------------------------------")

NBats = 8 # int(input("#Batteries: "))

# Weight
BodyArea = 2.809  # m^2
Mass = (
    ((BodyArea * 0.001) * 1930) + (0.349 * 2) + (0.300 * NBats) + 0.0158 + 0.5 + 2.5
)  # kg
Weight = Mass * 9.81

# Lift

CL = A * (Alpha - AlphaL0)


# Wing drag

# Skin Friction Coefficent Wing

if ReWing <= 100000:
    CFWing = 1.328 / (ReWing ** (1 / 2))
else:
    CFWing = 0.455 / (
        ((math.log10(ReWing)) ** 2.58) * (1 + 0.144 * (Mach ** 2)) ** 0.65
    )

# Form Factor Wing

FFWing = (((1 + (0.6 / XC)) * TC) + (100 * (TC ** 4))) * (
    ((1.34 * Mach) ** 0.18) * (math.cos(Sweep)) ** 0.28
)

# Total Wing Drag

CD0Wing = CFWing * FFWing * QWing * (SWetWing / WingArea)


# Fuselage Drag

# Skin Friction Coefficent WingFuse

if ReWingFuse <= 100000:
    CFWingFuse = 1.328 / (ReWing ** (1 / 2))
else:
    CFWingFuse = 0.455 / (
        ((math.log10(ReWing)) ** 2.58) * (1 + 0.144 * (Mach ** 2)) ** 0.65
    )

"""
# Form Factor Wing

FFWingFuse = (((1 + (0.6 / XC)) * TC) + (100 * (TC ** 4))) * (
    ((1.34 * Mach) ** 0.18) * (math.cos(Sweep)) ** 0.28
)
"""

FFWingFuse = Cd0

# Total Wing Drag

CD0WingFuse = CFWingFuse * FFWingFuse * QWingFuse * (SWetWingFuse / WingArea)

"""
# Skin Friction Coefficent Fuselage

if ReFuse <= 100000:
    CFFuse = 1.328 / (ReFuse ** (1 / 2))
else:
    CFFuse = 0.455 / (
        ((math.log10(ReFuse)) ** 2.58) * (1 + 0.144 * (Mach ** 2)) ** 0.65
    )

# Form Factor Fuselage

FFFuse = 0.9 + (5 / (F ** 1.5)) + (F / 400)

# Wetted Fuselage

SWetFuse = 2 * (FuselageLength * ChordRoot * TC)

# Total Fuselage Drag

CD0Fuse = CFFuse * FFFuse * QFuse * (SWetFuse / WingArea)
"""


# Total Plane Drag

CD0 = CD0Wing + CD0WingFuse


# Aircraft Drag

CD = CD0 + K * (CL ** 2)


# Display output
print(f"Altiutude {Altitude} meters")
print(f"Velocity {Velocity} m/s")
print(f"RE Wing {ReWing}")
print(f"RE Fuselage {ReWingFuse}")
print(f"Mach {Mach}")
print(f"Mass {Mass} kg")
print(f"Weight {Weight} N")
print(f"Cl {A0}")
print(f"Cd {Cd0}")
print(f"CL {CL}")
print(f"CD {CD}")


# Efficency Ratios

""" 
Max Endurance prop ((Cl^(3/2))/Cd)max

VInf = sqrt((2 * W/RhoInf * S) / (k / 3 * CD0))
Optimal Value = 3^(3/4) / (4 * (CD0^(1/4)) * (k)^(3/4))


Max Range Prop
Max Endurance Jet

VInf = sqrt((2 * W/RhoInf * S) / (k / CD0))
Optimal Value = sqrt(1 / (4 * k * CD0))


Max Range Jet

VInf = sqrt((2 * W/RhoInf * S) / (3 * k / CD0))
Optimal Value = (3/4) * (1 / (3 * k * CD0^3))^(1/4)

"""

CL32CDMax = (3 ** (3 / 4)) / (4 * (CD0 ** (1 / 4) * K ** (3 / 4)))
CLCDMax = math.sqrt(1 / (4 * K * CD0))

# Plane thrust vars
BCurrent = 7  # Ah
BVoltage = 12  # V
BEnergy = NBats * (BCurrent * BVoltage) * 3600  # J
EtaProp = 0.70
EtaMotor = 0.80

MaxRange = (((BEnergy * EtaProp * EtaMotor) / Weight) * CLCDMax) / 1000  # km

MaxEndurane = (
    (
        (BEnergy * EtaProp * EtaMotor * math.sqrt(Density * WingArea))
        / (math.sqrt(2) * Weight ** (3 / 2))
    )
    * CL32CDMax
) / 3600  # hr

print(f"Max Range {MaxRange} km")
print(f"Max Endurance {MaxEndurane} hours")

# Velocity for max range and endurance

VRangeMax = math.sqrt(
    ((2 * Weight) / (Density * WingArea)) * (math.sqrt(K / (3 * CD0)))
)

VEnduranceMax = math.sqrt(((2 * Weight) / (Density * WingArea)) * (math.sqrt(K / CD0)))

print(f"Velocity for maximum range: {VRangeMax} m/s")
print(f"Velocity for maximum endurance: {VEnduranceMax} m/s")

#VStall = math.sqrt((2 * Weight) / (Density * WingArea * CLCDMax))
#print(VStall) # Id bet this is wrong


AeroPower = EtaMotor*EtaProp*(2*.32*12*3600)
print(f"Aero Power: {AeroPower} J")
SFLPowR = CD * Velocity
print(f"Steady level Flight Power Required: {SFLPowR} J")


# More Vars

AltMax = 3000  # m
RhoASL = 0.95  # kg/m^3
TempASL = 294  # degree K
Grav = 9.81  # m/s^2
RConst = 287  # J/(kg*degree K)
AConst = -6.5 * 10 ** -3

# Rate Of Climb

Z = 1 + math.sqrt(1 + (3 / ((CLCDMax ** 2) * ((AeroPower / Weight) ** 2))))


VROCMax = ((((AeroPower / Weight) * (Weight / SWetWing)) / (3 * RhoASL * CD0)) * Z) ** 0.5

ClimbRateMax = (
    ((((Weight / SWetWing) * Z) / (3 * RhoASL * CD0)) ** 0.5)
    * ((AeroPower / Weight) ** (3 / 2))
    * (1 - (Z / 6) - (3 / (2 * ((AeroPower / Weight) ** 2) * ((CLCDMax) ** 2) * Z)))
)

print(f"ClimbRateMax: {ClimbRateMax}")
print(f"VROCMax: {VROCMax}")

"""
ThetaMaxClimbRate = math.degrees(math.asin(ClimbRateMax / VROCMax))
print(ThetaMaxClimbRate)

MaxClimbAngle = math.asin((AeroPower / Weight) - math.sqrt(4 * CD0 * K))
print(math.degrees(MaxClimbAngle))

VMaxClimbAngle = math.sqrt((2/RhoASL)*((K/CD0)**.5)*(Weight/WingArea)*math.cos(MaxClimbAngle))
print(VMaxClimbAngle)

# Altitude dependent stuff

ThrustReq = (.5*RhoASL*VROCMax**2)*WingArea*CD0+(K*(Weight**2)*math.cos(math.radians(ThetaMaxClimbRate)))/((.5*RhoASL*VROCMax**2)*WingArea)

print(ThrustReq)

ThrustAvail = (.5*RhoASL*VROCMax**2)*WingArea*CD0+(K*(Weight**2)/((.5*RhoASL*VROCMax**2)*WingArea))

print(ThrustAvail)


Alts = np.arange(0, AltMax + 100, 100)
YAxis = Alts

XAxis = []

for Var1 in Alts:
    TempEq = TempASL + AConst * (Var1 - 0)
    RhoEq = RhoASL * (TempEq / TempASL) ** ((-Grav / (AConst * RConst)) - 1)
    ThrustAtAlt = AeroPower * (RhoEq / RhoASL)
    XAxis.append(ThrustAtAlt)


fig, ax = pl.subplots()
ax.plot(XAxis, YAxis)

ax.set(xlabel="Thrust (kN)", ylabel="Altitude (m)", title="Turbo Jet Thrust vs Altitude")
ax.grid()

pl.show()
"""