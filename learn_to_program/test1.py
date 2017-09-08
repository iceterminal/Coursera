def shift_left(L):
    ''' (list) -> NoneType
    Shift each item in L one position to the left and shift the first item to the last position.
    Precondition: len(L) >= 1
    '''
    first_item = L[0]
    for i in range(1, len(L)):
        L[i - 1] = L[i]
    L[-1] = first_item # takes original L[0] & puts it to end of list

letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4, 5]
print(shift_left(letters))
print(letters)
print(shift_left(numbers))
print(numbers)
