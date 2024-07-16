
import random
number = random.randint(-10,10)
while True:
    number = int(number)
    
    if number > 0:
        print(f"positive={number}"/n)
    elif number == 0:
        print(f"zero={number}"/n)
    else:
        print(f"negative={number}"/n)
