def list_divide(numbers, divide=2):
    count = 0
    for element in numbers:
        if element % divide == 0:
            count += 1
    return count


class ListDivideException(Exception):
    pass

def test_list_divide():

    if list_divide([1,2,3,4,5]) != 2:
        raise ListDivideException()
    elif list_divide([2,4,6,8,10]) != 5:
        raise ListDivideException()
    elif list_divide([30,54,63,98,100], 10) != 2:
        raise ListDivideException()
    elif list_divide([]) != 0:
        raise ListDivideException()
    elif list_divide([1,2,3,4,5], 1) !=5:
        raise ListDivideException()

test_list_divide()









