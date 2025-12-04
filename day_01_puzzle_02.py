INPUT_FILENAME = "inputs/day_01_puzzle_input.txt"

# Read in puzzle input and split lines
with open(INPUT_FILENAME) as f:
    puzzle_input = f.read().split("\n")

# Dial
dial = [x for x in range(0, 100)]

# Rotation instructions
rotations = [(line[0], int(line[1:])) for line in puzzle_input]

# Puzzle answer: Number of times dial hits zero at any point during the rotation
clicks_on_zero = 0

# The current number the dial is pointing to as the index of the dial list
# The dial starts by pointing to 50
curr_dial_indx = 50
# Iterate through all instructions and traverse the number line held in dial
for rotation in rotations:
    old_num_clicks = clicks_on_zero
    # If the rotation starts with the instruction "L"
    # move toward 0 by the number in the second part of the rotation
    if rotation[0] == "L":
        new_dial_index = curr_dial_indx - rotation[1]
        # If the dial rotated left past 0 and the absolute
        # value of the new dial location is less than or
        # equal to 99, then the dial did not make a full rotation
        # Adjust the index value to the correct positive number
        # Do not increase clicks_on_zero since a full rotation was
        # not made
        if new_dial_index < 0 and abs(new_dial_index) <= 99:
            # Negative numbers are tricky, use the dial list
            # to make sure we wrap around correctly
            new_dial_index = dial[new_dial_index]
            # If the left rotation took the dial "past"
            # zero and the dial did not start on 0, this
            # rotation included one and only one click
            # on zero
            if curr_dial_indx > 0:
                clicks_on_zero += 1
        # If the dial rotated left past 0 and the absolute
        # value of the new dial location is 100 or more
        # then the dial made at least one full rotation
        elif new_dial_index < 0 and abs(new_dial_index) > 99:
            # The number of times the dial landed on 0
            # is equal to at least the number of 100s in the new
            # dial location
            clicks_on_zero += abs(new_dial_index) // 100
            # Adjust the value of the new dial location
            # to the appropriate starting value
            new_dial_index = new_dial_index % 100
            # Negative numbers are tricky, use the dial
            # to make sure we wrap around correctly
            new_dial_index = dial[new_dial_index]
            # As long as the dial did not start on 0
            # increment counter one additional time
            # since this case means there was more than one
            # full rotation made
            if curr_dial_indx > 0:
                clicks_on_zero += 1
        # If the dial rotated left and the new index
        # is exactly zero, then the dial landed on zero, increment counter
        elif new_dial_index == 0:
            clicks_on_zero += 1

    # If the rotation starts with any other instruction (i.e., "R")
    # move toward 99 by the number in the second part of the rotation
    else:
        new_dial_index = curr_dial_indx + rotation[1]
        # No need to increment clicks on zero outside
        # the following if statement since the only
        # way to land on or pass zero in a right
        # rotation is to pass 99
        if new_dial_index > 99:
            # Determine how many full rotations the dial made
            # A full rotation from any starting point will include
            # one click on zero
            clicks_on_zero += new_dial_index // 100
            # Adjust the value of the new dial location to the
            # appropriate value
            new_dial_index = new_dial_index % 100

    # Debug the instructions!
    print(f"Instruction {rotation} started at {curr_dial_indx} and ended at {new_dial_index}, pointing to zero {clicks_on_zero - old_num_clicks} times")
    # Update the current dial index for the next rotation
    curr_dial_indx = new_dial_index

# Print the puzzle answer!
print(clicks_on_zero)