# Step 1: Initialize an empty stack to hold the train cars (wagons)
stack = []

# Step 2: Initialize a list to keep track of operations (1 for push, 2 for pop)
operations = []

# Step 3: Initialize a list to store the final operations (push and pop) and their counts
operation_counts = []

# Step 4: Read the number of wagons from the input
n = int(input("Enter the number of wagons: "))

# Step 5: Read the list of wagon numbers (in order) from the input
wagon_numbers = list(
    map(int, input("Enter the wagon numbers separated by spaces: ").split())
)

# Step 6: Initialize the next expected wagon number to 1
expected_wagon = 1

# Step 7: Process each wagon number
for val in wagon_numbers:
    # If the current wagon number is greater than the top of the stack,
    # it means we cannot maintain the desired order.
    if len(stack) > 0 and val > stack[-1]:
        print(0)  # Output 0 to indicate failure
        quit(0)  # Exit the program

    # Record the "push" operation (1 means push)
    operations.append(1)  # This means we are pushing the current wagon
    stack.append(val)  # Push the wagon number onto the stack

    # Check if the top of the stack matches the expected wagon number
    while len(stack) > 0 and stack[-1] == expected_wagon:
        # If the top of the stack matches the expected wagon number,
        # we pop it (remove it) from the stack and move to the next expected wagon.
        operations.append(2)  # This means we are popping the top wagon
        stack.pop()  # Pop the top wagon from the stack
        expected_wagon += 1  # Increment the expected wagon number to the next one

# Step 8: Count the occurrences of each operation and store them as tuples in operation_counts
current_operation = operations.pop(0)  # Start with the first operation
count = 1  # Initialize a count for the number of consecutive operations

# Step 9: Go through the remaining operations and group consecutive same operations
while len(operations) > 0:
    if operations[0] == current_operation:
        # If the next operation is the same as the current one, increase the count
        count += 1
    else:
        # If the operation changes, store the current operation and its count as a tuple
        operation_counts.append((current_operation, count))
        current_operation = operations[0]  # Update to the new operation
        count = 1  # Reset the count for the new operation
    operations.pop(0)  # Remove the processed operation

# Step 10: Add the last operation and its count to operation_counts
operation_counts.append((current_operation, count))

# Step 11: Print out the operations and their counts
print(len(operation_counts))
for op, count in operation_counts:
    print(f"{op} {count}")
