class Student:
  """A Class to define a student."""

  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
    self.attendance = {}
  
  def add_grade(self, grade):
    self.grade = grade

    if type(self.grade) == Grade:
      self.grades.append(self.grade)

  def get_average(self, grades):
    return sum(grades)/len(grades)
  
  def add_attendance(self, date, attended=False):
    self.date = date
    self.attended = attended

    attendance["date"] = self.attended

class Grade:
  """A Class to represent the students' grade"""
  minimum_passing = 65

  def __init__(self, score):
    self.score = score

  def is_passing(self):
    if self.score >= minimum_passing:
      return True
    return False
  
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter_grade = Grade(100)
pieter.add_grade(pieter_grade)
