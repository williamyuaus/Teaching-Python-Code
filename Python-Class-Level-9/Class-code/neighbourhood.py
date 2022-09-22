# n = input()

positions = []
for i in range (10):
    n = input()
    positions.append(int(n))
# for i in range(n):
#     positions.append(int(input()))
print
positions.sort()

left = (positions[1] - positions[0]) / 2
right = (positions[2] - positions[1]) / 2
min_size = left + right

n = len(positions)
for i in range(2, n - 1):
    left = (positions[i] - positions[i - 1]) / 2
    right = (positions[i + 1] - positions[i]) / 2
    size = left + right
    if size < min_size:
        min_size = size

print(min_size)