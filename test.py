""" from unicodedata import name


class UserDefined:
    def __init__(self, name) -> None:
        self.name =  name

    def info(self):
        print(f"player name is {self.name}")
        return "done"

player1 = UserDefined("toan")
player1.info() """

""" class geeks:
    course = 'DSA'
  
    def purchase(obj):
        print("Puchase course : ", obj.course)
  
  
geeks.purchase = classmethod(geeks.purchase)
geeks.purchase() """



""" # Python program to understand the classmethod
  
class Student:
  
    # create a variable
    name = "Geeksforgeeks"
  
    # create a function
    def print_name(obj):
        print("The name is : ", obj.name)
  
  
# create print_name classmethod
# before creating this line print_name()
# It can be called only with object not with class
Student.print_name = classmethod(Student.print_name)
  
# now this method can be called as classmethod
# print_name() method is called a class method
Student.print_name() """




""" # Python program to demonstrate
# use of a class method and static method.
from datetime import date
  
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
  
    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
  
    def display(self):
        print("Name : ", self.name, "Age : ", self.age)
  
person = Person('mayank', 21)
person.display() """




# Adds a welcome message to the string
# returned by fun(). Takes fun() as
# parameter and returns welcome().
""" def decorate_message(fun):
  
    # Nested function
    def addWelcome(site_name):
        return "Welcome to " + fun(site_name)
  
    # Decorator returns a function
    return addWelcome
  
@decorate_message
def site(site_name):
    return site_name;
  
# Driver code
  
# This call is equivalent to call to
# decorate_message() with function
# site("GeeksforGeeks") as parameter
print(site("GeeksforGeeks")) """


# This one's a bit different, representing an unusual (and honestly,
# not recommended) strategy for tracking users that sign up for a service.

""" class User:
    # An (intentionally shared) collection storing users who sign up for some hypothetical service.
    # There's only one set of members, so it lives at the class level!
    members = set()
    def __init__(self, name):
        self.name = name
        # self.members = set()  # Not signed up to begin with.
    def sign_up(self):
        self.members.add(self.name)

# Change the code above so that the following lines work:
# 
sarah = User('sarah')
heather = User('heather')
cristina = User('cristina')
print(User.members)  # set()
heather.sign_up()
cristina.sign_up()
print(User.members)  # {'heather', 'cristina'} """


""" #By reading the python documentation, add 3 more magic/dunder methods of your choice to this Toy class. 
class Toy():
  def __init__(self, color, age):
    self.color = color
    self.age = age
    self.my_dict = {
        'name':'Yoyo',
        'has_pets': False,
    }

  def __str__(self):
    return f"{self.color}"

  def __len__(self):
    return 5

  def __del__(self):
    return "deleted"

  def __call__(self):
      return('yes??')

  def __getitem__(self,i):
      return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name']) """