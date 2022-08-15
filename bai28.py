def convert(my_string):
    arr = [char for char in my_string]
    arr[0], arr[-1] = arr[-1], arr[0]
    return "".join(arr)

print(convert("a"))
print(convert("ab"))
print(convert("abcd"))