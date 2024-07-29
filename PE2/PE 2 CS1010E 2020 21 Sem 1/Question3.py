### PE 02

"""
Question 3: Game of Life
"""
def create_zero_matrix(n, m):
  return [[0 for i in range(m)] for j in range(n)]
def m_tight_print(m):
  for row in m:
    print(''.join(map(str,row)))
def m_tight_print_gof(m):
  for row in m:
    print(''.join(map(lambda x: '#' if x == 1 else '_',row)))
"""
3.1 Add cells
  Write the function to add cells
"""
def add_cells(board, cell_list):
  n,m = len(board),len(board[0])
  for x,y in cell_list:
    if 0 <= x < n and 0 <= y < m:
      board[x][y] = 1

### Test data (do not modify)
very_long_house = [(5,6),(5,7),(5,8),(5,9),(5,10),(6,5),(6,8),(6,11),(7,5),(7,6),(7,10),(7,11)]
board = create_zero_matrix(2, 3)
### Test cases (comment out or remove before copying to Coursemology)
##add_cells(board, [(1,2), (1,1), (1,0)])
##m_tight_print(board)
##add_cells(board, [(0,1), (1,1)])
##m_tight_print(board)



"""
3.2 Simulate
  Write the function to
  simulate game of life
"""
def neighbour(board,i,j):
  res = 0
  n,m = len(board),len(board[0])
  for x in range(-1,2):
    for y in range(-1,2):
      if x == y == 0:
        continue
      if 0 <= x+i < n and 0 <= y+j < m:
        res += board[x+i][y+j]
  return res
def step(board):
  n,m = len(board),len(board[0])
  res = create_zero_matrix(n, m)
  for i in range(n):
    for j in range(m):
      nb = neighbour(board,i,j)
      if board[i][j] == 1 and 2 <= nb <= 3:
        res[i][j] = 1
      elif board[i][j] == 0 and nb == 3:
        res[i][j] = 1
  return res

### Test data (do not modify)
board0 = [[1,1,0,0],
          [1,1,1,1],
          [0,1,0,0]]
### Test cases (comment out or remove before copying to Coursemology)
##m_tight_print(board0)
##board1 = step(board0)
##m_tight_print(board1)
##board2 = step(board1)
##m_tight_print(board2)
