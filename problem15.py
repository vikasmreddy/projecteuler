#solution using dynamic programming (keeping state as we go through)
N_seed = 20
N = N_seed + 1 #an 20 X 20 grid has 21 x 21 "corners"
grid = [[-1 for x in xrange(N)] for x in xrange(N)]
for j in range(0,N):
    for i in range(0,N):
        if i == 0 and j == 0:
            grid[i][j] = 1
        elif j == 0:
            grid[i][j] = grid[i-1][j] #copy from left
        elif i == 0:
            grid[i][j] = grid[i][j-1] #copy from up
        else:
            grid[i][j] = grid[i-1][j] + grid[i][j-1] #sum of left and up

print grid[N-1][N-1]