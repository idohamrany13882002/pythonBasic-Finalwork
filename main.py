def exc_1():
    """
    Write a for loop that prints the numbers from 12 to 24.
    :return:
    """
    print("exc.1:", end=" ")
    for i in range(12, 25):
        print(i, end=" ")
    print()


def exc_2():
    """
    Write a for loop that prints the ODD numbers from 7 to 31
    :return:
    """
    print("exc.2:", end=" ")
    for i in range(7, 32, 2):
        print(i, end=" ")
    print()


def exc_3():
    """
    Write a for loop that prints the EVEN numbers from 10 to -20.
    :return:
    """
    print("exc.3:", end=" ")
    for i in range(10, -21, -2):
        print(i, end=" ")
    print()


def exc_4():
    """
    Write a for loop that iterates through all numbers from 1 to 45. Print the
    following:
    ● For each number that multiples of 3 print “Fizz”
    ● For each number that multiples of 5 print “Buzz”
    ● For each number that multiples of 3 and 5 print “FizzBuzz”
    :return:
    """
    print("exc.4:", end=" ")
    for i in range(1, 46):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")

        else:
            print(i, end=" ")
    print()


def exc_5(l1: list[int]):
    """
    Write a function that receives an array as a parameter and calculates the sum
    of all the numbers in the given array (don’t use sum() function).
    For example if the given array is: [1,13,22,123,49,34,5,24,57,45]
    The result should be 373
    :param l1:
    :return:
    """
    print("exc.5:", end=" ")
    res: int = 0
    for i in l1:
        res += i
    print(res)


def exc_6(students: list[dict[str, object]]):
    """
    Write a function that receives an array of objects.
    Each object should represent a student with the properties:
    ● id
    ● first name
    ● last name
    ● age
    ● country
    ● city
    In addition, the function should receive a property to change.

    1 - The function should check for each property in each object in the array if
    the given property exists and if it does, the function should delete it from the
    object.
    2 - Write a function that prints each property of each object in the given array.
    3 - Write a function that sorts the array by the students age from the oldest to
    the youngest and return the sorted array.
    :param students:
    :return:
    """
    print("exc.6:", end=" ")

    for student in students:
        for i in student.keys():
            keys_to_keep: list[str] = []
            if not i in keys_to_keep:
                keys_to_keep.append(i)
            else:
                student.pop(i)

    print(sorted(students, key=lambda x: x['age'], reverse=True))


def exc_7_1(our_pets: list[object]):
    """
    our_pets = [{"animal_type": "cat","names": ["Meowzer","Fluffy","Kit-Cat"]},{"animal_type": "dog","names": ["Spot","Bowser","Frankie"]}]
    1 - Write a function that receives the array shown above and prints only
    animalType: cat.
    :return:
    """
    # print("exc.7:", end=" ")
    for pet in our_pets:
        if pet["animal_type"] == "cat":
            print("exc 7.1:", f"animalType: {pet["animal_type"]}")


def exc_7_2(our_pets: list[object], animal_type: str):
    """
    our_pets = [{"animal_type": "cat","names": ["Meowzer","Fluffy","Kit-Cat"]},{"animal_type": "dog","names": ["Spot","Bowser","Frankie"]}]
    2 - Write a function that receives the array shown above and the animal type.
    The function should print all names of that animal type if this type exists in the
    object.
    :param our_pets:
    :param animal_type:
    :return:
    """
    for pet in our_pets:
        if pet["animal_type"] == animal_type:
            print("exc 7.2:", f"names of {animal_type}s: {pet["names"]}")


def exc_7_3(our_pets: list[object], name: str):
    """
    our_pets = [{"animal_type": "cat","names": ["Meowzer","Fluffy","Kit-Cat"]},{"animal_type": "dog","names": ["Spot","Bowser","Frankie"]}]
    3 - Write a function that that receives the array shown above and animal name
    The function should add the specified animal name to each ‘names’ array in
    each animal_type if that name does not exist in the ‘names’ array.
    :param our_pets:
    :return:
    """
    for pet in our_pets:
        if name not in pet["names"]:
            pet["names"].append(name)
    print("exc.7.3:", our_pets)


def exc_8():
    """
    student = {'name': 'John','age': 20,'hobbies': ['reading', 'games', 'coding'],}
    1 - Write a function that prints all the student data (each student property
    should be printed in a new line).
    2 - Write a function that receives the student object and a hobby, the function
    should add the hobby to the student's hobbies array if it’s not exist already.
    3 - Use the function that you wrote in ex 1 to print the data of the student and
    check that the new hobby has been added.
    4 - Write a function that receives an object of a student and hobby, the
    function should delete the hobby from the student's hobbies.
    5 - Use the function that you wrote in ex 1 to print the data student and check
    that the hobby has been deleted from the object student.
    6 - Add to the object student new property: family_name and add a value.
    :return:
    """
    print("exc.8:", end=" ")


def exc_9():
    """
    Write a function that prints all the elements of a 2D array using nested for
    loops.
    matrix =[[1, 2],[3, 4],[5, 6]]
    print_matrix(matrix) → Should print: 1 2 3 4 5 6
    :return:
    """
    print("exc.9:", end=" ")


def exc_10():
    """
    Write a function to count how many numbers of zeros appear in a 2D matrix
    using nested for loops and increment operation.
    matrix =[[0,1,1],[0,1,0],[1,0,0]]
    print(zero_count(matrix)) → Should print: 5
    :return:
    """
    print("exc.10:", end=" ")


def exc_11():
    """
    Write a function to return an array of all the elements that are repeated more
    than once in a given array.
    arr = [4,2,34,4,1,12,1,4]
    print(find_dup(arr)) Should print: [4, 1]
    :return:
    """
    print("exc.11:", end=" ")


def exc_12():
    """
    Write a function using a for loop that gets an array and returns a new array
    with the elements from the given array appearing in reverse order. (Don’t use
    array reverse() method)
    For example:
    arr = [43, "what", 9, true, "cannot", false, "be", 3, true];
    Function output should be:
    [ture, 3, “be”, false, “cannot”, true, 9, “what”, 43]
    :return:
    """
    print("exc.12:", end=" ")


def exc_13():
    """
    Given two arrays of integers. Add up each element in the same position and
    create a new array containing the sum of each pair.
    Assume both arrays are of the same length.
    For example:
    first_array = [4, 6, 7];
    second_array = [8, 1, 9];
    Function output should be:
    [12, 7, 16]
    :return:
    """
    print("exc.13:", end=" ")


def exc_14():
    """
    Write a program that will check if two strings are palindromes.
    A palindrome is a word that spells the same forward and backward.
    Palindrome: a word, phrase, or sequence that reads the same backward as
    forward, examples for valid palindromes: madam, nurses run.
    For example:
    first_str = "racecar"
    second_str = "Java"
    Function output should be:

    True (for first_str)
    False (for second_str)
    :return:
    """
    print("exc.14:", end=" ")


def exc_15():
    """
    Write a while loop that iterates as long as the counter is less than 100, on
    every iteration the counter is multiplied by 2 starting from 1.
    :return:
    """
    print("exc.15:", end=" ")


def exc_16():
    """
    Write a while loop that iterates as long as the counter is greater than 50 , on
    every iteration the counter is divided by 2.
    The counter should start with the value 900000 before the first iteration.
    :return:
    """
    print("exc.16:", end=" ")


def exc_17():
    """
    Write a function that gets an array of strings as parameter and returns a new
    array containing all the values that appear more than once. In your solution
    use only while loops.
    :return:
    """
    print("exc.17:", end=" ")


def exc_18():
    """
    Write a function that gets an array of strings as parameter and returns a new
    array containing all the values from the provided array in the same order but
    without any duplicated values. In your solution use only while loops.
    For example:
    names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', ‘Chris’, ‘Kevin’]
    Function output should be:
    ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor']
    :return:
    """
    print("exc.18:", end=" ")


def exc_19():
    """
    Write a function that gets an array of strings as parameter and returns a new
    array containing all the values from the provided array in the same order but
    without any duplicated values.
    If the string ‘pete’ is a value inside the array your function should skip it and
    not copy it to the new array. In your solution use only while loops.
    For example:
    names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', ‘Chris’, ‘Kevin’]
    Function output should be:
    ['Chris', 'Kevin', 'Naveed', 'Victor']
    :return:
    """
    print("exc.19:", end=" ")


def exc_20():
    """
    Use a while loop to iterate on a boolean array.
    As long as the next index is different from the previous index the iteration
    continues, otherwise, return the index of the element with the same value.
    If there are not two successive values, the function will return -1.
    For example:
    array= [true, false, false, true, true, false] → return 2
    array= [true, false, true, false, true, true]; → returns 5
    array= [true, false, true, false, true, false]; → returns -1
    :return:
    """
    print("exc.20:", end=" ")


def exc_21():
    """
    Write a python program that gets user input (use input() function for this).
    The first input will be the user full name
    Second input will be the user age
    Third input will be the user email
    Write validation for each input provided by the user and allow the user to try
    again in case the user provided invalid input.
    Validation for full name input → string type with 2 words for first name and last
    name.
    Validation for age input → int type between 1 - 130.
    Validation for email input → string type with ‘@’ inside.
    :return:
    """
    print("exc.21:", end=" ")


exc_1()
exc_2()
exc_3()
exc_4()
exc_5([1, 13, 22, 123, 49, 34, 5, 24, 57, 45])
exc_6([{"id": 1, "id": 1, "first name": "Ido", "last name": "Hamrani", "age": 22, "country": "Israel",
        "city": "Rosh-ha'ayin"},
       {"id": 2, "first name": "Danny", "first name": "Danny", "last name": "Cohen", "age": 18, "country": "USA",
        "city": "New-York"},
       {"id": 3, "first name": "Liz", "last name": "Walsh", "age": 31, "age": 31, "country": "UK", "city": "London"}])
exc_7_1([{"animal_type": "cat", "names": ["Meowzer", "Fluffy", "Kit-Cat"]},
         {"animal_type": "dog", "names": ["Spot", "Bowser", "Frankie"]}])
exc_7_2([{"animal_type": "cat", "names": ["Meowzer", "Fluffy", "Kit-Cat"]},
         {"animal_type": "dog", "names": ["Spot", "Bowser", "Frankie"]}], "dog")
exc_7_3([{"animal_type": "cat", "names": ["Meowzer", "Fluffy", "Kit-Cat"]},
         {"animal_type": "dog", "names": ["Spot", "Bowser", "Frankie"]}], "Mario")
# exc_8()
# exc_9()
# exc_10()
# exc_11()
# exc_12()
# exc_13()
# exc_14()
# exc_15()
# exc_16()
# exc_17()
# exc_18()
# exc_19()
# exc_20()
# exc_21()
