def highest_number_cubed(limit):
    number = 1
    while number**3 < limit:
        number = number + 1
    return number - 1

# The above program seems to work in REPL, but I am having trouble running the tests in the terminal here in Cloud9

def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
