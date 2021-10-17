# HW7
import math

CD0 = 0.0254
K = 0.0462
SWing = 16.17  # m^2
eta = .90  # %
rho = 1.2  # kg/m^3
BSFC = 260  # g/kWh
WTakeoff = 2450 * 0.45359237  # N
WFuel0 = 2000 * 0.45359237  # N

CLCDmax = ((4 * K * CD0) ** -1) ** 0.5  # optimal value
print(CLCDmax)

Range = (eta / ((BSFC * 9.81) / 1*10**6)) * CLCDmax * math.log(WTakeoff / WFuel0) # km
print(Range)
