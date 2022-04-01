class Parent:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname
    
  def  printname(self, *args, **Kwargs):
    print('my name is' self.firstname, self.lastname)
    
class Student(Parent):
  def      