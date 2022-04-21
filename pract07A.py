# Practical 07
# Inheritance

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname  
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("Shoyo", "Hinata")
x.printname()