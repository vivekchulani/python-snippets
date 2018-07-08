def is_even(x):
    if x %2 == 0:
        return True
    else:
        return False

def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x = x // 10
        print x
    return total

def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

def reverse(text):
  newString = ""
  textLength = len(text)
  while textLength > 0:
    newString += text[textLength - 1]
    textLength = textLength - 1
  return newString

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
  total = 0
  for letter in word.lower():
    total = total + score[letter]
  return total
