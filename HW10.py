import math

Mass = 1111
G = 9.81
Weight = Mass * G
SWingArea = 16.17
Rho = 1.225
CLMax = 1.6
CLRolling = 0.35
K = 0.05
CD0 = 0.05
CD = CD0 + K * (CLRolling ** 2)
MuRolling = 0.02

VStall = math.sqrt((2 * Weight) / (Rho * SWingArea * CLMax))

VLo = 1.2 * VStall
VInf = 0.7 * VLo

qInf = 0.5 * Rho * (VInf ** 2)

Lift = qInf * SWingArea * CLRolling
Drag = qInf * SWingArea * CD

Thrust = 120000/VInf #Power = 120kW / VInf = thrust for prop

a = (Thrust - Drag - MuRolling * (Weight - Lift))/Mass

SGround = (1.44 * (Weight ** 2)) / (G * Rho * SWingArea * CLMax * (Thrust - Drag - MuRolling * (Weight - Lift)))

print(f"ground distance: {SGround} meters")

Radius = (1.44 * (VStall ** 2)) / (0.15 * G)
#print(f"radius: {Radius} meters")

HeightTr = Radius - (Radius * math.cos(math.radians(5)))
STr = Radius * math.sin(math.radians(5))
print(f"transition distance {STr} meters")
Ha = 35 - HeightTr
Sa = Ha / math.tan(math.radians(5))
print(f"air distance {Sa} meters")

STakeoff = SGround + STr + Sa
print(f"takeoff distance {STakeoff} meters")

#LANDING NOW

print("-----------------------------")

Angle = math.radians(3)
VFlare = 1.23*VStall
VTD = 1.3*VStall
MuBraking = .4

RadiusL = VFlare**2 / (.15*G)
print(RadiusL)

HeightFlare = RadiusL - RadiusL * math.cos(Angle)
FlareDistance = RadiusL * math.sin(Angle)
ApproachD = (50 - HeightFlare) / math.tan(Angle)

print(f"Approach D = {ApproachD} meters")
print(f"FlareDistance = {FlareDistance} meters")

SGLanding = (1.69*(Weight**2)) / (G*Rho*SWingArea*CLMax*(Drag + MuBraking*(Weight-Lift)))
print(f"Ground distance landing {SGLanding} meters")

SLanding = FlareDistance + ApproachD + SGLanding
print(f"Landing distance = {SLanding} meters")
