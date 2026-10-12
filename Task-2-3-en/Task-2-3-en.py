# Initializing variables
direction = 0  # 0: direction unknown, 1: up, -1: down
changes = 0  # Direction change counter
new_direction = direction  # New direction
print("Enter the floor numbers where the elevator stopped.")
print("0 - end of input.")
# Read the first floor
prev = int(input())
b_done = (prev == 0)  # flag variable, loop exit condition
while not b_done:
    current = int(input())  # Enter the remaining floors
    b_done = (current == 0)  # Exit the loop if 0 is entered
    # If the floors are the same, the direction doesn't change
    # just skip
    if not b_done and current != prev:
        # Determine the new current direction
        # between prev and current
        new_direction = 1
        if current > prev:
            new_direction = -1
    # If the direction was already known (not 0)
    # and it doesn't match the new direction, then a change has occurred
    if not b_done and direction != 0 and new_direction != direction:
        changes += 1
    # Update history for the next step
    direction = new_direction
    prev = current

print(f"Number of elevator direction changes: {changes}")
