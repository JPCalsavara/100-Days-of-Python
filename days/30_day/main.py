#Comum Errors
#FileNotFound - if the file does not exist

# with open("file.csv") as file:
#     print(file)
#
# #keyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["exist"]
#
# #IndexError
# fruit_list = {"Apple", "Banana","Watermelon"}
# fruit = fruit_list[3]
#
# #TypeError
# name = "joao"
# all_name = name + 3

#How to mask errors?
#Use try,except,else,finally
#try to put the code that might cause an exception

#Pessimism
#except: to do this if there was an exception
#DANGER: can hide another problems if you don't put the error in the except error like if/else

#Positivism
#else: to do this if there were no an exception

#Nilism
# finally : it doesn't matter what happens, it works

#FileNotFound with mask
try:
    file = open("file.csv")
except FileNotFoundError:
    print("There was an error, file created")
    file = open("file.csv","w")
    file.write("Jesus is the king")
except KeyError as error_key:
    print(f"The key{error_key} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")

#Raise - create an error
# raise TypeError("This is an error that I made up")
#Pratical use

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    #Avoid inhuman height
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
