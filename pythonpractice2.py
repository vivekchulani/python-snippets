pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
else:
    print 'empty'


def hotel_cost(days):
  #The hotel cost 140 per night
  return 140 * (days)

def plane_ride_cost(city):
  if (city == "Charlotte"):
    return 183
  if (city == "Tampa"):
    return 220
  if (city == "Pittsburgh"):
   	return 222
  if (city == "Los Angeles"):
    return 475
  
def rental_car_cost(days):
  #Car costs 40 each day
  car_cost = days * 40
  if (days >= 7):
    return car_cost - 50
  elif (days >= 3 and days < 7):
    return car_cost - 20
  else:
    return car_cost
  
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money
  
print trip_cost("Los Angeles", 5, 600)
