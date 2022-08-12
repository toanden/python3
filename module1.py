# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("mew", 2)
cat2 = Cat("mew", 3)
cat3 = Cat("mew", 4)

# 2 Create a function that finds the oldest cat


def oldest_cat(*args):
    return max(args)


def oldest1_cat(*args):
    oldest_cat_age = 0
    for age in args:
        if age >= oldest_cat_age:
            oldest_cat_age = age
    return oldest_cat_age


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(
    f"The oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old")
print(
    f"The oldest cat is {oldest1_cat(cat1.age, cat2.age, cat3.age)} years old")
