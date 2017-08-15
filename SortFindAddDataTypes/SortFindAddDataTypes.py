#This is a project dedicated to the use of multiple data types
#and the learning of how higher level functions and data types in python
#Will start off with lowest one and go to highest which seems to be tuples/dictionaries


def listSortAdd():
 print("hit first function")
 user_input = int(input())
 listFunction = []
 listFunction.append(user_input)
 print("Enter other Numbers")
 while(len(listFunction) < 10):
  user_loop_input = int(input())
  listFunction.append(user_loop_input)
 for input_parms in listFunction:
  print(listFunction[input_parms])
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






