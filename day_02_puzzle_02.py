import re

INPUT_FILENAME = "inputs/day_02_puzzle_input.txt"

with open(INPUT_FILENAME) as f:
    puzzle_input = f.read().split(",")

sum_invalid_ids = 0

for r in puzzle_input:
    # Get the range as numbers
    complete_range = r.split("-")
    start_num = int(complete_range[0])
    end_num = int(complete_range[1])

    for num in range(start_num, end_num+1):
        num_as_str = str(num)
        # Boolean flag to determine if an invalid ID has been found
        is_invalid_id = False

        # Very inefficient loop that will take a long time to complete
        # but still coompletes
        for i in range(1, len(num_as_str)+1):
            # Grab the pattern to check for
            # Puzzle states a single repeated number counts as well
            pattern = num_as_str[:i]
            # Use regex to find all matches in the current number string
            pattern_matches = re.findall(pattern, num_as_str)
            # If more than one pattern match is found
            # and the length of all the matches is
            # the same as the length of the number string
            # an invalid ID has been found and no more processing
            # is required for this number string
            if len(pattern_matches) > 1 and ((len(pattern) * len(pattern_matches)) == len(num_as_str)):
                is_invalid_id = True
                break

        # If the ID is invalid, add to sum
        if is_invalid_id:
            sum_invalid_ids += num

# Print the sum!
print(f"Sum of invalid ids: {sum_invalid_ids}")
