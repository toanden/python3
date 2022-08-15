func_str = [
        "You converted {} C to {} F", 
        "You converted {} F to {} C", 
        "You converted {} Kg to {} lb", 
        "You converted {} lb to {} Kg", 
        "You converted {} meet to {} feet", 
        "You converted {} feet to {} meet"
        ]

def convert_func(featture):
    
    value = int(input("enter value you want convert: ")) 
    func_convert = {
        "1": value * 1.8000+ 32.00, 
        "2": (value - 32)/1.8, 
        "3": value * 2.2046, 
        "4": value / 2.2046, 
        "5": value * 3.2808, 
        "6": value / 3.2808
    }
    return func_str[int(featture) - 1].format(value, func_convert[featture])

def display():

    print("There are some feature convert: ")
    print("1. C2F")
    print("2. F2C")
    print("3. Kg2Lb")
    print("4. Lb2Kg")
    print("5. M2Feet")
    print("6. Feet2M")

def get_feature():
    feature = int(input("Choose 1 - 6 with the feature you want: "))
    while not feature in range(1,7): feature = int(input("Choose 1 - 6 with the feature you want: "))
    return feature

while True:
    display()
    feature = get_feature()
    print(convert_func(str(feature)))    
    if input("press any key to continue, \"No\" to finesh: ") == "No":
        break
