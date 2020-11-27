'''Write a function named printTable() that takes

a list of lists of strings and displays it in

a well-organized table with each column

left-justified. Assume that all the inner

lists will contain the same number of strings.'''

 

tableData = [['apples', 'oranges', 'cherries', 'banana'],

             ['Alice', 'Bob', 'Carol', 'David'],

             ['dogs', 'cats', 'moose', 'goose']]

 

def printTable():

 

#Print a header for the table """

  print('ORGANIZED TABLE OF ITEMS'.center(10 * 3, '-'))

  print()

  num_of_lists_in_tableData= len(tableData)

  num_items_in_each_tableData_list = len(tableData[0])

  new_list_of_items = []

  x = 0

 

  '''assemble a new list of items, combine 3 lists to one'''

  for i in range(num_items_in_each_tableData_list):

      for j in range(num_of_lists_in_tableData):

          new_list_of_items.append(tableData[j][i])   

  

  '''print(new_list_of_items) in table format,

     one row at a time'''

  for idx1 in range(num_items_in_each_tableData_list):

    for idx2 in range(num_of_lists_in_tableData):

        print(new_list_of_items[x].ljust(12), end='')

        x += 1

        # before starting new row,

        # print() to move to new line

    print()

printTable()

