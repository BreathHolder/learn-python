'''
This next function will give us the values from a list at every odd index. We will need to accept a list of numbers as an input parameter and loop through the odd indices instead of the elements. Here are the steps needed:

1. Define the function header to accept one input which will be our list of numbers
2. Create a new list which will hold our values to return
3. Iterate through every odd index until the end of the list
4. Within the loop, get the element at the current odd index and append it to our new list
5. Return the list of elements which we got from the odd indices.
'''

def odd_indices(lst):
    held_lst = []
    for index in range(1, len(lst), 2):
        held_lst.append(lst[index])
    return held_lst

print(odd_indices([4, 3, 7, 10, 11, -2]))