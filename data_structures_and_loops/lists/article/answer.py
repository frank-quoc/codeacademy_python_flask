"""1. Append Sum"""
#Write your function here
def append_sum(lst):
  for i in range(3):
    lst.append(lst[-1] + lst[-2])
  return lst
#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

"""2. Larger List"""
#Write your function here
def larger_list(lst1, lst2):
  if (len(lst1) == len(lst2)) or (len(lst1) >= len(lst2)):
    return lst1[-1]
  else:
    return lst2[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

"""3. More Than N"""
#Write your function here
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

"""4. Append Size"""
#Write your function here
def append_size(lst):
  lst.append(len(lst))
  return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

"""5. Combine Sort"""
#Write your function here
def combine_sort(lst1, lst2):
  tot_lst = lst1 + lst2
  tot_lst.sort()
  return tot_lst
#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
