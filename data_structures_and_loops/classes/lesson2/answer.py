class SortedList(list):
  def __init__(self, lst):
    super.__init__(lst)
    self.sort()
  
  def append(self, value):
    super().append(value)
    self.sort()

class NewDict(dict):
  fallback = "No Key Exists"
  def __init__(self, values):
    super.__init__(values)
  
  def __getitem(self, key):
    try:
      return super().__getitem__(key)
    except KeyError:
      return self.fallback
