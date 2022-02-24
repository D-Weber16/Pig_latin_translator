normie = input("Please enter your word/phrase: \n").lower().strip(".,?! ").split()
pig_latin = []
def word_split(word): #splits iterable word into list of characters
  return list(word)

def listToString(s):
  str1 = " "
  return(str1.join(s))

vowels = ('a','e','i','o','u')
for word in normie:
  if word.startswith(vowels,0,2) == True: #loop for words beginning with vowel
    temp = word_split(word) #creates temporary list of letters from iterable
    temp.append("hay")
    pig_latin.append(''.join(temp))

  elif word.startswith(vowels) == False: #loop for words beginning with consonant
    temp1 = word_split(word)
    temp_first = temp1.pop(0) #removes and stores first consonant
    temp1.append(temp_first)
    if word.startswith(vowels,1) == False: #nested loop for consonant clusters
      temp_second = temp1.pop(0) #removes and stores second Consonant
      temp1.append(temp_second)
    temp1.append("ay")
    pig_latin.append(''.join(temp1))
print("Pig Latin: ", listToString(pig_latin))
