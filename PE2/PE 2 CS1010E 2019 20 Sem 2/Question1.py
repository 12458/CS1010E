### PE 02

"""
Question 1: Auction
"""
import csv
from pprint import pprint
def read_csv(csvfilename):
  rows = []
  with open(csvfilename) as csvfile:
    file_reader = csv.reader(csvfile)
    for row in file_reader:
      rows.append(row)
  return rows
"""
1.1 Vickrey Auction
  Write the function to find the winner
  in a Vickrey auction
"""
def vickrey(bid_file, title, item_num):
  pass

### Test cases (comment out or remove before copying to Coursemology)
##print(vickrey('bid_info.csv', 'AGGREGATES, HOT MIX ASPHALT(HWYS)', 9))
##print(vickrey('bid_info.csv', 'AGGREGATES, HOT MIX ASPHALT(HWYS)', 10))
##print(vickrey('bid_info.csv', 'AGGREGATES, HOT MIX ASPHALT(HWYS)', 13))


"""
1.2 Successful Companies
  Write the function to find all
  successful companies
"""
def success(bid_file):
  pass

### Test cases (comment out or remove before copying to Coursemology)
##print(success('small_bid_info.csv'))
