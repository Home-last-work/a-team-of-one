from typing import Iterator
import numpy
# create random matrix
matrix = numpy.random.random((3, 3))

def transpose_matrix(matrix: list[list[int]]) -> Iterator[list[list[int]]]:
    ''' This function transposes the matrix '''
    is_valid = len(set(map(lambda el: len(el), matrix))) == 1

    if is_valid:
        yield list(map(list,zip(*matrix)))


if __name__ == '__main__':
    print(*transpose_matrix(matrix=matrix))