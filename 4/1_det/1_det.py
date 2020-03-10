#1. Matrix Determinant
#Create a function that returns the determinant of a given square matrix.
from itertools import permutations
import json

def is_valid_matrix(array):
    if type(array) != list:
        raise ValueError('Not a matrix')
    row_len = len(array)
    if row_len < 1:
        raise ValueError('Not a valid matrix')
    for row in array:
        if type(row) != list:
            raise ValueError('Not a matrix')
        if row_len != len(row):
            raise ValueError('Not a square matrix')
        for column in row:
            if type(column) != int:
                raise ValueError('Not a matrix of numbers')


def sign_per(permutation, size): #counts sign of permutation
  cnt = 0
  for i in range(size):
    for j in range(i+1,size):
      if (permutation[i]>permutation[j]):
        cnt += 1    
  return cnt%2

def det(matrix, size):
  ans = 0
  for i in permutations(list(range(size))):
    step = 1
    for j,k in zip(i,range(size)):
      step *= matrix[j][k]
    ans += ((-1)**sign_per(i, size))*step
  return ans

with open("input.txt") as f:
    array = json.load(f)
size = len(array)
is_valid_matrix(array)
print(det(array, size))