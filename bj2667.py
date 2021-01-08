import sys
N = int(sys.stdin.readline())
apart = []

for _ in range(N):
    apart.append(list(sys.stdin.readline().strip()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
next_pos = []
count_arr = []

for y in range(N):
    for x in range(N):
        value = apart[y][x]

        if value == '1':
            count = 1
            apart[y][x] = '0'
            next_pos.append([y, x])

            while next_pos:
                ty, tx = next_pos[0][0], next_pos[0][1]
                next_pos.pop(0)
                for i in range(4):
                    next_x = dx[i] + tx
                    next_y = dy[i] + ty
                    if 0 <= next_x < N and 0 <= next_y < N and apart[next_y][next_x] == '1':
                        next_pos.append([next_y, next_x])
                        apart[next_y][next_x] = '0'
                        count += 1
            count_arr.append(count)

count_arr.sort()

print(len(count_arr))

for i in range(len(count_arr)):
    print(count_arr[i])