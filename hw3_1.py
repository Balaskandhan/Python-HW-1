def bunny_ear_calculation(num_of_bunnies):
    if num_of_bunnies == 0:
        return 0
    elif num_of_bunnies % 2 == 0:
        return bunny_ear_calculation(num_of_bunnies-1)+3
    else:
        return bunny_ear_calculation(num_of_bunnies-1)+2


num_of_bunnies = int(input("Enter number of bunnies"))
num_of_ears = bunny_ear_calculation(num_of_bunnies)
print(num_of_ears)