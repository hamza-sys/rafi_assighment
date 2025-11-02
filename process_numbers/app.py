
# create function to process user entered numbers
# checking for the smallest number, reverse the numbers and finding duplicates
def process_numbers():
    numbers = []

    while True:
        try:
            # taking input for the user
            user_input = float(input('Enter number: '))
            if user_input > 0:
                number = int(user_input)
                numbers.append(number)
            if user_input < 0:
                print("The list is completed")
                break
        except ValueError:
            print("Enter Number only")

    # find the smallest number in number
    smallest_number = min(numbers)
    # reverse the number
    reversed_list = list(reversed(numbers))
    duplicates = []

    # checking for duplicates
    for n in numbers:
        if numbers.count(n) > 1 and n not in duplicates:
            duplicates.append(n)

    if duplicates:
        print('Duplicate numbers found: ' + str(duplicates))
    else:
        print('No duplicate numbers found')

    print(numbers)
    print('Minimum number is ' + str(smallest_number))    
    print(reversed_list)
    print('Student ID - 100536294')

    # showing menu to the user
    print("\nMenu:")
    print("1. Add new numbers to the list")
    print("2. Remove a number from the list")

    choice = input('Enter your choice 1 or 2')

    # add number to the list
    if choice == '1':
        num = input('Enter number to add to the list ')
        if num.isdigit():
            numbers.append(int(num))
            print('Number added successfully.')
            print('The updated list is ' + str(numbers))
        else:
            print('invalid number')

    #   remove number from the list
    elif choice == '2':
        usr_num = input('Enter number to remove to the list ')
        if usr_num.isdigit():
            if int(usr_num) in numbers:
                numbers = [n for n in numbers if n != int(usr_num)]
                print('number removed successfully.')
                print('the updated list is ' + str(numbers))
            else:
                print('Number not found in the list')
        else:
            print('Enter a valid Number')

# calling the function
process_numbers()


# I wrote this program using the same strategy as in the previous question, keeping the code simple and doing everything in a very basic way. The program can be improved by using Python’s built-in features and methods. It could also be enhanced by creating a function that encapsulates the logic for adding and removing items from the list at the end of the program, but I decided to keep it as it is.