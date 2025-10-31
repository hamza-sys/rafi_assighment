
numbers = []

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def identify_primes():

    # ask the user for input    
    print('Enter a positive integer. Type "finish" to stop.')

    # repeatedly ask the user to enter positive integers
    while True:
        user_input = input('Enter a number: ')

        if user_input.lower() == 'finish':
            break
        
        # check if the user enter a number or not
        if user_input.isdigit():
            number = int(user_input)
            if number > 0:
                numbers.append(number)
        else:
            print('Please enter a valid number or "finish".')

    primes = [num for num in numbers if is_prime(num)]

    if primes:
        if len(primes) == 1:
            print('The only prime numbers is ' + str(primes[0]))
        else:
            # Initialize smallest and largest with the first prime
            smallest = primes[0]
            largest = primes[0]

            # Loop through the list to find smallest and largest
            for num in primes:
                if num < smallest:
                    smallest = num
                if num > largest:
                    largest = num
                
            print('Minimum prime is: ' + str(smallest))
            print('Maximum prime is: ' + str(largest))

            print('Total numbers entered by user are ' + str(numbers))
            print('Total prime numbers are ' + str(primes))

            sum_of_all_primes = 0
            for n in primes:
                sum_of_all_primes += n

            return {
                    'all numbers': numbers,
                    'primes': primes,
                    'count_numbers': len(numbers),
                    'count_primes': len(primes),
                    'sum_primes': sum_of_all_primes,
                    'min_prime': smallest,
                     'max_prime': largest
                    }
        
    else:
        print('No prime numbers were entered.')



result = identify_primes()
print(result)
print('Student ID - 100536294')

# I wrote this program according to the instructions given in the question, handling inputs and validating them without using try-except statements, and checking each input to ensure it meets the required criteria. I faced no difficulties while writing this program, as the instructions were clear about what to do and how to do it. The program can be further improved by removing some of the restrictions mentioned in the question, allowing for more flexible solutions based on specific needs.