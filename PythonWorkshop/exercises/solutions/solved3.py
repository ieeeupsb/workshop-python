def formMatrix(x, y):
    return [[i * j for j in range(x)] for i in range(y)]


print(formMatrix(3, 3))