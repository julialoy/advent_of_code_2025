INPUT_FILENAME = "inputs/day_01_puzzle_input.txt"

# Read in puzzle input and split lines
with open(INPUT_FILENAME) as f:
    puzzle_input = f.read().split("\n")

# Dial
dial = [x for x in range(0, 100)]

# Rotation instructions
rotations = [(line[0], int(line[1:])) for line in puzzle_input]

# Puzzle answer: Number of times dial is left at zero after any single rotation
safe_password = 0

# The dial starts by pointing to 50
curr_dial_indx = 50
# Iterate through all instructions and traverse the number line held in dial
for rotation in rotations:
    # If the rotation starts with the instruction "L"
    # move toward 0 by the number in the second part of the rotation
    if rotation[0] == "L":
        curr_dial_indx -= rotation[1]
        # Fix out of bounds dial
        if curr_dial_indx < 0 and abs(curr_dial_indx) <= 99:
            # Negative numbers are tricky, use the dial
            # to make sure we wrap around correctly
            curr_dial_indx = dial[curr_dial_indx]
        elif curr_dial_indx < 0 and abs(curr_dial_indx) > 99:
            # Figure out new dial index if there was at least one full rotation
            curr_dial_indx = curr_dial_indx % 100
            # Negative numbers are tricky, use the dial
            # to make sure we wrap around correctly
            curr_dial_indx = dial[curr_dial_indx]
    # If the rotation starts with any other instruction (i.e., "R")
    # move toward 99 by the number in the second part of the rotation
    else:
        curr_dial_indx += rotation[1]
        # Figure out new dial index if there was at least one full rotation
        if curr_dial_indx > 99:
            curr_dial_indx = curr_dial_indx % 100

    # Increment the safe password if the rotation stops on 0
    if curr_dial_indx == 0:
        safe_password += 1

print(safe_password)