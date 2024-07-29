### PE 02

"""
Question 3: Maze
"""
def create_zero_matrix(r,c):
  return [[0]*c for _ in range(r)]
def get_row(m):
  return len(m)
def get_col(m):
  return len(m[0])
def m_tight_print(m):
  for row in m:
    print(f'{"".join(map(str,row))}')
"""
3.1 Amazing Slide
  Write the function to check if
  you can slide
"""
def is_solvable(maze):
  pass

### Test data (do not modify)
maze1 = [[1,0,0,0,1,0,0],
         [0,0,1,0,0,0,1],
         [0,1,0,0,1,0,0],
         [0,1,1,0,0,0,0],
         [0,0,0,0,0,0,1]]
maze2 = [[1,0,0,0,1,0,0],
         [0,0,0,0,0,0,1],
         [0,1,0,0,1,0,0],
         [0,1,1,0,0,0,0],
         [0,0,0,0,0,0,1]]
### Test cases (comment out or remove before copying to Coursemology)
##print(is_solvable(maze1))
##print(is_solvable(maze2))
