# In this file, you will be solving problems that will require you to use loop
# You have to implement each of the following functions one by one
# The methods that you need to employ to solve these problems are mostly discussed in class
# Do not copy code for anything from the Internet -- In all likelihood I would know if its copied.
# The primary goal of this homework is to test if you can write code for solutions that you already know
# Spend half of the time in sketching the solutions first and test your solutions on paper
# Flowcharts are easier to dry run against test cases
# Delete the word "pass" and start implementing the following function
# You are not allowed to change the name of the functions and number of arguments passed to it
# You can, however, write helper functions if you need to


# SAMPLE for testing
def test_loop(input_list):
    index = 0
    number_of_items = len(input_list)
    while index<number_of_items:
        print(input_list[index],end=",")
        index = index+1 # index of the next item
=======
    while index < number_of_items:
        print(input_list[index] , end=",")
        index = index+1
        # index of the next item
>>>>>>> 4340b7c (Initial commit)
        # if you dont increment your program will get into infinite loop and get stuck
        # You can use Ctr+C to get out

# REQUIRED
def get_the_largest(list_of_items):
    # This function takes a list of items, and returns the one that is the largest
    # If there are more than one largest then return the largest number as well as the number of times
    # the largest has occurred in the list
    # You MUST NOT SORT THE LIST, else you will receive ZERO points
<<<<<<< HEAD
    pass
=======
    index = 0
    number_of_items = len(list_of_items)
    largest = list_of_items[index]
    count = 0
    while index < number_of_items:
        if list_of_items[index] > largest:
            largest = list_of_items[index]
        elif list_of_items[index] == largest:
            largest = list_of_items[index]
            count = count + 1
        index = index + 1

    else:
        print(largest, count)
>>>>>>> 4340b7c (Initial commit)

# REQUIRED
def get_the_smallest(list_of_items):
    # This function takes a list of items, and returns the one that is the smallest
    # If there are more than one smallest then return the smallest number as well as the number of times
    # the smallest has occurred in the list
<<<<<<< HEAD
    # You MUST NOT SORT THE LIST, else you will receive ZERO points
    pass

# REQUIRED
def get_the_sum(list_of_numbers):
    # This function takes a list of numbers, add them one by one, and returns the sum
<<<<<<< HEAD
    pass
=======

    index = 0
    number_of_items = len(list_of_numbers)
    total = 0
    while index < number_of_items:
        total = total + list_of_numbers[index]
        index = index + 1
    print(total)
>>>>>>> 4340b7c (Initial commit)


# REQUIRED
def get_the_products(list_of_numbers):
    # This function takes a list of numbers, add them one by one, and returns the sum
<<<<<<< HEAD
    pass
=======

    index = 1
    number_of_items = len(list_of_numbers)
    total = list_of_numbers[0]
    while index < number_of_items:
        total = total * (list_of_numbers[index])
        index = index + 1
    print(total)
>>>>>>> 4340b7c (Initial commit)

# REQUIRED
def is_prime_algo2(a_positive_number):
    # This function takes a_positive_number, test whether the number is prime or not
    # Returns True if Prime, else False
    # Implement the algorithm2 that we have studied in the class
<<<<<<< HEAD
    pass
=======
    n = int(a_positive_number ** .5)
    for i in range(2, n):
        if (a_positive_number % i) == 0:
            print("False")
            break

    else:
        print("True")
>>>>>>> 4340b7c (Initial commit)

# REQUIRED
def is_prime_algo3(a_positive_number):
    # This function takes a_positive_number, test whether the number is prime or not
    # Returns True if prime, else False
    # Implement the algorithm3 that we have studied in the class
<<<<<<< HEAD
    pass
=======
    n = int(a_positive_number ** .5)
    if (a_positive_number % 2 == 0) or (a_positive_number % 3 == 0):
        print("False")
    elif (n - 1) % 6 == 0:
        print("False")
    elif (n - 1) % 6 == 0:
        print("False")
    else:
        for i in range(2, n):
            if (a_positive_number % i) == 0:
                print("False")
                break

        else:
            print("True")
>>>>>>> 4340b7c (Initial commit)

# OPTIONAL
def get_the_top_two(list_of_items):
    # This function takes a list of items, and returns the top two items
    # You MUST NOT SORT THE LIST, else you will receive ZERO points
<<<<<<< HEAD
    pass
=======
    largest = 0
    largest2 = 0
    length = len(list_of_items)
    index = 0
    while index < length:
        if list_of_items[index] > largest:
            largest = list_of_items[index]
        index = index + 1
    list_of_items.remove(largest)

    index = 0
    length = length - 1
    while index < length:
        if list_of_items[index] > largest2:
            largest2 = list_of_items[index]
        index = index + 1

    print(largest, largest2)
>>>>>>> 4340b7c (Initial commit)
