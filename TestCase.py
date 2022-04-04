class Parent:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname
    
  def  printname(self):
    print('my name is', self.firstname, self.lastname)
    
class Student(Parent):
  def __init__(self, firstname, lastname):
    super().__init__(firstname, lastname)
  
p1 = Student('Awodi', 'Emmy', 2022)
p1.printname()        