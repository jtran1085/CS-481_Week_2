from collections import deque
# check if specified row and column are valid matrix index


def isValid(i, j, N, M):
    return (0 <= i < M) and (0 <= j < N)

# check the current cell if it is a path and has not been calculated yet


def isSafe(i, j, mat, result):
    return mat[i][j] == 'O' and result[i][j] == -1

# Replace all O's in a matrix with their shortest distance
# from the nearest trap


def shortestDistanceToTraps(mat):
    if not mat or not len(mat):
        raise Exception("Empty Matrix")

    (R, C) = (len(mat), len(mat[0]))

    result = [[0 for x in range(C)] for y in range(R)]

    queue = deque()

    for i in range(R):
        for j in range(C):
            # if cell is mine, append to queue and set distance  to 0
            if mat[i][j] == 'T':
                queue.append((i, j, 0))

                result[i][j] = 0
            else:
                # if cell is wall or path, set value to -1
                result[i][j] = -1
# directions adjacent from cell
    row = [0, -1, 0, 1]
    col = [-1, 0, 1, 0]

# for each mine in queue, update distance adjacent to mine cell
    while queue:
        # pop front cell
        x, y, dist = queue.popleft()

        # update adjacent cells of the front node
        for i in range(len(row)):
            # append if valid and is 'O' and distance is not calculated yet
            if isValid(x + row[i], y + col[i], C, R) and \
                 isSafe(x + row[i], y + col[i], mat, result):
                result[x+row[i]][y+col[i]] = dist + 1
                queue.append((x + row[i], y + col[i], dist + 1))

    return result


if __name__ == '__main__':

    mat = [
            ['O', 'O', 'T', 'O', 'O'],
            ['O', 'W', 'O', 'T', 'O'],
            ['W', 'T', 'O', 'O', 'W'],
            ['O', 'O', 'O', 'O', 'O']
        ]

    result = shortestDistanceToTraps(mat)
# print results
for r in result:
    print(r)
