# function to find an even number of evens
def even_number_of_evens(numbers):
    """
    Should raise a TypeError if a list is not passed into the
    function
    error mesg: "A list was not passed into the function"
    Return False if:
    -numbers is empty
    -number of evens is odd
    -number of evens is 0
    Return True if:
    -number of evens is even
    """

    # (REFACTORED) code for raising TypeError if not a list passed in
    if isinstance(numbers, list):
        evens = 0
        # counting number of evens
        evens = sum([1 for num in numbers if num % 2 == 0])
        # checks if evens != 0 and if there is an odd/even amount
        return True if evens and evens % 2 == 0 else False
    # raises a TypeError if numbers is not a list
    else:
        raise TypeError("A list was not passed into the function")


# # (created with the tests - non-refactored)
#     if isinstance(numbers, list):
#         # returning false if [] is empty (covered by evens=0 check)
#         if len(numbers) == 0:
#             return False
#         else:
#             evens = 0
#         # counting number of evens
#         for num in numbers:
#             if num % 2 == 0:
#                 evens += 1
#         # checks if evens != 0 and if there is an odd/even amount
#         if evens:
#             return evens % 2 == 0
#         else:
#             return False
#     # raises a TypeError if numbers is not a list
#     else:
#         raise TypeError("A list was not passed into the function")


# stops this being triggered by running test_evens.py
if __name__ == '__main__':
    print(even_number_of_evens(5))
