my_string = "kitten"

def missing_char(my_string, index):
    return my_string.replace(my_string[index],"")

def get_index():
    return int(input("enter n = "))

print(missing_char(my_string, get_index()))