import os, math
import matplotlib as mp
import isacalc as isa

os.system("cls" if os.name == "nt" else "clear")

# Wing dimensions

ChordRoot = 0.8  # m
ChordTip = 0.2  # m
TaperRatio = ChordTip / ChordRoot
Wingspan = 2.5  # m
WingArea = 1  # m^2
WetWingArea = 1 # m^2, area of wing exposed to stream lines
Sweep = math.radians(0) # degrees, converted to radians, only non 0 when transsonic +
AverageChord = WingArea / Wingspan
AR = (Wingspan ^ 2) / WingArea
XC = 0.25  # Location of center of mass in % of chord
TC = 0.14  # Maximum thickness in % of chord
QWing = 1.25

# Fuselage dimensions

FuselageLength = 0.8  # m
Height = ChordRoot * TC  # m
QFuse = 1
AFuse = (4(FuselageLength * (ChordRoot * TC)))  # m^2
F = FuselageLength / ((4 / math.pi) * AFuse)**(1/2)

# variable setups

Gamma = 1.4  # Ratio of specific heats for dry air
R = 287  # J/kgK specific gas constant for dry air
LambdaM = 60  # degrees
E = 0.7
Oswald = 1.78 * (1 - .045 * (AR)**.68) - .64
A0 = 0.104
A = A0 / ((1 + (57.3 * A0)) / (math.pi * E * AR))
Alpha = 17.5  # degrees
AlphaL0 = 0  # degrees
K = (math.pi * Oswald * AR)**(-1)

# Altitude and speed variables

Altitude = 8000 / 3.28084  # Divide by 3.28084 for ft to m conversion
Velocity = 60  # m/s

Atmosphere = isa.get_atmosphere()
Temp, Pressure, Density, SpeedSound, DynamicViscosity = isa.calculate_at_h(
    Altitude, Atmosphere
)

Mach = Velocity / SpeedSound

#Reynolds number

ReWing = (Density * Velocity * AverageChord) / DynamicViscosity
ReFuse = (Density * Velocity * FuselageLength) / DynamicViscosity

# Lift

CL = A * (Alpha - AlphaL0)



# Wing drag

# Skin Friction Coefficent Wing

if ReWing <= 100000:
    CFWing = 1.328 / (ReWing**(1/2))
else:
    CFWing = .455/(((math.log10(ReWing))**2.58) * (1 + .144*(Mach**2))**.65)

# Form Factor Wing

FFWing = (((1 + (.6/XC)) * TC) + (100 * (TC**4))) * (((1.34 * Mach)**.18) * (math.cos(Sweep))**.28)

# Wetted Wing

SWetWing = (1.977 + .52 * (TC)) * WetWingArea

# Total Wing Drag

CD0Wing = CFWing * FFWing * QWing * (SWetWing / WingArea)



# Fuselage Drag

# Skin Friction Coefficent Fuselage

if ReFuse <= 100000:
    CFFuse = 1.328 / (ReFuse**(1/2))
else:
    CFFuse = .455/(((math.log10(ReFuse))**2.58) * (1 + .144*(Mach**2))**.65)

# Form Factor Fuselage

FFFuse = (.9 + (5 / (F**1.5)) + (F/400))

# Wetted Fuselage

SWetFuse = 2(FuselageLength * (ChordRoot * TC))

# Total Fuselage Drag

CD0Fuse = CFFuse * FFFuse * QFuse (SWetFuse / WingArea)



# Total Plane Drag

CD0 = CD0Wing + CD0Fuse



# Aircraft Drag

CD = CD0 + K * (CL**2)



# Display output
print("")