import pickle
import matplotlib.pyplot as plt
import numpy as np

# Read eval_list_scriptwhite from file
with open("C:\\Users\\J.Franke\\PycharmProjects\\chessboardmovetime_evaldiff_tuple3min.pkl", "rb") as f:
    chessboardmovetime_evaldiff_tuple3min = pickle.load(f)

# Filter tuples based on x_coords
filtered_tuples_yandz = [(x, y, z, t, u, w) for x, y, z, t, u, w in chessboardmovetime_evaldiff_tuple3min if x > 50 and u == w and y < 15 and -800 < z < 200]

# Extract filtered x coordinates
y_coords_filtered_yandz = [coord[1] for coord in filtered_tuples_yandz]

# Count the number of observations for each unique x coordinate
observation_count = {}
for x in y_coords_filtered_yandz:
    observation_count[x] = observation_count.get(x, 0) + 1

# Extract y and z coordinates from the filtered tuples
x_coords_filtered_yandz = [coord[0] for coord in filtered_tuples_yandz]
z_coords_filtered_yandz = [coord[2] for coord in filtered_tuples_yandz]
t_coords_filtered_yandz = [coord[3] for coord in filtered_tuples_yandz]
u_coords_filtered_yandz = [coord[4] for coord in filtered_tuples_yandz]
w_coords_filtered_yandz = [coord[5] for coord in filtered_tuples_yandz]

# Filter tuples based on x_coords
filtered_tuples_y = [(x, y, z, t, u, w) for x, y, z, t, u, w in chessboardmovetime_evaldiff_tuple3min if 50 < x < 170 and y < 15 and -800 < z < 200]

# Extract x and y coordinates from the tuple
x_coords_filtered_y = [coord[0] for coord in filtered_tuples_y]
y_coords_filtered_y = [coord[1] for coord in filtered_tuples_y]
z_coords_filtered_y = [coord[2] for coord in filtered_tuples_y]
t_coords_filtered_y = [coord[3] for coord in filtered_tuples_y]
u_coords_filtered_y = [coord[4] for coord in filtered_tuples_y]
w_coords_filtered_y = [coord[5] for coord in filtered_tuples_y]
# Count the number of observations for each unique value of rounded_complexity_allmoves
observation_count = {}
for time_on_clock in x_coords_filtered_y:
    observation_count[time_on_clock] = observation_count.get(time_on_clock, 0) + 1

# Count the number of observations for each unique value of rounded_complexity_allmoves
observation_count2 = {}
for time_on_clock in x_coords_filtered_yandz:
    observation_count2[time_on_clock] = observation_count2.get(time_on_clock, 0) + 1

observation_count_sorted = sorted(observation_count.items(), key=lambda x: x[0], reverse=True)

observation_count2_sorted = sorted(observation_count2.items(), key=lambda x: x[0], reverse=True)

# Create scatter plot
plt.figure(figsize=(15, 6))
plt.scatter(x_coords_filtered_y, z_coords_filtered_y, color='blue', alpha=0.9, s=5)
plt.title('Time on Clock vs. Eval Difference')
plt.xlabel('Time on Clock')
plt.ylabel('Eval Difference')
plt.grid(True)

# Annotate the plot with observation counts
for time_on_clock, count in observation_count.items():
    plt.text(time_on_clock, 0, str(count), ha='right', va='bottom')

plt.show()


# Create scatter plot
plt.figure(figsize=(15, 6))
plt.scatter(x_coords_filtered_yandz, z_coords_filtered_yandz, color='blue', alpha=0.9, s=5)
plt.title('Time on Clock vs. Eval Difference')
plt.xlabel('Time on Clock')
plt.ylabel('Eval Difference')
plt.grid(True)

# Annotate the plot with observation counts
for time_on_clock, count in observation_count2.items():
    plt.text(time_on_clock, 0, str(count), ha='right', va='bottom')

plt.show()

# Calculate the ratio of observation counts
observation_ratio = {}
for complexity in observation_count:
    if complexity in observation_count2:
        observation_ratio[complexity] = observation_count2[complexity] / observation_count[complexity]
    else:
        observation_ratio[complexity] = 0  # If no observation in observation_count2, set ratio to 0

xaxis = list(range(50, 169))
# Create a bar plot for the observation ratio
plt.figure(figsize=(15, 6))
plt.bar(xaxis, observation_ratio.values(), color='green')
plt.title('Ratio of Observation Counts')
plt.xlabel('Complexity Bins')
plt.ylabel('Ratio (observation_count2 / observation_count)')
plt.grid(True)
plt.show()
