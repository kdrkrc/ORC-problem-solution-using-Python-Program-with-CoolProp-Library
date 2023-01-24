import CoolProp.CoolProp as CP

# Input Parameters
import CoolProp.Plots.PsychChart

fluid = 'R245fa'
M_ORC = 10  # kg/s mass flow rate
Pump_eff = 0.89
Turb_eff = 0.92
Q_pre = 67160.28 * 1000  # j/s
Q_evap = 41903.98 * 1000  # j/s
# Before Pump thermodynamic properties
T_1 = 298  # K
# P_1 = 14_8000  # pa
P_1 = CP.PropsSI('P', 'T', T_1, 'Q', 0, fluid)  # Pa
H_1 = CP.PropsSI('H', 'T', T_1, 'Q', 0, fluid)  # units J/kg
print(f"H_1:{H_1}")
D_1 = CP.PropsSI('D', 'T', T_1, 'Q', 0, fluid)  # kg/m^3
print(D_1)
V_1 = 1 / D_1
# After Pump thermodynamic properties
P_2 = 2_484_300  # pa
PW = (V_1 * (P_2 - P_1)) / Pump_eff  # J/kg
H_2 = PW + H_1  # J/kg

# Pre-Heater outlet  thermodynamic properties
P_3 = P_2
H_3 = (Q_pre / (M_ORC)) + H_2
print(f"H_3:{H_3 / 1000}")

T_4 = 405 #K

print(f"T_4:{T_4} K")

# Evaporator
H_4 = (Q_evap / M_ORC) + H_3

print(f"H_4:{round(H_4 / 1000, 3)}")

S_1 = CP.PropsSI('S', 'T', T_4, 'Q', 1, fluid)
print(f"S_1:{S_1 / 1000}j/kgK")

# Turbine
S_2f = CP.PropsSI('S', 'T', T_4, 'Q', 0, fluid)
S_2g = CP.PropsSI('S', 'T', T_4, 'Q', 1, fluid)
S_2fg = S_2g - S_2f
print(f"S_2:{S_2fg}")
Q = (S_1 - S_2f) / S_2fg
print(f"Q:{Q}")
print(f"S_5fg:{S_2fg}")
T_2 = CP.PropsSI('T', 'S', S_1, 'P', P_3, fluid)
H_8f = CP.PropsSI('H', 'T', T_2, 'Q', 0, fluid)
H_8g = CP.PropsSI('H', 'T', T_2, 'Q', 1, fluid)
print(f"T_2:{T_2} K")
H_8fg = H_8f - H_8g
print(f"H_8fg:{H_8fg} and H_g:{H_8g}")
H_8 = H_8f + Q * H_8fg

print(f"H_8:{round(H_8 / 1000, 3)}")
TW = (M_ORC/1000 * (H_4 - H_8)) * Turb_eff
print(f"Turbine Power:{TW}W")
print(f"Turbine Power:{TW / 1000} kW = {TW / (1000 * 1000)} megawatt")
SOP = TW - PW
print(f"PW:{PW / 1000}")
print(f"SOP:{SOP}")
HI = M_ORC * (H_4 - H_2)  # j/sn
print(f"HI:{HI}")

Cycle_eff = SOP / HI
print(f"Cycle eff:{Cycle_eff*100}")
