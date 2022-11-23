def check(letter):
  list_of_vowels = ['a', 'e', 'i', 'o', 'u']
  if letter in list_of_vowels:
      return True
  else:
      return False
letters = ['u', 'a', 'q', 'c', 'i', 'd', 'z', 'p', 'e']
filtered_object = filter(check, letters)
filtered_list = list(filtered_object)
print("The list of vowels is: ", filtered_list)