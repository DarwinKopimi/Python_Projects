#This is using the automate the boring stuff to get better practice with some web modules
#Been awhile since done any python work
#This is the  google map project
import webbrowser,sys,pyperclip

if len(sys.argv) >1:
  #Gets the address from commandline
  address = ' '.join(sys.argv[1:])
else:
  address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address)