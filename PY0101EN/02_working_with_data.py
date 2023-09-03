# Working with Data

path_file = "D:\Python\example.txt"
path_file_write = "D:\Python\example_write.txt"

# Open a file. Method open () with a path (path+file name) + mode r(read)/w(write)/a(appending)

# Write
with open (path_file_write,"w") as file_1:
    list_fruit = list ()
    list_fruit = ("orange", "melon","watermelon","banana")

    for fruit in list_fruit:
        file_1.write(fruit+"\n")
file_1.close()

# Append
with open (path_file_write,"a") as file_1:
    file_1.write ("kiwifruit\n")
file_1.close ()

# Read
with open (path_file_write,"r") as file_1:
    for line in file_1:
        print (line)
file_1.close ()



# Look at the attributes
print (file_1.name) # D:\Python\example.txt
print (file_1.encoding) # cp1252