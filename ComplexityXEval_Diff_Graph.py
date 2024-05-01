import pickle
import matplotlib.pyplot as plt


# Function to check if a string is a valid float
def is_valid_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Read eval_list_scriptwhite from file
with open("C:\\Users\\J.Franke\\PycharmProjects\\chessboardmovetime_evaldiff_tuple3min.pkl", "rb") as f:
    chessboardmovetime_evaldiff_tuple3min = pickle.load(f)

# Filter tuples based on x_coords
filtered_tuples_tandz = [(x, y, z, t, u, w) for x, y, z, t, u, w in chessboardmovetime_evaldiff_tuple3min if u == w and -800 < z < 200 and t < 2.0]

# Extract x and y coordinates from the tuple
x_coords_filtered_tandz = [coord[0] for coord in filtered_tuples_tandz]
y_coords_filtered_tandz = [coord[1] for coord in filtered_tuples_tandz]
z_coords_filtered_tandz = [coord[2] for coord in filtered_tuples_tandz]
t_coords_filtered_tandz = [coord[3] for coord in filtered_tuples_tandz]
u_coords_filtered_tandz = [coord[4] for coord in filtered_tuples_tandz]
w_coords_filtered_tandz = [coord[5] for coord in filtered_tuples_tandz]

# Filter tuples based on x_coords
filtered_tuples_t = [(x, y, z, t, u, w) for x, y, z, t, u, w in chessboardmovetime_evaldiff_tuple3min if -800 < z < 200 and t < 2.0]

# Extract x and y coordinates from the tuple
x_coords_filtered_t = [coord[0] for coord in filtered_tuples_t]
y_coords_filtered_t = [coord[1] for coord in filtered_tuples_t]
z_coords_filtered_t = [coord[2] for coord in filtered_tuples_t]
t_coords_filtered_t = [coord[3] for coord in filtered_tuples_t]
u_coords_filtered_t = [coord[4] for coord in filtered_tuples_t]
w_coords_filtered_t = [coord[5] for coord in filtered_tuples_t]

# Round each element of complexity_bestmoves to 2 digits behind the decimal point
rounded_complexity_bestmoves = [round(elem, 1) for elem in t_coords_filtered_tandz]

# Round each element complexity_allmoves to 2 digits behind the decimal point
rounded_complexity_allmoves = [round(elem, 1) for elem in t_coords_filtered_t]

# Count the number of observations for each unique value of rounded_complexity_allmoves
observation_count = {}
for complexity in rounded_complexity_allmoves:
    observation_count[complexity] = observation_count.get(complexity, 0) + 1

# Count the number of observations for each unique value of rounded_complexity_bestmoves
observation_count2 = {}
for complexity in rounded_complexity_bestmoves:
    observation_count2[complexity] = observation_count2.get(complexity, 0) + 1

# Create scatter plot
plt.figure(figsize=(15, 6))
plt.scatter(rounded_complexity_allmoves, z_coords_filtered_t, color='blue', alpha=0.9, s=5)
plt.title('Complexity vs. Eval Difference')
plt.xlabel('Complexity')
plt.ylabel('Eval Difference')
plt.grid(True)

# Annotate the plot with observation counts
for complexity, count in observation_count.items():
    plt.text(complexity, 0, str(count), ha='right', va='bottom')

plt.show()


# Create scatter plot
plt.figure(figsize=(15, 6))
plt.scatter(rounded_complexity_bestmoves, z_coords_filtered_tandz, color='blue', alpha=0.9, s=5)
plt.title('Complexity vs. Eval Difference')
plt.xlabel('Complexity')
plt.ylabel('Eval Difference')
plt.grid(True)

# Annotate the plot with observation counts
for complexity, count in observation_count2.items():
    plt.text(complexity, 0, str(count), ha='right', va='bottom')

plt.show()

# Calculate the ratio of observation counts
observation_ratio = {}
for complexity in observation_count:
    if complexity in observation_count2:
        observation_ratio[complexity] = observation_count2[complexity] / observation_count[complexity]
    else:
        observation_ratio[complexity] = 0  # If no observation in observation_count2, set ratio to 0

xaxis = list(range(0, 21))
# Create a bar plot for the observation ratio
plt.figure(figsize=(15, 6))
plt.bar(xaxis, observation_ratio.values(), color='green')
plt.title('Ratio of Observation Counts')
plt.xlabel('Complexity Bins')
plt.ylabel('Ratio (observation_count2 / observation_count)')
plt.grid(True)
plt.show()
