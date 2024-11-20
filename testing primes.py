numbers = []
print("How high do you want to check for primes to?")
# add all the numbers the user want to be checked if prime
for x in range(2, int(input("Inter here:"))+1, 1):
    numbers.append(x)
# time 5.56 seconds
# loop for checking all numbers in the list to see if their prime
for z in range(0, len(numbers), 1):
    try:
        for y in range(z+1, len(numbers), 1):
            try:
                if numbers[y] % numbers[z] == 0:
                    del numbers[y]
            except IndexError:
                continue
    except IndexError:
        continue
for a in range(0, len(numbers), 5):
    print(numbers[a: a+5])
