# In this file, you will be solving problems that will require you to use if else
# You have to implement each of the following functions one by one
# The methods that you need to employ to solve these problems are mostly discussed in class
# Do not copy code for anything from the Internet -- In all likelihood I would know if its copied.
# The primary goal of this homework is to test if you can write code for solutions that you already know
# Spend half of the time in sketching the solutions first and test your solutions on paper
# Flowcharts are easier to dry run against test cases
# Delete the word "pass" and start implementing the following function
# You are not allowed to change the name of the functions and number of arguments passed to it
# You can, however, write helper functions if you need to

def the_largest_of_three_number_without_loop(item1, item2, item3):
    # this function takes three items and returns the largest of them
    # if there are two or more largest the program should return all of them
    # You must not use loop to solve this problem
    # If you use the LOOP, zero points shall be awarded

    largest = 0
    if item2 > item1:
        largest = item2
    elif item3 > item1:
        largest = item3
    if item3 > item2:
        largest = item3
    elif item2 == item3:
        largest = item2, item3

    if item1 == item2:
        largest = item1, item2
        if item2 == item3:
            largest = item1, item2, item3
    print(largest)
>>>>>>> 4340b7c (Initial commit)


def does_rectangles_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    # This function takes 8 arguments i.e. 4 co-ordinates representing 2 rectangles
    # (x1,y1), and (x2, y2) represent the coordinates of the opposite corners (lower left and upper right) the first rectangle
    # (x3,y3), and (x4, y4) represent the coordinates of the opposite corners (lower left and upper right) the second rectangle
    # You can assume (and check if they are not) that the rectangles are parallel to x and y axes
    # This function would return either True or False depending on whether the inputted rectangles intersect or not


    if x2 >= x4 and y2 >= y4:
        print("True")
    elif x2 >= x3 and y2 >= y3:
        print("True")
    elif x1 >= x4 and y1 >= y4:
        print("True")
    elif x2 >= x4 and y2 >= y4:
        print("true")
    elif x1 >= x3 and y1 >= y3:
        print("True")
    else:
        print("False")
>>>>>>> 4340b7c (Initial commit)
