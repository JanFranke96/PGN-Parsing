import pickle

# Read eval_list_scriptwhite from file
with open("C:\\Users\\J.Franke\\PycharmProjects\\chessboardtimeandeval_white3min.pkl", "rb") as f:
    chessboardtimeandeval_white = pickle.load(f)

# Read eval_list_scriptblack from file
with open("C:\\Users\\J.Franke\\PycharmProjects\\chessboardtimeandeval_black3min.pkl", "rb") as f:
    chessboardtimeandeval_black = pickle.load(f)

# Calculate the difference in evaluations between script 1 and script 2
eval_difference = []
for (x_coord, y_coord, z_coord, s_coord, t_coord, u_coord, w_coord), (p_coord, q_coord, v_coord) in zip(chessboardtimeandeval_white, chessboardtimeandeval_black):
        eval_difference.append(float(v_coord) - float(s_coord))

# Filter out coordinates that don't meet the condition
filtered_coords = [
    (x_coord, y_coord, z_coord, diff, t_coord, u_coord, w_coord)
    for (x_coord, y_coord, z_coord, s_coord, t_coord, u_coord, w_coord), diff, (p_coord, q_coord, v_coord) in zip(chessboardtimeandeval_white, eval_difference, chessboardtimeandeval_black)

]

x_coords = [coord[0] for coord in filtered_coords]
y_coords = [coord[1] for coord in filtered_coords]
z_coords = [coord[2] for coord in filtered_coords]
t_coords = [coord[4] for coord in filtered_coords]
u_coords = [coord[5] for coord in filtered_coords]
w_coords = [coord[6] for coord in filtered_coords]

# Zip x_coords and diff together to create tuples
coord_diff_tuples = list(zip(y_coords, z_coords, eval_difference, t_coords, u_coords, w_coords))

# Sort coord_diff_tuples by the third element in each tuple (v_coords) from biggest to smallest
coord_diff_tuples_sorted = sorted(coord_diff_tuples, key=lambda x: x[0], reverse=False)


# Print the numbered tuples
print("Numbered Time and Difference Tuples:", coord_diff_tuples_sorted)
print("Number of elements in eval_diff_final:", len(coord_diff_tuples_sorted))

# Specify the save location
save_location = "C:\\Users\\J.Franke\\PycharmProjects\\chessboard"

# Save movetime_evaldiff_tuple to a file
with open(save_location + "movetime_evaldiff_tuple3min.pkl", "wb") as f:
    pickle.dump(coord_diff_tuples, f)
