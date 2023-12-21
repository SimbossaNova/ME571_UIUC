from sympy import symbols, Eq, diff, solve
import pandas as pd
import numpy as np


# Define the variable and constants
t = symbols('t', real=True)
T = 10

# Define the cost functions
f1 = (10 - t)**2
f2 = (20 - 2*(T - t))**2

# Total cost function
C_tot = f1 + f2

# First derivative of the total cost function
dC_tot_dt = diff(C_tot, t)

# Find the value of t that minimizes the total cost
critical_points = solve(dC_tot_dt, t)

# Evaluate the second derivative to find the minimum
d2C_tot_dt2 = diff(dC_tot_dt, t)
min_points = [point for point in critical_points if d2C_tot_dt2.subs(t, point) > 0]

# Evaluate the total cost at the minimum
C_tot_min_values = [C_tot.subs(t, point) for point in min_points]
C_tot_min_values, min_points





import numpy as np
import pandas as pd



# Given values
Tc = 293  # Cold reservoir temperature in K
Th = 313  # Hot reservoir temperature in K
Qc = 1000  # Heat flow into the evaporator in W

# Carnot COP for a refrigerator or heat pump
COP_carnot = Tc / (Th - Tc)

# Work required by the compressor in a Carnot cycle
Wc = Qc / COP_carnot

# Heat flow out of the condenser
Qh = Qc + Wc

print(COP_carnot, Wc, Qh)

# Constants
Uc = Uh = 20  # Overall heat transfer coefficient for both evaporator and condenser in W/m^2K

# Initialize a DataFrame to store the results
columns = ['A (m^2)', 'Trc (K)', 'Trh (K)', 'COP_Carnot_actual', 'COP_actual', 'P (W)']
results = pd.DataFrame(columns=columns)

# Calculate values for A from 1 to 10 m^2
for A in range(1, 11):
    # Calculate Trc and Trh using the given equations
    Trc = Tc - (Qc / (Uc * A))
    Trh = Th + (Qc / (Uh * A))
    
    # Calculate COP_Carnot_actual
    COP_Carnot_actual = Trc / (Trh - Trc)
    
    # Calculate COP_actual (50% of COP_Carnot_actual)
    COP_actual = 0.5 * COP_Carnot_actual
    
    # Calculate P (Compressor power)
    P = Qc / COP_actual
    
    # Append the results to the DataFrame
    results = results.append(pd.Series([A, Trc, Trh, COP_Carnot_actual, COP_actual, P], index=columns), ignore_index=True)

print(results)

R = 0.12  # Electricity rate in $/kWh
T = 50000  # Hours of operation during system lifetime in hr
Ce = Cc = 20  # Evaporator and condenser cost in $/m^2

# Add a new column to the results DataFrame for LCC
results['P (kW)'] = results['P (W)'] / 1000  # Convert P from W to kW
results['LCC ($)'] = (results['P (kW)'] * R * T) + (results['A (m^2)'] * (Ce + Cc))

# Find the value of A that minimizes the LCC
min_LCC_row = results.loc[results['LCC ($)'].idxmin()]

print(min_LCC_row[['A (m^2)', 'LCC ($)']])

