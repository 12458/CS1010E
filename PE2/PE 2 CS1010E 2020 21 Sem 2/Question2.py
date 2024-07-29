### PE 02

"""
Question 2: Cousins
"""

"""
2.1 Are You My Cousins
  Write the function to check if
  the two people are cousins
"""
def is_cousin(name1, name2, tree):
  pass

### Test data (do not modify)
parent = {
  'Amy' : 'Ben' , 'Tom': 'Ben'   , 'Frank' : 'Amy',
  'May' : 'Tom' , 'Ben': 'Howard', 'Howard': 'George',
  'Jane': 'May' , 'Joe': 'Frank' ,  # second cousin
  'Liz' : 'Jane', 'Alf': 'Joe'      # third cousin
}
### Test cases (comment out or remove before copying to Coursemology)
##print(is_cousin('Frank', 'May', parent))
##print(is_cousin('Jane', 'Joe', parent))
##print(is_cousin('Liz', 'Alf', parent))



"""
2.2 N-th Cousin
  Write the function to find
  the value of n such that
  the two people are n-th cousin
"""
def nth_cousin(name1, name2, tree):
  pass

### Test cases (comment out or remove before copying to Coursemology)
##print(nth_cousin('Frank', 'May', parent))
##print(nth_cousin('Jane', 'Joe', parent))
##print(nth_cousin('Liz', 'Alf', parent))
