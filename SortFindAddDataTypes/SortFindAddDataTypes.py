#This is a project dedicated to the use of multiple data types
#and the learning of how higher level functions and data types in python
#Will start off with lowest one and go to highest which seems to be tuples/dictionaries


def listSortAdd():
 print("hit first function")
 listFunction = []
 print("Enter other Numbers")
 while(len(listFunction) < 10):
  user_loop_input = int(input())
  listFunction.append(user_loop_input)
 print("1: see list,2:sort list,3 remove item off list")
 user_input = int(input())
 if (user_input==1):
  for input_parms in listFunction:
   print(listFunction[input_parms])
 elif (user_input == 2):
  print(sorted(listFunction))
 elif (user_input == 3):
  listFunction.pop(0)
  print(len(listFunction))
def tupleSortAdd():
 print("hit second function")
def dictSortAdd():
 print("hit third function")

def picker():
 option = [0,1,2]
 x = int(input())

 if(option[0] == x):
  listSortAdd()
  #break
 elif(option[1] == x):
  tupleSortAdd()
#  break
 elif(option[2] == x):
  dictSortAdd()
 # break
 else:
  print("unable to finish operation")
  #break

print("Welcome to the data picker! \n Chose your data type!")
picker()






