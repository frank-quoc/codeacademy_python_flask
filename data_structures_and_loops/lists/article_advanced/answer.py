"""1. Every Three Numbers"""
#Write your function here
def every_three_nums(start):
  lst = []
  if start > 100:
    return lst
  for i in range(start, 101, 3):
    lst.append(i)
  return lst

#Uncomment the line below when your function is done
print(every_three_nums(91))

"""2. Remove Middle"""
#Write your function here
def remove_middle(lst, start, end):
  for i in range(start, end+1):
    del lst[start]
  return lst

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

"""3. More Frequent Item"""
#Write your function here
def more_frequent_item(lst, item1, item2):
  c_item1 = lst.count(item1)
  c_item2 = lst.count(item2)
  if c_item1 >= c_item2:
    return item1
  return item2
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

"""4. Double Index"""
#Write your function here
def double_index(lst, index):
  try:
    twice_ele = 2 * lst.pop(index)
    lst.insert(index, twice_ele)
  except IndexError:
    return lst
  else:
    return lst
#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

"""5. Middle Item"""
#Write your function here
def middle_element(lst):
  mid = int(len(lst)/2)
  if len(lst)%2 != 0:  # odd num of elements
    return lst[mid]
  else:
    return sum(lst[mid-1:mid+1])/2

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
