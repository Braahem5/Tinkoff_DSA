stack = []
operations = []
operation_counts = []

n = int(input())
wagon_numbers = list(map(int, input().split()))
expected_wagon = 1

for val in wagon_numbers:
    if len(stack) > 0 and val > stack[-1]:
        print(0)
        quit(0)

    operations.append(1)
    stack.append(val)

    while len(stack) > 0 and stack[-1] == expected_wagon:
        operations.append(2)
        stack.pop()
        expected_wagon += 1

current_operation = operations.pop(0)
count = 1

while len(operations) > 0:
    if operations[0] == current_operation:
        count += 1
    else:
        operation_counts.append((current_operation, count))
        current_operation = operations[0]
        count = 1
    operations.pop(0)

operation_counts.append((current_operation, count))

print(len(operation_counts))

for op, count in operation_counts:
    print(f"{op} {count}")
