### PE 02

"""
Question 1: Calculus
"""
def compute(poly, x): # You don't have to understand this, it works
  return sum(poly[i]*x**i for i in range(len(poly)))
"""
1.1 Iterative Derivative
  Write the function to compute
  the derivative iteratively
"""
def derivative_I(poly):
  pass

### Test cases (comment out or remove before copying to Coursemology)
##print(derivative_I([3, -9, 1, 2]))
##print(derivative_I([-9, 2, 6]))



"""
1.2 Recursive Derivative
  Write the function to compute
  the derivative recursively
"""
def derivative_R(poly):
  pass

### Test cases (comment out or remove before copying to Coursemology)
##print(derivative_R([3, -9, 1, 2]))
##print(derivative_R([-9, 2, 6]))



"""
1.3 Newton's Method
  Write the function to find
  the root of a polynomial
  using Newton's method
"""
def newton(poly, x0):
  pass

### Test cases (comment out or remove before copying to Coursemology)
##print(newton([3, -9, 1, 2], 2))
##print(newton([3, -9, 1, 2], 0))
##print(newton([3, -9, 1, 2], -2))
