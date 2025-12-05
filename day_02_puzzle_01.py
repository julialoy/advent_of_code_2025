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
        # Amount of digits in the number
        num_len = len(str(num))
        # Puzzle rules indicate an invalid ID will always
        # have an even number of digits
        if num_len % 2 != 0:
            continue

        # Compare the first half of the number
        # to the scecond half, to determine
        # whether an invalid ID has been found
        first_half = str(num)[:num_len//2]
        second_half = str(num)[num_len//2:]

        # If the ID is invalid, add to sum
        if first_half == second_half:
            sum_invalid_ids += num

print(f"Sum of invalid ids: {sum_invalid_ids}")
