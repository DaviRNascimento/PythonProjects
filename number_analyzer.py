'''
This code below ask some numbers and return them after make some analysis
'''

def get_number():
    all_numbers = []
    print("Type here 10 different real numbers for our analysis: \n")

    while len(all_numbers) < 10:
        try:
            number = int(input())
            if number in all_numbers:
                print("Type a differnt value: ")
                continue
            all_numbers.append(number)

        except ValueError:
            print("Has to be a Real Value. Try again :")

    return all_numbers


def classify_numbers():
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    prime_numbers = [num for num in odd_numbers if is_prime(num)]

    if 2 in even_numbers:
        prime_numbers.insert(0, 2)

    return even_numbers, odd_numbers, prime_numbers


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
    
            
def print_values(numbers, even_numbers, odd_numbers, prime_numbers):
    print(f"You typped {len(numbers)} numbers and they are: {', '.join(map(str, numbers))}")

    if len(even_numbers) < 1:
        print("There is not a even value")
    else:
        print(f"You typped {len(even_numbers)} even numbers and they are: {', '.join(map(str, even_numbers))}")

    if len(odd_numbers) < 1:
        print("There is not a odd value")
    else:
        print(f"You typped {len(odd_numbers)} odd numbers and they are: {', '.join(map(str, odd_numbers))}")

    if len(prime_numbers) < 1:
        print("There is not a prime value")
    else:
        print(f"You typped {len(prime_numbers)} prime numbers and they are: {', '.join(map(str, prime_numbers))}")

    print(f"The average of the values you entered is: {sum(numbers) / len(numbers)}")


numbers = get_number()
even_numbers, odd_numbers, prime_numbers = classify_numbers()
print_values(numbers, even_numbers, odd_numbers, prime_numbers)

