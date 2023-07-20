#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
#return [list(map(lambda n: n**2, sublist)) for sublist in matrix]

    for i in matrix:
        for j in matrix:
            return[[j ** 2 for j in i] for i in matrix]
        
