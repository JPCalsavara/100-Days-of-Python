#Open a file without use need to close like while loop
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("/Users/jpcal/Desktop/my_file.txt") as file:
    # file.write("\nUma guitarra tambem")
    cont = file.read()
    print(cont)

