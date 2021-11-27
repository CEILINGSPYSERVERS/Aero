import numpy as np
import isacalc as isa
from numpy import sqrt,sin,cos,tan,log10,exp
from numpy import pi
import os

import pint
ur=pint.UnitRegistry()

os.system("cls" if os.name == "nt" else "clear")

# Atmosphere data will be necessary to determine aircraft
# performance at altitude, specifically density (needed
# for q) and viscosity (needed for Reynolds number).

"""
Atmosphere = isa.get_atmosphere()
Temp, Pressure, Density, SpeedSound, DynamicViscosity = isa.calculate_at_h(
    cruise_alt, Atmosphere
)

Mach = Velocity / SpeedSound
"""

# begin atmosphere input parameters 
cruise_alt=2000*ur.m; # cruise altitude meters 
v_cruise_approx=30*ur.m/ur.s; # approximate cruise speed (m/s); to be used for Reynolds number calculations
airport_alt=0*ur.m; # meters
a1=-6.5e-3*ur.K/ur.m; # Temperature lapse rate below 11 km, in deg K/m
Temp0=288.15*ur.K; # Nominal sea level temperature (std. atmosphere), deg K
rho0=1.225*ur.kg/ur.m**3; # Air density at sea level, kg/m^3
h0=0.*ur.m # sea level, meters
Ratm=287*ur.J/(ur.kg*ur.K); # ideal gas constant J/(kg*K) 
g_planet=9.8*ur.m/ur.s**2; # acceleration due to gravity m/s^2  
gamma_atm = 1.4; # ratio of specific heats
Beta=1.458e-6*ur.kg/(ur.s*ur.m*ur.K**0.5); # kg/(s*m*sqrt(K)) from 1976 US standard atmosphere, page 19
Suth = 110.4*ur.K; # deg K, Sutherland's constant, from 1976 US standard atmosphere, page 1
# end atmosphere input parameters 


# now calculate Tcruise, Tairport, rhocruise, rhoairport,
# mucruise, muairport, c_soundcruise

Tcruise = Temp0 + cruise_alt*a1; # Calculate temperature at cruise altitude based on lapse rate
Tairport = ; # Calculate temperature at airport altitude based on lapse rate
rhocruise = rho0*(Tcruise/Temp0)**(-g_planet/(a1*Ratm)-1); # Calculate density at cruise altitude based on standard atmosphere formula
rhoairport = ; # Calculate density at cruise altitude based on standard atmosphere formula

mucruise = (Beta*Tcruise**(3/2))/(Tcruise+Suth);  # Dynamic viscosity from 1976 US standard atmosphere, page 19, eq 51.... Valid below 86 km
muairport = (Beta*Tairport**(3/2))/(Tairport+Suth);  # Dynamic viscosity from 1976 US standard atmosphere, page 19, eq 51.... Valid below 86 km
c_soundcruise = sqrt(gamma_atm*Ratm*Tcruise).to(ur.m/ur.s);

print(f'## atmosphere output results');
print(f'Tcruise={Tcruise:.4g}; ## cruise temperature (deg K)');
print(f'Tairport={Tairport:.4g}; ## airport temperature (deg K)');
print(f'rhocruise={rhocruise:.4g}; ## cruise density (kg/m^3)');
print(f'rhoairport={rhoairport:.4g}; ## airport density (kg/m^3)');
print(f'mucruise={mucruise:.4g}; ## cruise viscosity (kg/m^3)');
print(f'muairport={muairport:.4g}; ## airport viscosity (kg/m^3)');
print(f'c_soundcruise={c_soundcruise:.4g}; ## speed of sound at cruise (m/s)');
print(f'## end atmosphere output results\n');

# rough cruise flight parameters: inputs
Swing = *ur.m**2; # Wing area (m^2)
b = 2.5*ur.m; # wing span (m)
# end rough cruise flight parameters: inputs

avgchord = ; # average wing chord (m)
WingRe_cruise = ; # Wing Reynolds number at cruise
M_cruise = ; # Mach number at cruise

# These are needed inputs for XFLR5 to calculate airfoil parameters
# (use cruise values because ultimate performance is usually most
# significant at cruise) 
print(f'## rough cruise flight parameter results');
print(f'avgchord={avgchord:.4g}; ## average wing chord (m)');
print(f'WingRe_cruise={WingRe_cruise:.4g}; ## typical cruise Reynolds number');
print(f'M_cruise={M_cruise:.4g}; ## typical cruise Mach number');
print(f'## end rough cruise flight parameter results\n');



# Suggest load and plot your XFLR5 data here ...


# airfoil input parameters (2D/3D)
a0 = /ur.deg; # lift slope in 1/deg
cd0 = ; # zero lift drag coefficient
zeroliftalpha = *ur.deg; # zero lift angle of attack (deg) (alpha_L=0)
alphastall = *ur.deg;# stall angle of attack (deg)
wing_sweepbackangle=*ur.deg; # wing sweep back angle (degrees)
e = ; # estimated span efficiency factor (airfoil alone)
# end airfoil input parameters (2D/3D)



# 2D lift model is cl = a0(alpha-zeroliftalpha)
# Treat cl,max as a0(alphastall-zeroliftalpha)
# 2D drag model is cd = cd0

# 3D wing lift model is CL = a(alpha-zeroliftalpha)
# 3D wing drag model is CD = CD0_wing + kCL^2

# perform calculations of CD0_wing, a, k, CL,max
CD0_wing= ; # this is the same as 2D cd0, remember?
AR = ; # aspect ratio
a=;
k=;  # This is the wing k, based on span efficiency factor e,
     # not the the whole airplane K based on Oswald efficiency eo
CLmax=;

print(f'## 3D airfoil output results');
print(f'CD0_wing={CD0_wing:.4g}; ## Wing zero lift 3D drag');
print(f'a={a:.4g}; ## 1/deg');
print(f'k={k:.4g}; ## 3D airfoil quadratic drag coefficient');
print(f'CLmax={CLmax:.4g}; ## Maximum CL prior to stall');
print(f'## end 3D airfoil output results\n');



# begin drag build-up/whole airplane input parameters
# Swing already specified above. 
wing_Q=; # Wing interference factor

fuselage_length = *ur.m; # fuselage length (m)
fuselage_dmax = *ur.m; # fuselage max diameter (m)
fuselage_Swet = ; # fuselage wetted area (m^2) 

tail_Sexposed=*ur.m**2;  # Tail planform area (m^2) (total for horizontal + vertical stabilizer)... or you can split them apart and do them separately
tail_toverc=;   # Tail thickness over chord
tail_xoverc;   # Tail position of maximum thickness over chord
tail_sweepbackangle=*ur.deg; # Tail sweep back angle (degrees)
tail_avgchord = *ur.m;  # tail average chord (m)
tail_Q=;


num_engines_drag = ; # number of external engines in pods for drag calculation
engine_length = *ur.m; # (m)
engine_dmax = *ur.m; # (m)  # engine max diameter  (m)
engine_Swet = ; # Wetted area around engine nacelle
engine_Q=; # Engine interference factor


# end drag build-up/whole airplane input parameters



# Now calculate the drag build-up/whole airplane
# parameters based on your 2D/3D airfoil parameters/results
# and the above parameters

# Have CD0_wing from above (but don't forget to consider wing
# interference factor when adding it into CD0)
fuselageRe_cruise= ; 
fuselage_Cf= ; 
fuselage_f= ;
fuselage_FF= ;

CD0_fuselage=  ; 

print(f'## fuselage drag results');
print(f'fuselageRe_cruise={fuselageRe_cruise:.4g};');
print(f'fuselage_Cf={fuselage_Cf:.4g};');
print(f'fuselage_f={fuselage_f:.4g};');
print(f'fuselage_FF={fuselage_FF:.4g};');
print(f'CD0_fuselage={CD0_fuselage:.4g};');
print(f'## end fuselage drag results\n');


tailRe_cruise=
tail_Swet=
tail_Cf= 
tail_FF=

CD0_tail=; # include interference factor

print(f'## tail drag results');
print(f'tailRe_cruise={tailRe_cruise:.4g};');
print(f'tail_Cf={tail_Cf:.4g};');
print(f'tail_FF={tail_FF:.4g};');
print(f'CD0_tail={CD0_tail:.4g};');
print(f'## end tail drag results\n');


engineRe_cruise=;
engine_Cf=; 

engine_f=;
engine_FF=;
CD0_engines=; # include all engines and interference factors

print(f'## engine drag results');
print(f'engineRe_cruise={engineRe_cruise:.4g};');
print(f'engine_Cf={engine_Cf:.4g};');
print(f'engine_f={engine_f:.4g};');
print(f'engine_FF={engine_FF:.4g};');
print(f'CD0_engines={CD0_engines:.4g};');
print(f'## end engine drag results\n');

CD0_misc=; # Other sources of CD0 drag
CD0= ; # Whole airplane CD0... don't forget to include wing interference factor
eo = ; # estimated Oswald efficiency factor (entire airplane)

K=; # Whole airplane K


print(f'## drag buildup output results');
print(f'CD0_misc={CD0_misc:.4g}; ## Other wing-referenced drag contributions');
print(f'CD0={CD0:.4g}; ## Whole airplane CD0');
print(f'eo={eo:.4g}; ## Estimated Oswald efficiency (entire airplane)');
print(f'K={K:.4g}; ## Whole airplane quadratic drag coefficient');
print(f'## end drag buildup output results\n');
# Your whole airplane drag model is CD=CD0+KCL^2
# Your whole airplane lift model is unchanged from the wing


# Performance calculations for a typical mission profile:
# Takeoff... climb... cruise... loiter... land


# begin performance input parameters
Wzerofuel = *ur.N; # Loaded, zero-fuel weight (N)   
Wfuel=*ur.N; # Initial fuel load (N)
m=; # Engine thrust/power altitude dependence exponent

### For a Jet
Ta_airport = *ur.N; # Thrust available (airport,max)
TSFC = *ur.N/ur.s/ur.N; # Thrust-specific fuel consumption in (N/s)/N

### alternatively, for a Prop
Pa_airport = *ur.W; # Power available (airport, max)
BSFC = *ur.N/ur.s/ur.W; # Brake specific fuel consumption in (N/s)/W
eta_pr =; # Propeller efficiency factor


# end performance input parameters

LovDmax = ; # (L/D)max
CL12ovCDmax = ; # (CL^(1/2)/CD)max
CL32ovCDmax = ; # (CL^(3/2)/CD)max

print(f'## simple performance output results');
print(f'LovDmax = {LovDmax:.4g}; ## (L/D)max');
print(f'CL12ovCDmax = {CL12ovCDmax:.4g}; ## (CL^(1/2)/CD)max');
print(f'CL32ovCDmax = {CL32ovCDmax:.4g}; ## (CL^(3/2)/CD)max');
print(f'## end simple performance output results\n');


# Takeoff

# takeoff input parameters
n_takeoff = ; # takeoff load factor (typically 1.15)
vlo_factor = ; # liftoff velocity relative to stall (typically 1.1)
takeoffclimbangle = *ur.deg; # gamma (deg); typically 5 deg.
mu_r = ; # Rolling friction coefficient
alpha_wheelsdown = *ur.deg; # angle of attack when wheels on runway (deg)
# end takeoff input parameters


v_stall_takeoff = ; # v_stall on takeoff (fully fueled) (m/s)
v_lo = ; # liftoff velocity (m/s)
CL_wheelsdown = ;
D_accel = ;
L_accel = ;

a_takeoff = ; # acceleration at takeoff (m/s^2), calculated @ v=0.7 v_lo
sg = ; # ground distance (m) = v_lo^2/(2*a_takeoff) 
R_takeoffpullup = ; # radius of pull-up maneuver (m)
str = ; # distance for transition to flight (m)
htr = ; # height for transition to flight (m)
scl = ; # climb distance to clear 35' (10.7 m) obstacle (if positive)
s_takeoff = ; # total takeoff distance

print(f'## takeoff output results');
print(f'v_stall_takeoff={v_stall_takeoff:.4g}; ## v_stall on takeoff (fully fueled) (m/s)');
print(f'v_lo={v_lo:.4g}; ## liftoff velocity (m/s)');
print(f'a_takeoff={a_takeoff:.4g}; ## takeoff acceleration (m/s^2)');
print(f'sg={sg:.4g}; ## ground distance (m)');
print(f'str={str:.4g}; ## transition distance (m)');
print(f'htr={htr:.4g}; ## transition height (m)');
print(f'scl={scl:.4g}; ## climb distance (m)');
print(f's_takeoff={s_takeoff:.4g}; ## takeoff distance (m)');
print(f'## end takeoff output results\n');


# Climb to cruising altitude

Max_RoC_airport = ; # maximum rate of climb (airport altitude) (m/s)
Ta_cruise = ; # Thrust available, max (cruise altitude) (N) (jet only)
Pa_cruise = ; # Power available, max (cruise altitude) (W) (prop only)
Max_RoC_cruise = ; # maximum rate of climb (cruise altitude) (m/s)

# Service ceiling is define as the height where the max rate of climb
# falls below 100 ft/m (.508 m/s)
# Is your cruise altitude above the service ceiling? (this next
# line will cause an error if it is)
assert(Max_RoC_cruise > .508 * ur.m/ur.s); 

# Estimate time-to-climb using the average of the cruise and airport RoC's.
# (time = distance/rate )
TimeToClimb = ; # (s)
# Fuel use in climb at max thrust would be Power or Thrust available (average)
# multiplied by BSFC or TSFC as appropriate, multiplied by time
Wclimbfuel = ;# fuel used during climb

Wfuel_after_climb = ; # Weight of fuel remaining after initial climb (N)

print(f'## climb output results');
print(f'Max_RoC_airport={Max_RoC_airport:.4g}; ## max rate of climb at airport altitude (m/s)');

# jet only:
print(f'Ta_cruise={Ta_cruise:.4g}; ## max thrust available at cruise altitude (N)');
# prop only 
print(f'Pa_cruise={Pa_cruise:.4g}; ## max power available at cruise altitude (W)');


print(f'Max_RoC_cruise={Max_RoC_cruise:.4g}; ## max rate of climb at cruise altitude (m/s)');
print(f'TimeToClimb={TimeToClimb:.4g}; ## time to climb to cruise altitude (s)');
print(f'Wclimbfuel={Wclimbfuel:.4g}; ## Weight of fuel expended during climb (N)');
print(f'Wfuel_after_climb={Wfuel_after_climb:.4g}; ## Weight of fuel remaining after climb (N)');
print(f'## end climb output results\n');


# cruise input parameter
CruiseDist = ; # Cruise distance (m) 
# end cruise input parameter

# (In a battery powered aircraft you would be tracking battery capacity
# instead of weight)

# You can find the fuel used in (optimal) cruise by plugging CruiseDist
# into the appropriate range equation. W1 would be your
# (Wfuel_after_climb+Wzerofuel). Then solve for W2, which is
# equivalent to (Wfuel_after_cruise+Wzerofuel)
Wfuel_after_cruise = ; # (N)
	     

v_cruise = ;   # Get a typical cruise velocity by finding the velocity that
               # Gives you the optimal cruise range at the average of W1 and
  	       # W2.

M_cruise=;

print(f'## cruise output results');
print(f'Wfuel_after_cruise={Wfuel_after_cruise:.4g}; ## Weight of fuel remaining after cruise (N)');
print(f'v_cruise={v_cruise:.4g}; ## averaged cruise velocity (m/s)');
print(f'M_cruise={M_cruise:.4g}; ## Approximate cruise mach number');
print(f'## end cruise output results\n');

assert(M_cruise < 0.85); # Equations we are using assume speed significantly below Mach 1


# Loiter
# loiter input parameter
LoiterTime = *ur.s; # Loiter time (s)
# end loiter input parameter

# You can find the fuel used in (optimal) loiter by plugging LoiterTime
# into the appropriate endurance equation. W1 would be your
# (Wfuel_after_cruise+Wzerofuel). Then solve for W2, which is
# equivalent to (Wfuel_after_loiter+Wzerofuel)
Wfuel_after_loiter=; # (N)


v_loiter = ; # Get a typical loiter velocity by finding the velocity that
             # Gives you the optimal loiter time at the average of W1 and
	     # W2.

# Also a good idea to check that your v_loiter > v_stall
v_stall_loiter = ; # stall speed at loiter altitude/avg. weight
       
assert(v_loiter >= v_stall_loiter); # will fail if v_loiter < v_stall 

print(f'## loiter output results');
print(f'Wfuel_after_loiter={Wfuel_after_loiter:.4g}; ## Weight of fuel remaining after loiter (N)');
print(f'v_loiter={v_loiter:.4g}; ## averaged loiter velocity (m/s)');
print(f'v_stall_loiter={v_stall_loiter:.4g}; ## stall speed at loiter altitude (m/s)');
print(f'## end loiter output results\n');


# Descent
# Typical descent uses a 3 degree glideslope
# This is like climbing (Lec 21) but theta in that perspective is negative.
# Assume a smooth transition from v_loiter at the top of descent
# to vapproach (typically 1.3vstall at airport elevation) at landing 

# descent input parameters
theta_approach = *ur.deg; # typically 3 (deg) 
vapproach_factor = ; # vapproach/vstall... typically 1.3 
# end descent input parameters


Treq_topofdescent = ; # Thrust required for steady level flight at top of descent (speed v_loiter)
Preq_topofdescent = ; # Power required for steady level flight at top of descent

v_stall_landing = ; # v_stall on landing (airport altitude, most fuel gone, OK to neglect fuel consumption during descent in this calc.) (m/s)
v_approach = ; # approach velocity (m/s)
Treq_approach =; # Thrust required for steady level flight at airport elevation and approach velocity
Preq_approach =; # Power required for steady level flight at airport elevation and approach velocity


# From climb (lec 21), we had sin(theta) = (T-TR)/W
# where TR is the thrust required for steady level flight
# at the corresponding altitude.

# For descent sin(theta) is negative (theta=-theta_approach=-3deg)
# Solve the above equation for T (engine thrust setting for descent)
# both at loiter altitude and airport altitude;
# If a prop, multiply by corresponding v to get P_descent (engine
# power setting for descent). Then multiply by TSFC or
# BSFC as appropriate to get fuel flow rate. Multiply by
# approximate descent time (rate of descent = v*sin(theta_approach))
# to get fuel used in descent.


T_topofdescent = ; # engine thrust setting for top of descent (N)
if T_topofdescent < 0:
    T_topofdescent = 0*ur.N; # Thrust setting cannot be negative (use speed brakes)
    pass

T_approach = ; # engine thrust setting for bottom of descent (N)
if T_approach < 0:
    T_approach = 0*ur.N; # Thrust setting cannot be negative (use speed brakes)
    pass
P_topofdescent = ; # engine power setting for top of descent (W)
P_approach = ; # engine power setting for bottom of descent (W)

# The above numbers should be LESS THAN the thrust and power required
# numbers farther up because in descent some of the power is coming
# from work done by gravity, versus the Tr and Pr correspond to
# steady level flight. 

fuelflow_topofdescent = ;# (N/s)
fuelflow_approach = ; # (N/s)

descenttime = ; # (s)
fuelconsumption_descent = ; # (N)

Wfuel_after_descent = ; # (N)

assert(Wfuel_after_descent > 0); # must land with some fuel remaining 

print(f'## descent output results');
print(f'Treq_topofdescent={Treq_topofdescent:.4g}; ## Thrust required for steady level flight at top of descent (N)');
print(f'Preq_topofdescent={Preq_topofdescent:.4g}; ## Power required for steady level flight at top of descent (W)');
print(f'v_stall_landing={v_stall_landing:.4g}; ## stall speed at landing altitude (m/s)');
print(f'v_approach={v_approach:.4g}; ## approach velocity (m/s)');
print(f'Treq_approach={Treq_approach:.4g}; ## Thrust required for steady level flight at bottom of descent (N)');
print(f'Preq_approach={Preq_approach:.4g}; ## Power required for steady level flight at bottom of descent (W)');

print(f'T_topofdescent={T_topofdescent:.4g}; ## Thrust setting for top of descent (N)');
print(f'T_approach={T_approach:.4g}; ## Thrust setting for bottom of descent (N)');
print(f'P_topofdescent={P_topofdescent:.4g}; ## Power setting for top of descent (W)');
print(f'P_approach={P_approach:.4g}; ## Power setting for bottom of descent (W)');

print(f'fuelflow_topofdescent={fuelflow_topofdescent:.4g}; ## Fuel flow for top of descent (N/s)');
print(f'fuelflow_approach={fuelflow_approach:.4g}; ## Fuel flow for bottom of descent (N/s)');

print(f'descenttime={descenttime:.4g}; ## Descent time (s)');
print(f'fuelconsumption_descent={fuelconsumption_descent:.4g}; ## Descent fuel weight consumed (N)');
print(f'Wfuel_after_descent={Wfuel_after_descent:.4g}; ## Weight of fuel remaining after descent (N)');

print(f'## end descent output results\n');


# Landing
# landing input parameters
h_obstacle = 15.2*ur.m;  # (m) ... obstacle height 50' (15.2 m) 
theta_f = *ur.deg; # flare angle ... less than or equal to theta_a which is usually 3.0 deg.
n_flare = ; # flare pullup maneuver load factor ... typically 1.2
mu_braking = ;# Braking friction coefficient
# end landing input parameters

v_flare = ; # avg flare velocity (m/s)
v_touchdown = ; # touchdown velocity (m/s)


R_flare = ; # Flare pullup maneuver radius (m)
sa = ; # approach distance from obstacle to start of flare (meters)
sf = ; # flare distance (meters)

# deceleration distance is v_touchdown**2/2a
# lift and drag affect deceleration; they are calculated in the
# wheels down configuration (based on CL_wheelsdown)
D_decel = ; # Drag during deceleration @ 0.7*v_td (N)
L_decel = ; # Lift during deceleration @ 0.7*v_td (N)
a_landing = # deceleration, calculated @ v=0.7 v_td
sg_landing = # ground distance (m) = v_lo**2/(2*a_decel) 

# total landing distance
s_land = ; # Total landing distance 

print(f'## landing output results');
print(f'v_flare={v_flare:.4g}; ## flare velocity (m/s)');
print(f'v_touchdown={v_touchdown:.4g}; ## touchdown velocity (m/s)');
print(f'R_flare={R_flare:.4g}; ## Flare pullup maneuver radius (m)');
print(f'sa={sa:.4g}; ## approach distance (m)');
print(f'sf={sf:.4g}; ## flare distance (m)');
print(f'D_decel={D_decel:.4g}; ## drag during deceleration @ 0.7v_td (N)');
print(f'L_decel={L_decel:.4g}; ## lift during deceleration @ 0.7v_td (N)');
print(f'a_landing={a_landing:.4g}; ## ground deceleration (m/s^2)');
print(f'sg_landing={sg_landing:.4g}; ## ground deceleration distance (m)');
print(f's_land={s_land:.4g}; ## landing distance (m)');
print(f'## end landing output results\n');

