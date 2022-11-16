#non functional
def add_matrices(x, y):
 # результирующая матрица
 result = [
   [0, 0, 0],
   [0, 0, 0],
   [0, 0, 0]
 ]

 # `len()` возвращает длину списка
 # выполняем итерацию по количеству строк
 for i in range(len(x)):
   # выполняем итерацию по количеству столбцов
   for j in range(len(x[0])):
     result[i][j] = x[i][j] + y[i][j]

 return result

# матрица раз
x = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

# матрица два
y = [
 [9, 8, 7],
 [3, 2, 1],
 [6, 5, 4]
]

print(add_matrices(x, y))
'''
[
 [10, 10, 10],
 [7, 7, 7],
 [13, 13, 13]
]
'''

# данная техника называется представлением списков (list comprehension)
add_matrices_advanced = lambda x, y: [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]

print(add_matrices_advanced(x, y))