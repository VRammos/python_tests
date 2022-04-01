from random import randrange, seed
seed(13) 
randrange(10,35)
ages = []

for age in range(5):
  ages.append(randrange(10,35))

print(ages)

def verify_if_can_drive(ages):
  for age in ages:
    if age >= 18:
      print(f"With {age} years old, you have permition to drive")
  else:
    print(f"With {age} years old, you don't have permition to drive")

verify_if_can_drive(ages)
