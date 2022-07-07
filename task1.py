def task(array):
    '''
    Searches the index of a first zero in the sequence
    '''
    has_zero = False
    founded_index = 0
    for index, element in enumerate(array):
        if element == '0':
            founded_index = index
            has_zero = True
            break

    if has_zero:
        return founded_index
    else:
        return 'Error! There is no zero!'


# Some tests:
tests = (
    '1110000000000000000000000000000000000000000000000000000000000000',
    '1111',
    '0000',
    '1111111111111111111111111111111111111111111111111111111111111000',
)

for test in tests:
    print(task(test))
