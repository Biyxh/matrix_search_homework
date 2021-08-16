def matrix_find(matrix, value):
    if not matrix or not matrix[0]:
        print([-1, -1])

    j = len(matrix) - 1
    for row in matrix:
        while row[j] > value:
            j = j - 1
            if j == -1:
                return False
        if row[j] == value:
            return True
    return False


matrix = [[[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]]]

print(matrix_find(matrix=matrix, value=4))
def condition(x): return x > 7


output = [idx for idx, element in enumerate(matrix) if condition(element)]
print(output)
