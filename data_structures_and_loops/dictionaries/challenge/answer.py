"""Sum Values"""
# Write your sum_values function here:
def sum_values(my_dictionary):
  return sum(my_dictionary.values())

# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

"""Even Keys"""
# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
  sum_v = 0
  for k, v in my_dictionary.items():
    if k%2 == 0:
      sum_v += v
  return sum_v

# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

"""Add Ten"""
# Write your add_ten function here:
def add_ten(my_dictionary):
  for k, v in my_dictionary.items():
    my_dictionary[k] = v+10
  return my_dictionary

# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

"""Values That Are Keys"""
# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  same_k_v = []
  for k in my_dictionary.keys():
    for v in my_dictionary.values():
      if k == v:
        same_k_v.append(k)
  return same_k_v

# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

"""Largest Value"""
# Write your max_key function here:
def max_key(my_dictionary):
  max_value = max(my_dictionary.values())
  for k, v in my_dictionary.items():
    if v == max_value:
      return k

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

"""Word Length Dict"""
# Write your word_length_dictionary function here:
def word_length_dictionary(words):
  return {word: len(word) for word in words}

# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

"""Frequency Count"""
# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  return {word:words.count(word) for word in words}

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

"""Unique Values"""
# Write your unique_values function here:

def unique_values(my_dictionary):
  values = []
  for v in my_dictionary.values():
    if v not in values:
      values.append(v)
  return len(values)

# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

"""Count First Letter"""
# Write your count_first_letter function here:
def count_first_letter(names):
  dict1 = {}
  for k, v in names.items():
    if k[0] not in dict1:
      dict1[k[0]] = len(v)
    else:
      dict1[k[0]] += len(v)
  return dict1

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
