# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 12:02:49 2023

@author: jacob
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Constants
depth_increment = 0.1  # depth increment in meters
boundary_temp = 40  # temperature of the heat exchange fluid in degrees Celsius
initial_temps = [40, 20, 20, 20, 20, 20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20]  # initial temperatures at each depth increment
thermal_conductivity = 0.5  # assumed thermal conductivity in W/(m·K)
heat_capacity = 1840  # assumed heat capacity in J/(kg·K)
density = 1400  # assumed density in kg/m³
time_step = 3600  # time step in seconds (1 hour)
num_depths = len(initial_temps)
num_time_steps = 500  # number of time steps to simulate


# Calculating thermal diffusivity
thermal_diffusivity = thermal_conductivity / (heat_capacity * density)

# Setting up the grid for temperature simulation
temp_grid = np.zeros((num_time_steps, num_depths))
temp_grid[0, :] = initial_temps  # setting initial temperatures

# Simulation loop
for t in range(1, num_time_steps):
    for d in range(1, num_depths - 1):
        # Calculating temperature change based on thermal diffusivity
        temp_change = thermal_diffusivity * (
           (temp_grid[t - 1, d - 1] - 2 * temp_grid[t - 1, d] + temp_grid[t - 1, d + 1]) / (depth_increment**2)
        ) * time_step

        # Updating temperature
        temp_grid[t, d] = temp_grid[t - 1, d] + temp_change

    # Maintaining the boundary temperature at 40°C
    temp_grid[t, 0] = boundary_temp

    # Ensuring no temperature drop below initial condition at each depth
    temp_grid[t, :] = np.maximum(temp_grid[t, :], temp_grid[0, :])

# Displaying the temperature grid for each time step
#print(temp_grid)
temp_df = pd.DataFrame(temp_grid)


plt.figure(figsize=(10, 6))
plt.plot(np.arange(num_depths) * depth_increment, temp_grid[-1, :], marker='o')
plt.ylabel('Temperature (°C)')
plt.xlabel('Depth (m)')
plt.title('Temperature Profile at the Last Time Step')
plt.grid(True)
plt.show()


########################################################################

# Finding the time it takes for the heat to penetrate 1 meter deep (to a temperature of 21°C)
target_depth_index = int(1 / depth_increment)  # converting 1 meter to index based on depth increment
target_temperature = 21  # target temperature of 21°C

# Finding the time step at which the temperature at 1 meter depth reaches 21°C
time_to_reach_target = None
for t in range(num_time_steps):
    if temp_grid[t, target_depth_index] >= target_temperature:
        time_to_reach_target = t * time_step  # converting time step index to actual time in seconds
        break

time_to_reach_target_hours = time_to_reach_target / 3600 if time_to_reach_target is not None else None

print(time_to_reach_target_hours)

##########################################################################

thermal_diffusivity = thermal_conductivity / (heat_capacity * density)
#thermal_diffusivity = 2 * thermal_diffusivity
# Setting up the grid for temperature simulation
temp_grid = np.zeros((num_time_steps, num_depths))
temp_grid[0, :] = initial_temps  # setting initial temperatures

# Simulation loop
for t in range(1, num_time_steps):
    for d in range(1, num_depths - 1):
        # Calculating temperature change based on thermal diffusivity
        temp_change = thermal_diffusivity * (
            (temp_grid[t - 1, d - 1] - 2 * temp_grid[t - 1, d] + temp_grid[t - 1, d + 1]) / depth_increment**2
        ) * time_step

        # Updating temperature
        temp_grid[t, d] = temp_grid[t - 1, d] + temp_change

    # Maintaining the boundary temperature at 40°C
    temp_grid[t, 0] = boundary_temp

    # Ensuring no temperature drop below initial condition at each depth
    temp_grid[t, :] = np.maximum(temp_grid[t, :], temp_grid[0, :])

# Displaying the temperature grid for each time step
#print(temp_grid)

plt.figure(figsize=(10, 6))
plt.plot(np.arange(num_depths) * depth_increment, temp_grid[-1, :], marker='o')
plt.ylabel('Temperature (°C)')
plt.axhline(y=21, color='r', linestyle='-', label='21°C Threshold')

plt.xlabel('Depth (m)')
plt.title('Temperature Profile at 185 hours Double Diffusivity')
plt.grid(True)
plt.show()

#print(temp_grid[184][30])

##############################################################################

first_thickness_temps = temp_grid[:, 1]
#print(first_thickness_temps)

# Calculating the temperature changes (differences) between each time step
temp_changes = np.diff(first_thickness_temps)

#print(temp_changes)

