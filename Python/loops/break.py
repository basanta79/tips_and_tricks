

def test_break_in_for():

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    for data in array:
        if data > 5:
            break
        print(data)


test_break_in_for()
