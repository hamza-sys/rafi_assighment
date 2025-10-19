# create an empty dictionary
even_numbers_data = {}

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

        even_numbers_data[startEndNumbers] = {
            "sum": sum(even_numbers),
            "average": round(sum(even_numbers) / len(even_numbers)),
            "count": len(even_numbers) 
        }

        print(even_numbers_data)

        run_programme_again = input('if you want to run the programme with a new pair of numbers press Y')

        if run_programme_again.lower() == "Y".lower():
            process_even_numbers()

    else:
       print('Enter Numbers only')
       return process_even_numbers()



process_even_numbers()