"""Divisible by Ten"""
#Write your function here
def divisible_by_ten(nums):
  count = 0 
  for num in nums:
    if num%10 == 0:
      count += 1
  return count

#Uncomment the line below when your function is done
#print(divisible_by_ten([20, 25, 30, 35, 40]))

"""Greetings"""
#Write your function here
def add_greetings(names):
  greetings = []
  for name in names:
    greetings.append("Hello, " + name)
  return greetings

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

"""Delete Starting Even Numbers"""
#Write your function here
def delete_starting_evens(lst):
  while (len(lst) > 0) and (lst[0]%2 == 0):
    lst = lst[1:]
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

"""Odd Indices"""
#Write your function here
def odd_indices(lst):
  odd_ind = []
  for i in range(1, len(lst), 2):
    odd_ind.append(lst[i])
  return odd_ind

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

"""Exponents"""
#Write your function here
def exponents(bases, powers):
  lst = []
  for i in bases:
    for j in powers:
      lst.append(i**j)
  return lst

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

"""Larger Sum"""
#Write your function here
def larger_sum(lst1, lst2):
  if sum(lst1) >= sum(lst2):
    return lst1
  return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

"""Over 9000"""
#Write your function here
def over_nine_thousand(lst):
  count = 0
  if lst == []:
    return 0
  for i in lst:
    count += i
    if count > 9000:
      break
  return count
    

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

"""Max Num"""
#Write your function here
def max_num(nums):
  return max(nums)

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

"""Same Values"""
#Write your function here
def same_values(lst1, lst2):
  com_indices = []
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      com_indices.append(i)
  return com_indices

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

"""Reversed List"""
#Write your function here
def reversed_list(lst1, lst2):
  if lst1 == list(reversed(lst2)):
    return True
  return False

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
