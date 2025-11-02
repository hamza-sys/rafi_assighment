# create an empty dictionary
even_numbers_data = {}

# the main function to handle all logic for processing even numbers
def process_even_numbers():
    # Ask user for input
    int1 = input("Enter Integer1: ")
    int2 = input("Enter Integer2: ")

    #  check if both the numbers are positive
    if int1.isdigit() and int2.isdigit():
        if int1 > int2:
            print('the first number must be smaller than the second number')
            return process_even_numbers()
        start = int(int1)
        end = int(int2)
    
        # list to store even numbers
        even_numbers = []
        
        # loop to append even numbers to list
        i = start
        while i <= end:
            if i % 2 == 0:
                even_numbers.append(i)
            i += 1

        print(even_numbers)
        print(sum(even_numbers))
        if even_numbers:
            print(round(sum(even_numbers) / len(even_numbers)))
        print(len(even_numbers))

        startEndNumbers = (start, end)

        # store result in the dictionary
        even_numbers_data[startEndNumbers] = {
            "sum": sum(even_numbers),
            "average": round(sum(even_numbers) / len(even_numbers)),
            "count": len(even_numbers) 
        }

        print(even_numbers_data)
        print('Student ID - 100536294')

        #ask the user if he/she wants to run the program again
        run_programme_again = input('if you want to run the programme with a new pair of numbers press "Y" otherwise press any key other than "Y".')
        if run_programme_again.lower() == "Y".lower():
            process_even_numbers()

    else:
       print('Enter Numbers only')
       return process_even_numbers()

# calling the process_even_numbers function
process_even_numbers()


# I wrote this program in a very basic way, handling input validation manually without using any of Python’s built-in methods. It follows a step-by-step approach without using try and except.
# This program can be improved by leveraging the full power of Python — using its built-in methods and language features.