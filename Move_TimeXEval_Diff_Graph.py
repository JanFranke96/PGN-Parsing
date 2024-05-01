import pickle
import matplotlib.pyplot as plt
import numpy as np

# Read eval_list_scriptwhite from file
with open("C:\\Users\\J.Franke\\PycharmProjects\\chessboardmovetime_evaldiff_tuple3min.pkl", "rb") as f:
    chessboardmovetime_evaldiff_tuple3min = pickle.load(f)

# Filter tuples based on x_coords
filtered_tuples_yandz = [(x, y, z, t, u, w) for x, y, z, t, u, w in chessboardmovetime_evaldiff_tuple3min if u == w and y < 15 and -1000 < z < 800]

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
filtered_tuples_y = [(x, y, z, t, u, w) for x, y, z, t, u, w in chessboardmovetime_evaldiff_tuple3min if y < 15 and -1000 < z < 800]

# Extract x and y coordinates from the tuple
x_coords_filtered_y = [coord[0] for coord in filtered_tuples_y]
y_coords_filtered_y = [coord[1] for coord in filtered_tuples_y]
z_coords_filtered_y = [coord[2] for coord in filtered_tuples_y]
t_coords_filtered_y = [coord[3] for coord in filtered_tuples_y]
u_coords_filtered_y = [coord[4] for coord in filtered_tuples_y]
w_coords_filtered_y = [coord[5] for coord in filtered_tuples_y]
# Count the number of observations for each unique x coordinate
observation_count2 = {}
for x in y_coords_filtered_y:
    observation_count2[x] = observation_count2.get(x, 0) + 1

# Calculate the mean of y_coords_filtered_x
mean_y = np.mean(y_coords_filtered_y)
print("Mean of y_coords_filtered_x:", mean_y)

# Calculate the mean of x_coords_filtered_x
mean_z = np.mean(z_coords_filtered_y)
print("Mean of z_coords_filtered_x:", mean_z)

# Create scatter plot
plt.figure(figsize=(15, 6))
plt.scatter(y_coords_filtered_yandz, z_coords_filtered_yandz, color='blue', alpha=0.9, s=5)
plt.title('Move Time vs. Eval Difference')
plt.xlabel('Move Time')
plt.ylabel('Eval Difference')
plt.grid(True)

# Annotate the plot with observation counts
for x, count in observation_count.items():
    plt.text(x, 0, str(count), ha='right', va='bottom')

plt.show()

# Create scatter plot
plt.figure(figsize=(15, 6))
plt.scatter(y_coords_filtered_y, z_coords_filtered_y, color='blue', alpha=0.9, s=5)
plt.title('Move Time vs. Eval Difference')
plt.xlabel('Move Time')
plt.ylabel('Eval Difference')
plt.grid(True)

# Annotate the plot with observation counts
for x, count in observation_count2.items():
    plt.text(x, 0, str(count), ha='right', va='bottom')

plt.show()

# Calculate the ratio between observation counts
observation_ratio = {}
for x, count in observation_count.items():
    if x in observation_count2:
        ratio = count / observation_count2[x]
        observation_ratio[x] = ratio

# Create a list of x coordinates from 1 to 20
x_axis = list(range(0, 15))

# Create a list of ratios corresponding to the x coordinates
ratios = [observation_ratio.get(x, 0) for x in x_axis]

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(x_axis, ratios, color='blue')
plt.title('Ratio of Observation Counts')
plt.xlabel('X Coordinate')
plt.ylabel('Ratio (observation_count / observation_count2)')
plt.xticks(x_axis)
plt.grid(axis='y')
plt.show()
