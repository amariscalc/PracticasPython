# Python Text Editor

# Import os module
import os

def menu ():
    option = "0"
    while option != "1" and option != "2":
    
        print ("Menu")
        print ("1) Continue to write.")
        print ("2) Delete all text and start again.")
        print ("help. Insert quit for exit")
        option = input ("Select a option:")

        if option != "1" and option != "2":
            print ("Option Error. Try again.")
        elif option == "1" or option == "2":
            return option
        
def to_create_delete(file):
    file_txt = open (file,"w")
    text = input ("")
    print (file_txt.readlines)
    file_txt.close ()

def to_write (file):
    while True:
        to_read (file)
        file_write = open (file, "a")
        text = input ("")
        file_write.write (text+"\n")
        if text == "quit":
            print ("")
            print ("You are going out the application. Thank you for use it")
            file_write.close()
            return False
            break
        
def to_read (file):
    file_to_read = open (file,'r')
    text_to_read = file_to_read.read ()
    print (text_to_read)
    file_to_read.close ()

# Check exist the file
file_to_edit = "text.txt"

print ("Welcome to the POC Python Text Editor.")

if os.path.exists("text.txt"):
    
    option = menu ()
    match option:
        case "1":
            to_read (file_to_edit)
            to_write (file_to_edit)
        case "2":
            to_create_delete (file_to_edit)
            to_write (file_to_edit)
else:
    file = input ("Create the new file. Name:")
    to_create_delete (file_to_edit)