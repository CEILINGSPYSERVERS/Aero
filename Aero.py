import os, math
import isacalc as isa

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
QFuse = 1
AFuse = 0.8704  # m^2
SWetFuse = 0.6144  # m^2
F = FuselageLength / (0.8 * 0.2 * 0.8)

# variable setups

Gamma = 1.4  # Ratio of specific heats for dry air
R = 287  # J/kgK specific gas constant for dry air
E = 0.85
Oswald = 1.78 * (1 - 0.045 * (ARD) ** 0.68) - 0.64
A0 = 0.0941
Cd0 = 0.007221496
A = A0 / (1 + ((57.3 * A0) / (math.pi * E * ARD)))
Alpha = 18.2  # degrees
AlphaL0 = 0  # degrees
K = (math.pi * Oswald * ARD) ** (-1)

# Altitude and speed variables

Altitude = 2000  # m
Velocity = 60  # m/s

Atmosphere = isa.get_atmosphere()
Temp, Pressure, Density, SpeedSound, DynamicViscosity = isa.calculate_at_h(
    Altitude, Atmosphere
)

Mach = Velocity / SpeedSound

# Reynolds number

ReWing = (Density * Velocity * AverageChord) / DynamicViscosity
ReFuse = (Density * Velocity * FuselageLength) / DynamicViscosity

# Weight
SurfaceArea = 2.809 # m^2
Mass = (((SurfaceArea * .001) * 1930) + .3 + .0158 + .5) # kg
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


# Total Plane Drag

CD0 = CD0Wing + CD0Fuse


# Aircraft Drag

CD = CD0 + K * (CL ** 2)


# Display output
print(f"Altiutude {Altitude} meters")
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

CL32CDMax = (3**(3/4)) / (4 * (CD0**(1/4) * K**(3/4)))
CLCDMax = math.sqrt(1 / (4 * K * CD0))

# Plane thrust vars
BCurrent = 7  # Ah
BVoltage = 12  # V
BEnergy = BCurrent * BVoltage  # Wh
EtaProp = .90
EtaMotor = .90

MaxRange = ((BEnergy * EtaProp * EtaMotor) / Weight) * CLCDMax  # m
MaxEndurane = ((BEnergy * EtaProp * EtaMotor * math.sqrt(Density * WingArea)) / (math.sqrt(2) * Weight**(3/2))) * CL32CDMax  # hr

print(f"Max Range {MaxRange} meters")  # THIS IS WRONG
print(f"Max Endurance {MaxEndurane} hours")  # THIS IS WRONG
