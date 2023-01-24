import CoolProp.CoolProp as CP

# Input Parameters
M_orc = 500  # kg/sn
fluid = 'Water'
T_1 = 411  # K

# Evaporator inlet thermodynamic properties
H_1 = CP.PropsSI('H', 'T', T_1, 'Q', 1, fluid)  # units J/kg
S_1 = CP.PropsSI('S', 'T', T_1, 'Q', 1, fluid)
# Evaporator outlet thermodynamic properties
T_2 = 386  # K

S_2f = CP.PropsSI('S', 'T', T_2, 'Q', 0, fluid)
S_2g = CP.PropsSI('S', 'T', T_2, 'Q', 1, fluid)
S_2gf = S_2g - S_2f
X = (S_1 - S_2f) / S_2gf
H_2 = CP.PropsSI('H', 'T', T_2, 'Q', X, fluid)
S_2 = CP.PropsSI('S', 'T', T_2, 'Q', X, fluid)
print(f"X_1:{X}")

q_evp = H_1 - H_2  # j/kg
Q_evp = q_evp * M_orc  # outlet energy j/sn
Evap_eff = (q_evp / H_1) * 100
print(f"Q_evp_1={Q_evp}")

# Pre-Heater inlet  thermodynamic properties

print(f"S:{S_1}")
# Pre-Heater outlet  thermodynamic properties
T_3 = 98 + 273  # K
S_2f = CP.PropsSI('S', 'T', T_3, 'Q', 0, fluid)
S_2g = CP.PropsSI('S', 'T', T_3, 'Q', 1, fluid)
S_2fg = S_2g - S_2f
X = (S_2 - S_2f) / S_2fg
print(f"X_2:{X}")

H_3 = CP.PropsSI('H', 'T', T_3, 'Q', X, fluid)

q_pre = H_2 - H_3
Q_preh = M_orc * q_pre / 1000
Pre_heat_eff = q_pre / H_2 * 100

# Performance:
ORC_efc = (H_1 - H_3) / H_1 * 100

# Solution
print("Brine flow parameters==>")
print(f"Temperature:{round(T_1 - 273, 2)} C")
print(f"Weight:{round(M_orc, 4)} kg/s")

print("/" * 10)

print("Evaporator parameters==>")
print(f"Inlet temp:{round(T_1 - 273, 2)} C")
print(f"Inlet enthalpy:{round(H_1 / 1000, 4)} kJ/kg")
print(f"Outlet temp:{round(T_2 - 273, 3)} C ")
print(f"Outlet enthalpy:{round(H_2 / 1000, 3)} kJ/kg")
print(f"Outlet energy:{round(Q_evp)} kW")
print(f"Efficiency:%{round(Evap_eff)}")

print("/" * 10)

print("Pre-Heater==>")
print(f"Outlet temp:{round(T_3 - 273, 3)} C ")
print(f"Outlet enthalpy:{round(H_3 / 1000, 3)} kJ/kg")
print(f"Efficiency:%{round(Pre_heat_eff)}")

print("Performance==>")
print(f"Evaporator energy transfer:{round(Q_evp / 1000, 2)} kW")
print(f"Pre-Heater energy transfer:{round(Q_preh, 2)} kW")
print(f"ORC Efficiency:%{round(ORC_efc, 2)}")
